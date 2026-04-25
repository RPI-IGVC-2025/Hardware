import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from message_filters import ApproximateTimeSynchronizer, Subscriber
import cv2
import numpy as np

from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Header
import sensor_msgs_py.point_cloud2 as pc2

from rclpy.qos import QoSProfile, ReliabilityPolicy
from message_filters import Subscriber
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped

class CVNode(Node):
    def __init__(self):
        super().__init__('cv_node')
        self.bridge = CvBridge()

        # Gaussian blur
        self.declare_parameter("blur_kernel_size", 11)
        self.declare_parameter("blur_sigma_x", 33.0)
        self.declare_parameter("blur_sigma_y", 33.0)

        # Canny edge detection
        self.declare_parameter("canny_low", 10)
        self.declare_parameter("canny_high", 100)

        # Hough Line Transform
        self.declare_parameter("hough_rho", 2.0)
        self.declare_parameter("hough_theta", np.pi / 180)
        self.declare_parameter("hough_threshold", 10)
        self.declare_parameter("hough_min_line_length", 4)
        self.declare_parameter("hough_max_line_gap", 5)

        self.declare_parameter("line_thickness", 10)
        
        

        # Synchronised RGB + PointCloud subscribers
        qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            depth=10
        )

        self.rgb_sub = Subscriber(
            self,
            Image,
            '/camera/camera/color/image_raw',
            qos_profile=qos
        )

        self.pc_sub = Subscriber(
            self,
            Image,
            '/camera/camera/depth/image_rect_raw',
            qos_profile=qos
        )
        
        
        self.sync = ApproximateTimeSynchronizer(
            [self.rgb_sub, self.pc_sub],
            queue_size=10,
            slop=0.05
        )
        self.sync.registerCallback(self.process)
        # ===== Publishers =====

        self.pc_pub = self.create_publisher(PointCloud2, 'cv_points', 10)
        self.left_pub = self.create_publisher(Path, '/left_boundary', 10)
        self.right_pub = self.create_publisher(Path, '/right_boundary', 10)
        
        self.get_logger().info("Node started")

        # Camera parameters based on factor calibration file
        self.fx = 1401.07
        self.fy = 1401.07
        self.cx = 1062.32
        self.cy = 634.124
        
    def lines_to_path(self, lines, depth_frame, stamp):
        path = Path()
        path.header.stamp = stamp
        path.header.frame_id = 'camera_link' # TODO check if this matches TF tree
        
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            
            # add both endpoints as separate poses
            for u, v in [(x1, y1), (x2, y2)]:
                if v >= depth_frame.shape[0] or u >= depth_frame.shape[1]:
                    continue
                
                Z = float(depth_frame[v, u])
                if not np.isfinite(Z) or Z <= 0:
                    continue
                
                X = (u - self.cx) * Z / self.fx
                Y = (v - self.cy) * Z / self.fy
                
                pose = PoseStamped()
                pose.header = path.header
                pose.pose.position.x = X
                pose.pose.position.y = Y
                pose.pose.position.z = Z
                pose.pose.orientation.w = 1.0
                path.poses.append(pose)
                
        return path
        
    def process(self, rgb_msg: Image, depth_msg: Image):
        self.get_logger().info("Called Process()")
        # Fetch parameters
        blur_k = self.get_parameter("blur_kernel_size").value
        blur_sx = self.get_parameter("blur_sigma_x").value
        blur_sy = self.get_parameter("blur_sigma_y").value
        canny_low = self.get_parameter("canny_low").value
        canny_high = self.get_parameter("canny_high").value
        hough_rho = self.get_parameter("hough_rho").value
        hough_theta = self.get_parameter("hough_theta").value
        hough_thresh = self.get_parameter("hough_threshold").value
        hough_min_len = self.get_parameter("hough_min_line_length").value
        hough_max_gap = self.get_parameter("hough_max_line_gap").value
        thickness = self.get_parameter("line_thickness").value

        # Convert ROS image to OpenCV
        frame = self.bridge.imgmsg_to_cv2(rgb_msg, 'bgr8')
        depth_frame = self.bridge.imgmsg_to_cv2(depth_msg, desired_encoding='passthrough')
        h, w  = frame.shape[:2]

        # Convert to grayscale
        gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Gaussian Blur
        blur  = cv2.GaussianBlur(gray, (blur_k, blur_k), blur_sx, blur_sy)
        
        # Canny edge detection
        edges = cv2.Canny(blur, canny_low, canny_high)

        # Hough Line Transform
        lines = cv2.HoughLinesP(
            edges,
            hough_rho, hough_theta, hough_thresh,
            minLineLength=hough_min_len,
            maxLineGap=hough_max_gap
        )

        # Mask of detected line segments
        line_mask  = np.zeros((h, w), dtype=np.uint8)
        line_image = np.zeros_like(frame)

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line.reshape(4)
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 255), thickness)
                cv2.line(line_mask, (x1, y1), (x2, y2), 255, thickness)

        # Look up depth for each white pixel directly
        white_v, white_u = np.where(line_mask > 0)
        distances = depth_frame[white_v, white_u]
        
        valid = np.isfinite(distances) & (distances > 0)
        white_u = white_u[valid]
        white_v = white_v[valid]
        distances = distances[valid]

        #points to 3D
        Z = distances
        X = (white_u - self.cx) * Z / self.fx
        Y = (white_v - self.cy) * Z / self.fy

        #create pointcloud
        points = np.vstack((X, Y, Z)).T

        header = Header()
        header.stamp = self.get_clock().now().to_msg()
        header.frame_id = ""

        cloud_msg = pc2.create_cloud_xyz32(header, points.tolist())
        
        self.get_logger().info(f"cloud: {pc2.read_points(cloud_msg, field_names=("x", "y", "z"), skip_nans=True)[0][0]}")
        self.get_logger().info(f"points shape: {points.shape}")
        self.get_logger().info(f"num points: {len(points)}")
        
        self.pc_pub.publish(cloud_msg)
        
        
def main(args=None):
    rclpy.init(args=args)
    node = CVNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()