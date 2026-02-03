# macOS Development Setup Guide

This guide walks through setting up the ROS 2 development container on macOS.

> **Note**: This devcontainer was originally designed for a Linux environment. Some features (hardware access, multi-machine ROS networking, GPU acceleration) will not work on macOS.

---

## Prerequisites

- macOS 10.15 (Catalina) or later
- [Homebrew](https://brew.sh/) installed
- Ability to run `sudo` commands (your user must be an Administrator)

---

## Step 1: Install XQuartz (for GUI applications)

XQuartz provides X11 display server for GUI apps like `rviz2` and `rqt`.

> **Skip this step** if you don't need GUI apps (rviz2, rqt, Gazebo).

```bash
brew install --cask xquartz
```

### Configure XQuartz

After installation:

1. Open **XQuartz** (from Applications → Utilities)
2. Go to **XQuartz → Preferences** (or `Cmd + ,`)
3. Click the **Security** tab
4. Check **"Allow connections from network clients"**
5. Close Preferences and **restart XQuartz**

### Enable X11 forwarding

> **IMPORTANT:** Run this command in the **XQuartz terminal** or a **macOS Terminal.app** — NOT in VS Code's integrated terminal.

1. Open XQuartz
2. Go to **Applications → Terminal** in the XQuartz menu bar (or use Terminal.app)
3. Run:

```bash
xhost +localhost
```

You'll need to run this each time you restart XQuartz.

To make this permanent, add it to your shell profile:

```bash
echo 'xhost +localhost 2>/dev/null' >> ~/.zshrc
```

---

## Step 2: Fix Homebrew Permissions (if needed)

If you saw permission errors during installation, fix them:

```bash
sudo chown -R $(whoami) /usr/local/bin /usr/local/include /usr/local/lib /usr/local/lib/pkgconfig
chmod u+w /usr/local/bin /usr/local/include /usr/local/lib /usr/local/lib/pkgconfig
```

---

## Step 3: Configure Docker CLI

Follow the main Install.md starting from step 2

---

## Step 4: Setup ROS 2 Environment

Once inside the container, ROS 2 commands require sourcing the setup file.

### Source ROS 2 (required each new terminal)

```bash
source /opt/ros/jazzy/setup.bash
```

### Make it permanent

Run this once to automatically source ROS 2 in every new terminal:

```bash
echo 'source /opt/ros/jazzy/setup.bash' >> ~/.bashrc
```

### Verify ROS 2 is working

```bash
# Check ROS 2 help
ros2 --help

# List installed packages
ros2 pkg list | head

# Test GUI (requires XQuartz running on macOS)
rviz2
```


---

## Troubleshooting

### GUI apps don't open / Display errors

1. Make sure XQuartz is running: `open -a XQuartz`
2. Run `xhost +localhost` in **XQuartz terminal or Terminal.app** (not in VS Code)
3. Verify DISPLAY is set inside container: `echo $DISPLAY`
   - Should show `host.docker.internal:0`

### No config picker appears

If VS Code doesn't show a picker with multiple configs:
- Make sure you opened the `RobotCode2026` folder (not a parent or subfolder)
- Try: `Cmd + Shift + P` → "Dev Containers: Rebuild and Reopen in Container"

---

## Quick Reference

### Start XQuartz and enable forwarding (run in Terminal.app, not VS Code)
```bash
open -a XQuartz && sleep 2 && xhost +localhost
```

### Reopen in container
```
Cmd + Shift + P → "Dev Containers: Reopen in Container" → select macOS config
```

### Rebuild container from scratch
```
Cmd + Shift + P → "Dev Containers: Rebuild Container Without Cache"
```


*Last updated: January 2026*
