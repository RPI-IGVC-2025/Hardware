# Running Gazebo with UI on macOS (devcontainer)

Short reference for running the Gazebo simulation **with the 3D view** in the devcontainer on Mac.

---

## 1. Start VNC (once per container session)

In a terminal **in the devcontainer**:

```bash
/home/ros2_ws/.devcontainer/start-gazebo-vnc.sh
```

Password when prompted: **vnc**

---

## 2. Connect from your Mac

- **Finder:** Cmd+K → `vnc://localhost:5900` → Connect → password: **vnc**
- Or **Screen Sharing** app → connect to **localhost** → password: **vnc**

You should see a gray/empty VNC window.

---

## 3. Run bringup in the container (Gazebo + rtabmap)

In a **second** terminal in the devcontainer:

```bash
source /home/ros2_ws/install/setup.bash
ros2 launch igvc_bringup bringup.launch.py use_sim:=true
```

Do **not** use `headless:=true`. Both the Gazebo and rtabmap windows appear in the VNC window. Use the taskbar at the bottom or click a window to bring it to the front (fluxbox window manager).

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
