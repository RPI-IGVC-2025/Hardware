FROM ros:jazzy
ARG USERNAME=$USERNAME
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Delete user if it exists in container (e.g Ubuntu Noble: ubuntu)
RUN if id -u $USER_UID ; then userdel `id -un $USER_UID` ; fi

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m -d /home/ros2_ws $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
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

USER $USERNAME

# [Optional] Set the default user. Omit if you want to keep the default as root.
CMD ["/bin/bash"]
