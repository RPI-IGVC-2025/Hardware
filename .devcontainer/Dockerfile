FROM ros:jazzy
ARG USERNAME=$USERNAME
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ARG PLATFORM="LINUX"
ARG SIM_ENABLED=true

ARG DEPLOYABLE_BUILD=false
ARG IMU_ENABLED=DEPLOYABLE_BUILD
ARG ZED_DEV_PLATFORM=DEPLOYABLE_BUILD

ARG MOUNT_CUDA=false

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

# Unconditional installs
RUN apt-get install -y 
    python3-pip \
    # CycloneDDS package
    ros-jazzy-rmw-cyclonedds-cpp 

## Simulation only
RUN if $SIM_ENABLED ; then \
        apt-get install -y \
            # RQT packages
            ros-jazzy-rqt-tf-tree ros-jazzy-rqt-graph ros-jazzy-rqt-image-view \
            # Teleop control keyboard
            ros-jazzy-teleop-twist-keyboard \
            # External terminal
            # TODO: Figure out how to do on mac
            gnome-terminal dbus-x11 ; \
    fi


## MacOS 
# Gazebo GUI on Mac: virtual display + VNC + window manager (switch between Gazebo/rtabmap)
# TODO: Figure out if there isn't a better way to do this
RUN if [[ "$PLATFORM" == "MAC" ]] ; then \
        apt-get install -y --no-install-recommends \
            xvfb x11vnc fluxbox \
        && rm -rf /var/lib/apt/lists/* ; \
fi

## IMU Lib
RUN if $IMU_ENABLED ; then \
        apt-get install -y \
            limxml2 libxml2-dev libzstd-dev bison flex libcdk5-dev cmake \
            ## local backend
            libaio-dev \
            ### Uncomment to use backend other than local
            # ## USB Backend
            # libusb-1.0-0-dev
            # ## Serial backend
            # libserialport-dev
            # ## Network backend
            # libavahi-client-dev
    fi

## CUDA 
RUN if $ZED_DEV_PLATFORM ; then \
        apt-get install -y \
            zstd pciutils mesa-utils wget gnupg \
        # TODOs:
        #   Figure out mounting CUDA from host
        && if ! $MOUNT_CUDA ; then \
            wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb \
            && dpkg -i cuda-keyring_1.1-1_all.deb \
            && apt-get update \
            && apt-get install -y cuda-toolkit-13-0 ; \
        fi ; \
    fi

RUN 

## ZED SDK
RUN if $ZED_DEV_PLATFORM ; then \
        # Determine Zed link based on platform
        case $PLATFORM in \
            LINUX) \
                export ZED_LINK="https://download.stereolabs.com/zedsdk/5.2/cu13/ubuntu24" \
                ;; \

            JETSON_ORIN) \
                export ZED_LINK="https://download.stereolabs.com/zedsdk/5.2/l4t36.5/jetsons" \
                ;; \

            JETSON_THOR) \
                export ZED_LINK="https://download.stereolabs.com/zedsdk/5.2/l4t38.4/jetsons" \
                ;; \
        esac \
        # Install SDK
        && wget -O zed_installer.run $ZED_LINK \
        && chmod +x zed_installer.run \
        && ./zed_installer.run -- silent --skip_python --skip_cuda; \
fi

ENV SHELL /bin/bash

CMD ["/bin/bash"]
