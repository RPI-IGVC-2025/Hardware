# Installation

1. Follow the [IGVC Docker Setup Guide](https://docs.google.com/document/d/1-VyvY_TrujEbJ-1xbitBwOAzUDWoNYXUCovK7mJRQQ4/edit?usp=sharing) to get Docker installed on your host machine.
    - Follow the [Docker post-installation guide](https://docs.docker.com/engine/install/linux-postinstall/) If you have issues running docker commands

2. Run `git clone https://github.com/RPI-IGVC-2025/RobotCode2026.git` within your WSL or native linux filesystem.

3. `cd` to the RobotCode2026 directory

4. Open the resulting repository in Visual Studio Code (Using `code .`)
    - Make sure to install the [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack).

5. Make sure your host docker engine (In the majority of cases, Docker Desktop) is running.

6. Use `Ctrl+Shift+P` to open the command pallete and run `Dev containers: Rebuild and Reopen in Container`
    - While within the devcontainer, the command will be `Dev containrs: Reopen in Container`

7. Verify ROS 2 is working

Open a new terminal in the container and run:

```bash
# Check ROS 2 help
ros2 --help

# List installed packages
ros2 pkg list | head

# Test GUI (requires XQuartz running on macOS)
rqt
```

You're ready to develop!