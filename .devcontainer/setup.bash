mkdir -p lib
cd lib

apt-get update --fix-missing
apt-get upgrade -y

. /opt/ros/jazzy/setup.sh

if [[ ! -d "ros_odrive" && "$ENABLE_ODRIVE" ]]; then
    git clone https://github.com/odriverobotics/ros_odrive.git
fi

if [[ ! -d "imu_ros2" && "$ENABLE_IMU" ]]; then
    git clone https://github.com/analogdevicesinc/imu_ros2.git
fi

# if [[ ! -d "libiio" && "$IMU_ENABLED" ]]; then
if [[ "$ENABLE_IMU" ]]; then
    # git clone https://github.com/analogdevicesinc/libiio.git --branch v0.26
    cd libiio

    mkdir -p build && cd build 

    cmake_options=""
    if [ "$IMU_BACKEND" == "LOCAL" ]; then
        cmake_options+="-DWITH_USB_BACKEND=OFF"
        cmake_options+=" -DHAVE_DNS_SD=OFF"
        cmake_options+=" -DWITH_XML_BACKEND=OFF"
        cmake_options+=" -DWITH_NETWORK_BACKEND=OFF"
    fi

    if ["$IMU_BACKEND" == ""]

    echo "$cmake_options"

    cmake $cmake_options ../ 
     
    make && sudo make install

    cd ../..
fi

cd ..

echo '. /opt/ros/jazzy/setup.sh' >> ~/.bashrc
