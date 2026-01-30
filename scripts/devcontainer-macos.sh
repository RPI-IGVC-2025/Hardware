#!/bin/bash
# macOS Dev Container Launcher
# This script starts the dev container using the macOS-specific configuration
# without modifying the default devcontainer.json (which is for Linux/WSL)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
DOCKERFILE="$PROJECT_ROOT/.devcontainer/Dockerfile"
CONTAINER_NAME="ros2-igvc-dev"
IMAGE_NAME="ros2-igvc-macos"

echo "Starting macOS dev container..."
echo "Project root: $PROJECT_ROOT"

# Check if container already exists
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    echo ""
    echo "Container '$CONTAINER_NAME' already exists."
    
    # Check if it's running
    if docker ps --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
        echo "Container is already running!"
        echo ""
        echo "To attach Cursor/VS Code:"
        echo "  Cmd+Shift+P → 'Dev Containers: Attach to Running Container'"
        echo "  Select '$CONTAINER_NAME'"
        echo ""
        echo "To open a shell directly:"
        echo "  docker exec -it $CONTAINER_NAME bash"
        echo ""
        echo "To stop and remove the container, run:"
        echo "  docker stop $CONTAINER_NAME && docker rm $CONTAINER_NAME"
        exit 0
    else
        echo "Container exists but is stopped. Removing it..."
        docker rm "$CONTAINER_NAME"
    fi
fi

# Build the image
echo ""
echo "Building Docker image..."
docker build \
    -t "$IMAGE_NAME" \
    -f "$DOCKERFILE" \
    --build-arg USERNAME=ros_user \
    "$PROJECT_ROOT/.devcontainer"

# Run the container
echo ""
echo "Starting container..."
docker run -d \
    --name "$CONTAINER_NAME" \
    --privileged \
    -e DISPLAY=host.docker.internal:0 \
    -e ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST \
    -e ROS_DOMAIN_ID=42 \
    -e ROS_LOCALHOST_ONLY=1 \
    -v "$PROJECT_ROOT:/home/ros2_ws" \
    -w /home/ros2_ws \
    "$IMAGE_NAME" \
    sleep infinity

# Run setup inside container
echo ""
echo "Running initial setup inside container..."
docker exec "$CONTAINER_NAME" bash -c '
    # Add ROS 2 sourcing to bashrc
    echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
    
    # Source ROS 2 for current commands
    source /opt/ros/jazzy/setup.bash
    
    # Run the setup script (clones libs)
    cd /home/ros2_ws
    if [ -f .devcontainer/setup.sh ]; then
        echo "Running setup.sh..."
        bash .devcontainer/setup.sh
    fi
    
    echo "Setup complete!"
'

echo ""
echo "============================================"
echo "Container '$CONTAINER_NAME' is running!"
echo "============================================"
echo ""
echo "To attach Cursor/VS Code:"
echo "  Cmd+Shift+P → 'Dev Containers: Attach to Running Container'"
echo "  Select '$CONTAINER_NAME'"
echo ""
echo "To open a shell directly:"
echo "  docker exec -it $CONTAINER_NAME bash"
echo ""
echo "To stop the container:"
echo "  docker stop $CONTAINER_NAME && docker rm $CONTAINER_NAME"
echo ""
echo "NOTE: ROS 2 is automatically sourced in new terminals."
