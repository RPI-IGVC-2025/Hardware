cd /home/ros2_ws

mkdir -p lib
cd lib

apt-get update --fix-missing
apt-get upgrade -y

. /opt/ros/jazzy/setup.sh


if [ ! -d "rplidar_ros" ] && $ENABLE_LIDAR ; then 
    git clone -b ros2 https://github.com/Slamtec/rplidar_ros.git
fi

if [ ! -d "ros_odrive" ] && $ENABLE_ODRIVE ; then
    git clone https://github.com/odriverobotics/ros_odrive.git
fi

if [ ! -d zed-ros2-wrapper ] && $HAS_ZED_DEPS; then 
    git clone https://github.com/stereolabs/zed-ros2-wrapper.git
fi


if $ENABLE_IMU; then 
    if [ ! -d "imu_ros2" ]; then
        git clone https://github.com/analogdevicesinc/imu_ros2.git
    fi

    if [ ! -d "libiio" ]; then
        git clone https://github.com/analogdevicesinc/libiio.git --branch v0.26
    fi
    
    cd libiio

    mkdir -p build && cd build 

    cmake_options=""

    if [ "$IMU_BACKEND" == "USB" ]; then 
        cmake_options+=" -DWITH_NETWORK_BACKEND=OFF"
        cmake_options+=" -DWITH_LOCAL_BACKEND=OFF -DWITH_IIOD=OFF"
    fi

    if [ "$IMU_BACKEND" == "NETWORK" ]; then 
        cmake_options+=" -DWITH_USB_BACKEND=OFF"
        cmake_options+=" -DWITH_LOCAL_BACKEND=OFF -DWITH_IIOD=OFF"
    fi


    if [ "$IMU_BACKEND" == "LOCAL" ]; then
        cmake_options+=" -DWITH_USB_BACKEND=OFF"
        cmake_options+=" -DWITH_NETWORK_BACKEND=OFF"
        cmake_options+=" -DWITH_XML_BACKEND=OFF"
    fi

    if [ "$IMU_BACKEND" == "XML" ]; then 
        cmake_options+=" -DWITH_USB_BACKEND=OFF"
        cmake_options+=" -DWITH_NETWORK_BACKEND=OFF"
        cmake_options+=" -DWITH_LOCAL_BACKEND=OFF -DWITH_IIOD=OFF"
    fi


    if [ "$IMU_BACKEND" == "SERIAL" ]; then 
        cmake_options+=" -DWITH_SERIAL_BACKEND=ON"

        cmake_options+=" -DWITH_USB_BACKEND=OFF"
        cmake_options+=" -DWITH_NETWORK_BACKEND=OFF"
        cmake_options+=" -DWITH_LOCAL_BACKEND=OFF -DWITH_IIOD=OFF"
    fi

    cmake --fresh $cmake_options ../ 
     
    make && sudo make install

    cd ../..
else 
    rm -rfv adi_imu libiio
fi

cd ..

echo '. /opt/ros/jazzy/setup.sh' >> ~/.bashrc

echo ' if [ -d '/home/ros2_ws/install' ]; then 
    . /home/ros2_ws/install/setup.bash
fi ' >> ~/.bashrc

