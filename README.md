# 6-DOF Manipulator Simulation

This repository contains a ROS 2 package for simulating a 6 Degree-Of-Freedom (DOF) robotic arm in Gazebo. It utilizes `ros2_control` and `gazebo_ros2_control` for realistic physics simulation and joint actuation.

## Package Overview

The workspace contains the `my_gazebo_arm` package which includes:

* **`urdf/simple_arm.urdf.xacro`**: The robot description file defining the links, joints, and transmissions for the 6-DOF arm.
* **`launch/sim.launch.py`**: The main launch file. Brings up the Gazebo simulation environment, spawns the robot, and loads the necessary controllers.
* **`launch/autonomous_task.py`**: Executes autonomous tasks with the simulated arm.
* **`config/controllers.yaml`**: The configuration file for `ros2_control`, defining the controllers such as the `joint_state_broadcaster` and `joint_trajectory_controller`.

## Prerequisites

Ensure you have the following installed to run this simulation:
* ROS 2 (e.g., Humble, Iron, or Jazzy)
* Gazebo (Classic or modern depending on your setup)
* `ros2-control` and `gazebo-ros2-control`
* `ros-dev-tools`
* Additional ROS 2 dependencies: `xacro`, `joint_state_publisher`

## Building the Workspace

Navigate to the root of the workspace and build using `colcon`:

```bash
cd ~/gazebo_arm_ws
colcon build
source install/setup.bash
```

## Running the Simulation

To launch the main Gazebo simulation with the 6-DOF arm:

```bash
ros2 launch my_gazebo_arm sim.launch.py
```

To run the autonomous task script:

```bash
ros2 launch my_gazebo_arm autonomous_task.py
# Or if it's a direct python node:
ros2 run my_gazebo_arm autonomous_task.py
```
