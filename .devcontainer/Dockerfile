FROM ros:jazzy
ARG USERNAME=$USERNAME
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Delete user if it exists in container (e.g Ubuntu Noble: ubuntu)
RUN if id -u $USER_UID ; then userdel `id -un $USER_UID` ; fi

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
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
ros-jazzy-teleop-twist-keyboard \
# CycloneDDS package
ros-jazzy-rmw-cyclonedds-cpp \
# IMU Lib dependencies
libxml2 libxml2-dev bison flex libcdk5-dev cmake libaio-dev libusb-1.0-0-dev libserialport-dev libxml2-dev libavahi-client-dev doxygen graphviz \
# External terminal
gnome-terminal dbus-x11 

# Camera stuff 
RUN if ["$DEPLOYABLE_BUILD == 1"]; then \
apt-get update \
&& apt-get install -y \
# Camera lib utilities
zstd pciutils mesa-utils wget gnupg \
# CUDA repo
&& wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb \
&& dpkg -i cuda-keyring_1.1-1_all.deb \
&& apt-get update \
&& apt-get install -y cuda-toolkit-13-0 \
fi

# ZED SDK
RUN if ["$DEPLOYABLE_BUILD == 1"]; then \
wget https://download.stereolabs.com/zedsdk/5.2/cu13/ubuntu24 \
&& ./ubuntu24 -- silent \
fi

# Gazebo GUI on Mac: virtual display + VNC + window manager (switch between Gazebo/rtabmap)
RUN if ["$IS_MACOS == 1"]; then \
apt-get update && apt-get install -y --no-install-recommends xvfb x11vnc fluxbox \
    && rm -rf /var/lib/apt/lists/*
fi

ENV SHELL /bin/bash

# [Optional] Set the default user. Omit if you want to keep the default as root.
CMD ["/bin/bash"]
