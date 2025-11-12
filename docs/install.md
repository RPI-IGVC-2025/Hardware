# Installation
1. Follow the ROS/Docker [setup guide](https://docs.google.com/document/d/1-VyvY_TrujEbJ-1xbitBwOAzUDWoNYXUCovK7mJRQQ4/edit?tab=t.0)
2. ``sudo apt install ros-rolling-ros2-control ros-rolling-ros2-controllers``
3. In your top-level directory create a workspace directoy and an src directory inside of it.
    ``mkdir -p {your_workspace}/src``
4. cd into your src subdirectory
5. Clone this repository
    - git swtich to feature/minimal-simulation, as it's currently the only one with a fleshed out package.xml
6. run ``rosdep install -r -y --from-paths . --ignore-src `` to install the ROS packages
7. cd up one directory
8. ``source opt/ros/jazzy/setup.bash ``
9. ``colcon build --symlink-install``
    - you can add ``--cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -G Ninja`` if you want to create a compile_commands.json for native support with IDEs like CLion

# Opening
## VS code
1. cd to {your_workspace}
2. ``source opt/ros/jazzy/setup.bash``
3. ``source install/setup.bash``
4. ``code .``

## CLion

1. Follow [these instructions](https://www.jetbrains.com/help/clion/ros-setup-tutorial.html)
    - For this to properly work, you need to open CLion from the terminal, sourced to the ROS and workspace setup files. I've decided that I'm not going to bother with this because I'd have to do it from powershell (icky) instead of WSL. If you come up with a better solution, add it here.


# Running

1. ensure your working directory is {your_workspace}
2. ``source install/setup.bash``
3. ros2 launch rrc_igvc_bot bot.launch.py - WON'T WORK YET
