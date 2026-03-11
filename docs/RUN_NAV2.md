## Running Nav2 with Gazebo (Mac + devcontainer)

- **Terminal 1 – VNC + simulation (inside devcontainer)**

```bash
cd /home/ros2_ws
source .devcontainer/start-gazebo-vnc.sh
source install/setup.bash
ros2 launch igvc_bringup bringup.launch.py use_sim:=true use_slam:=true use_mock_hardware:=true use_sim_time:=true
```

Then, from macOS, connect a VNC client to `vnc://localhost:5900` (password `vnc`).

- **Terminal 2 – Nav2 stack**

```bash
cd /home/ros2_ws
source install/setup.bash
ros2 launch igvc_nav igvc_nav.launch.py use_sim_time:=true
```

- **Terminal 3 – Send a navigation goal**

```bash
cd /home/ros2_ws
source install/setup.bash
ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "{
  pose: {
    header: { frame_id: 'map' },
    pose: {
      position: { x: 2.0, y: 0.0, z: 0.0 },
      orientation: { x: 0.0, y: 0.0, z: 0.0, w: 1.0 }
    }
  }
}"
```

