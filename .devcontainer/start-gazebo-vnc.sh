#!/usr/bin/env bash
# Start a virtual X display (Xvfb) and expose it via VNC so you can run Gazebo
# and rtabmap (and other GUIs) from bringup inside the devcontainer and view
# them on your Mac. Run once per container session, then connect with a VNC
# client to localhost:5900.
#
# IMPORTANT: You must SOURCE this script so DISPLAY is set in your shell:
#   source /home/ros2_ws/.devcontainer/start-gazebo-vnc.sh
# If you run it with ./start-gazebo-vnc.sh, the export is lost when the script exits.

DISPLAY_NUM=99
VNC_PORT=5900
# Virtual screen size: wide enough for Gazebo + rtabmap side by side
XVFB_RES="1920x1080x24"

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  echo "WARNING: Run with: source $(readlink -f "${BASH_SOURCE[0]}" 2>/dev/null || echo "$0")"
  echo "         so DISPLAY=:$DISPLAY_NUM is set in your shell (otherwise Gazebo will be headless)."
  echo ""
fi

# Start Xvfb (if already running for this display, it will error and we continue)
rm -f /tmp/.X${DISPLAY_NUM}-lock
Xvfb ":$DISPLAY_NUM" -screen 0 ${XVFB_RES} -ac &
sleep 2
echo "Xvfb on :$DISPLAY_NUM (${XVFB_RES})"

# Window manager: taskbar + click-to-focus so you can switch between Gazebo and rtabmap
DISPLAY=:$DISPLAY_NUM fluxbox &
sleep 1
echo "fluxbox (window manager) on :$DISPLAY_NUM"

# VNC password so Mac Screen Sharing can connect. Use: vnc
# -passwd sets it directly (no password file)
x11vnc -display ":$DISPLAY_NUM" -rfbport $VNC_PORT -forever -shared -bg -noxdamage -passwd vnc 2>/dev/null || true
echo "VNC server on port $VNC_PORT — when prompted, password is: vnc"

# Set DISPLAY and LIBGL for this shell AND for new terminals (so Gazebo/rtabmap use VNC)
export DISPLAY=:$DISPLAY_NUM
export LIBGL_ALWAYS_SOFTWARE=1
MARKER="# Gazebo + rtabmap VNC display (start-gazebo-vnc.sh)"
if ! grep -q "$MARKER" ~/.bashrc 2>/dev/null; then
  echo "" >> ~/.bashrc
  echo "$MARKER" >> ~/.bashrc
  echo "export DISPLAY=:$DISPLAY_NUM LIBGL_ALWAYS_SOFTWARE=1" >> ~/.bashrc
fi

echo ""
echo "1. On your Mac: connect to localhost:$VNC_PORT — password: vnc"
echo "2. In this SAME terminal run bringup:"
echo "   source /home/ros2_ws/install/setup.bash"
echo "   ros2 launch igvc_bringup bringup.launch.py use_sim:=true use_slam:=true use_mock_hardware:=true use_sim_time:=true"
echo ""
echo "If you did not run this with 'source start-gazebo-vnc.sh', DISPLAY is wrong."
echo "Stop and run:  source /home/ros2_ws/.devcontainer/start-gazebo-vnc.sh"
echo ""
