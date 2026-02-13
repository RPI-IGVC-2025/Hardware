#!/usr/bin/env bash
# Start a virtual X display (Xvfb) and expose it via VNC so you can run the
# Gazebo GUI inside the devcontainer and view it on your Mac.
# Run this once per container session, then connect with a VNC client to localhost:5900.

DISPLAY_NUM=99
VNC_PORT=5900

# Start Xvfb (if already running for this display, it will error and we continue)
rm -f /tmp/.X${DISPLAY_NUM}-lock
Xvfb ":$DISPLAY_NUM" -screen 0 1280x720x24 -ac &
sleep 2
echo "Xvfb on :$DISPLAY_NUM"

# VNC password so Mac Screen Sharing can connect. Use: vnc
# -passwd sets it directly (no password file)
x11vnc -display ":$DISPLAY_NUM" -rfbport $VNC_PORT -forever -shared -bg -noxdamage -passwd vnc 2>/dev/null || true
echo "VNC server on port $VNC_PORT — when prompted, password is: vnc"

echo ""
echo "1. On your Mac: connect to localhost:$VNC_PORT — password: vnc"
echo "2. In a new terminal in the container, run:"
echo "   export DISPLAY=:$DISPLAY_NUM LIBGL_ALWAYS_SOFTWARE=1"
echo "   source /home/ros2_ws/install/setup.bash"
echo "   ros2 launch igvc_gazebo empty_world.launch.py"
echo "   (do not use headless:=true)"
echo ""
