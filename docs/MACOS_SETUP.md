# macOS Development Setup Guide

This guide walks through setting up the ROS 2 development container on macOS.

> **Note**: This devcontainer was originally designed for Linux/WSL. Some features (hardware access, multi-machine ROS networking, GPU acceleration) will not work on macOS.

---

## Prerequisites

- macOS 10.15 (Catalina) or later
- [Homebrew](https://brew.sh/) installed
- Ability to run `sudo` commands (your user must be an Administrator)

---

## Step 1: Install Docker Desktop ✅

Docker Desktop provides the container runtime on macOS.

```bash
brew install --cask docker
```

If you see `Error: It seems there is already an App at '/Applications/Docker.app'`, Docker is already installed.

**After installation:**
1. Open Docker Desktop from Applications
2. Complete the initial setup wizard
3. Ensure Docker is running (whale icon in menu bar)

---

## Step 2: Install XQuartz (for GUI applications) ✅

XQuartz provides X11 display server for GUI apps like `rviz2` and `rqt`.

```bash
brew install --cask xquartz
```

**⚠️ IMPORTANT: You must log out and log back in after installing XQuartz.**

### Configure XQuartz

After logging back in:

1. Open **XQuartz** (from Applications → Utilities)
2. Go to **XQuartz → Preferences** (or `Cmd + ,`)
3. Click the **Security** tab
4. ✅ Check **"Allow connections from network clients"**
5. Close Preferences and **restart XQuartz**

### Enable X11 forwarding

> **⚠️ IMPORTANT:** Run this command in the **XQuartz terminal** or a **macOS terminal** — NOT in VS Code/Cursor's integrated terminal.

1. Open XQuartz
2. Go to **Applications → Terminal** in the XQuartz menu bar (or use a regular macOS Terminal)
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

## Step 3: Fix Homebrew Permissions (if needed)

If you saw permission errors during installation, fix them:

```bash
sudo chown -R $(whoami) /usr/local/bin /usr/local/include /usr/local/lib /usr/local/lib/pkgconfig
chmod u+w /usr/local/bin /usr/local/include /usr/local/lib /usr/local/lib/pkgconfig
```

---

## Step 4: Configure Docker CLI and Install Extensions

### Add Docker to PATH

After a fresh macOS install or if `docker` command isn't found, add Docker to your PATH:

```bash
echo 'export PATH="$PATH:/Applications/Docker.app/Contents/Resources/bin"' >> ~/.zshrc
echo 'export PATH="$PATH:/Applications/Docker.app/Contents/Resources/bin"' >> ~/.bash_profile
source ~/.zshrc  # or restart your terminal
```

Verify it works:
```bash
which docker
# Should output: /Applications/Docker.app/Contents/Resources/bin/docker
```

### Install Dev Containers Extension

Install manually in Cursor:
1. Open Extensions (`Cmd + Shift + X`)
2. Search for "Dev Containers"
3. Install **Dev Containers** (by Anysphere/Cursor or Microsoft)

---

## Step 5: Understand the Devcontainer Setup

This repository has multiple devcontainer configurations to support different platforms:

```
.devcontainer/
├── devcontainer.json    # Linux/WSL (default - DO NOT MODIFY)
├── Dockerfile           # Shared Dockerfile
├── setup.sh             # Shared setup script
└── macos/
    └── devcontainer.json    # macOS-specific config
```

**Important:** The main `devcontainer.json` is configured for Linux/WSL users. macOS users should use the script in the next step instead of modifying this file.

---

## Step 6: Build and Open the Container

macOS users should use the provided script to launch the container with the correct configuration.

### Run the macOS launch script

```bash
cd RobotCode2026
./scripts/devcontainer-macos.sh
```

This script:
- Builds the Docker image using the macOS-compatible settings
- Starts a container named `ros2-igvc-dev`
- Mounts your workspace at `/home/ros2_ws`
- **Automatically sources ROS 2** in `.bashrc`
- **Runs `setup.sh`** to clone required libraries (odrive, imu)
- Handles existing containers gracefully (won't fail if already running)
- Doesn't modify any files that would affect Linux/WSL users
- **Does NOT require npm/Node.js** — uses Docker directly

The first build will take **5-15 minutes** as it:
- Downloads the `ros:jazzy` base image
- Installs ROS 2 packages and dependencies

### Attach Cursor to the Container

After the container starts:
1. `Cmd + Shift + P`
2. Type: **"Dev Containers: Attach to Running Container"**
3. Select **`ros2-igvc-dev`**

A new Cursor window will open connected to the container.

---

## Step 7: Verify the Setup

The launch script automatically:
- Sources ROS 2 in `.bashrc` (no manual setup needed)
- Runs `setup.sh` to clone required libraries

### Verify ROS 2 is working

Open a new terminal in the container and run:

```bash
# Check ROS 2 help
ros2 --help

# List installed packages
ros2 pkg list | head

# Test GUI (requires XQuartz running on macOS)
rviz2
```

> **Note:** You're logged in as `root` in the container. This is fine for development.

### If ROS 2 commands aren't found

If you're in an existing terminal session that was opened before setup completed:

```bash
source ~/.bashrc
# or just open a new terminal
```

---

## Troubleshooting

### `docker: command not found`

Docker CLI isn't in your PATH. Fix it:

```bash
echo 'export PATH="$PATH:/Applications/Docker.app/Contents/Resources/bin"' >> ~/.zshrc
echo 'export PATH="$PATH:/Applications/Docker.app/Contents/Resources/bin"' >> ~/.bash_profile
```

Then **restart Cursor completely** (`Cmd + Q`, reopen).

### `ros2: command not found` (inside container)

ROS 2 isn't sourced. Run inside the container:

```bash
source /opt/ros/jazzy/setup.bash
```

To make permanent:
```bash
echo 'source /opt/ros/jazzy/setup.bash' >> ~/.bashrc
```

### GUI apps don't open / Display errors

1. Make sure XQuartz is running
2. Run `xhost +localhost` in a **macOS terminal** (not inside the container, not in Cursor)
3. Verify DISPLAY is set inside container: `echo $DISPLAY`
   - Should show `host.docker.internal:0`

### Container build fails

- Ensure Docker Desktop is running
- Check Docker has enough resources:
  - Docker Desktop → Settings → Resources
  - Recommend: 4+ CPUs, 8+ GB RAM

### "No matching distribution" or package errors

The ROS Jazzy packages may have architecture issues on Apple Silicon. Try:
```bash
# In devcontainer.json, add to build args:
"platform": "linux/amd64"
```

### Permission denied errors inside container

```bash
sudo chown -R $(whoami) /home/ros2_ws/
```

### Container already exists error

If you see "container name already in use":

```bash
docker stop ros2-igvc-dev && docker rm ros2-igvc-dev
./scripts/devcontainer-macos.sh
```

---

## macOS Limitations

| Feature | Status | Notes |
|---------|--------|-------|
| Code editing & building | ✅ Works | Full functionality |
| ROS 2 nodes (localhost) | ✅ Works | Single-machine only |
| GUI apps (rviz2, rqt) | ⚠️ Partial | Requires XQuartz setup |
| Multi-machine ROS networking | ❌ Broken | `--net=host` doesn't work on Mac |
| USB/Serial hardware access | ⚠️ Limited | Requires Docker Desktop USB config |
| GPU acceleration | ❌ None | No `/dev/dri` on Mac |

---

## Quick Reference

### Start XQuartz and enable forwarding (run in macOS terminal, not Cursor)
```bash
open -a XQuartz && sleep 2 && xhost +localhost
```

### Start macOS container
```bash
cd RobotCode2026
./scripts/devcontainer-macos.sh
```

### Attach to running container
```
Cmd + Shift + P → "Dev Containers: Attach to Running Container" → select "ros2-igvc-dev"
```

### Open shell in container (alternative to attaching Cursor)
```bash
docker exec -it ros2-igvc-dev bash
```

### Stop the container
```bash
docker stop ros2-igvc-dev && docker rm ros2-igvc-dev
```

### Rebuild container from scratch
```bash
docker stop ros2-igvc-dev && docker rm ros2-igvc-dev
docker rmi ros2-igvc-macos
./scripts/devcontainer-macos.sh
```

---

## Next Steps

After setup is complete:
1. Read the main [README.md](../README.md)
2. Check [Hardware docs](../src/Hardware/docs/install.md)
3. Try building a package: `colcon build --packages-select hardware`

---

*Last updated: January 2026*
