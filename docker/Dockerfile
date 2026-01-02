# Base image with ROS 2 Humble
FROM ros:humble-ros-base

# Set the workspace directory
WORKDIR /home/tim/picar_ws

# Install pip and required Python libraries for S3 and Env management
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir boto3 python-dotenv

# Default command
CMD ["/bin/bash"]
