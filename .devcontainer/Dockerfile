FROM ros:jazzy

# Modify existing ubuntu user to use /home/ros2_ws as home
RUN usermod -d /home/ros2_ws -m ubuntu \
    && apt-get update \
    && apt-get install -y sudo \
    && echo ubuntu ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/ubuntu \
    && chmod 0440 /etc/sudoers.d/ubuntu

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-pip

RUN apt-get update \
# Missing ROS packages
&& apt-get install -y ros-jazzy-rqt* \
# Camera Lib
ros-jazzy-depthai-ros \
# IMU Lib dependencies
libxml2 libxml2-dev bison flex libcdk5-dev cmake libaio-dev libusb-1.0-0-dev libserialport-dev libxml2-dev libavahi-client-dev doxygen graphviz

# Gazebo GUI on Mac: virtual display + VNC 
RUN apt-get update && apt-get install -y --no-install-recommends xvfb x11vnc \
    && rm -rf /var/lib/apt/lists/*

ENV SHELL /bin/bash

# USER $USERNAME
USER ubuntu

# [Optional] Set the default user. Omit if you want to keep the default as root.
CMD ["/bin/bash"]