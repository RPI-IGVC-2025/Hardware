# Running Gazebo with UI on macOS (devcontainer)

Short reference for running the Gazebo simulation **with the 3D view** in the devcontainer on Mac.

---

## 1. Start VNC and run bringup (same terminal)

You must **source** the script (not run it) so `DISPLAY=:99` is set in your shell. Otherwise Gazebo and rtabmap run headless and the VNC window stays black.

In a single terminal **in the devcontainer**:

```bash
source /home/ros2_ws/.devcontainer/start-gazebo-vnc.sh
source /home/ros2_ws/install/setup.bash
ros2 launch igvc_bringup bringup.launch.py use_sim:=true use_slam:=true use_mock_hardware:=true use_sim_time:=true
```

Password when connecting to VNC: **vnc**

---

## 2. Connect from your Mac

- **Finder:** Cmd+K → `vnc://localhost:5900` → Connect → password: **vnc**
- Or **Screen Sharing** app → connect to **localhost** → password: **vnc**

You should see a gray/empty VNC window at first; after bringup starts, Gazebo and rtabmap windows appear there. Use the taskbar at the bottom or click a window to bring it to the front (fluxbox window manager).

Do **not** use `headless:=true`. Do **not** run bringup in a different terminal than the one where you sourced the script — that terminal would not have `DISPLAY=:99`.

---

## Headless only (no UI)

```bash
source /home/ros2_ws/install/setup.bash
# ros2 launch igvc_gazebo empty_world.launch.py headless:=true
ros2 launch igvc_bringup bringup.launch.py use_sim:=true
```

---

## If you see "odrive_can 2" or invalid package name

Duplicate " 2" files in install/build can cause this. Remove them and re-source:

```bash
find /home/ros2_ws/install /home/ros2_ws/build -name '* 2*' -exec rm -rf {} + 2>/dev/null
source /home/ros2_ws/install/setup.bash
```

Then run the launch again.

---

## If the script fails with `bash\r`

Line-ending fix (run in container):

```bash
sed -i 's/\r$//' /home/ros2_ws/.devcontainer/start-gazebo-vnc.sh
```

Then run the script again.
