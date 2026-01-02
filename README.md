# Picar Edge Node

## 🚀 Overview
This repository serves as the **Edge Collection Node** for the **Edge-to-Cloud Robotics** architecture. It is responsible for recording ROS 2 data (MCAP/Bag) on the Raspberry Pi 4B and pushing it to the central station for further processing.

## 🔗 Infrastructure Links
- **Central Station IP**: `192.168.0.190` (Lenovo ThinkStation P620)
- **Storage Target**: MinIO Bucket `edge-to-cloud-robotics-landing-s3`
- **Parent Project**: [edge-to-cloud-robotics-ml-infra](https://github.com/5i5j/edge-to-cloud-robotics-picar)

## 🏗️ Hardware Architecture
- **Host**: Raspberry Pi 4B (8GB RAM)
- **Storage**: 1TB NVMe SSD (Mounted at `/mnt/robot_storage`)
- **OS**: Ubuntu 22.04 LTS

## 🛠️ Quick Start
1. Ensure the NVMe drive is correctly mounted.
2. Clone this repo into `~/picar_ws`.
3. Start the ROS 2 Humble environment:
   ```bash
   docker compose up -d
