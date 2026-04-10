mkdir -p lib
cd lib

apt-get update --fix-missing
apt-get upgrade

. /opt/ros/jazzy/setup.sh

if [ ! -d "ros_odrive" ]; then
    git clone https://github.com/odriverobotics/ros_odrive.git
fi

if [ ! -d "imu_ros2" ]; then
    git clone https://github.com/analogdevicesinc/imu_ros2.git
fi

if [ ! -d "robot_self_filter" ]; then
    git clone https://github.com/leggedrobotics/robot_self_filter.git
fi

if [ ! -d "libiio" ]; then
    git clone https://github.com/analogdevicesinc/libiio.git --branch v0.26
    cd libiio

    mkdir -p build && cd build && cmake ../ && make && sudo make install

    cd ../..
fi

cd ..

echo '. /opt/ros/jazzy/setup.sh' >> ~/.bashrc
