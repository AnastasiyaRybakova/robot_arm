# Robot arm (OpenManipulator)

This is the repository for the controlling the robot arm of OpenMnaipulator-X model.

The package is including the Dynamixel Workbench and self-made OpenManipulator packages.
### The  package structure:
- DynamixelSDK
- dynamixel_workbench
- dynamixel_workbench_controllers
- dynamixel-workbench-msgs
- dynamixel_workbench_operators
- dynamixel_workbench_toolbox
- open_manipualator_description
- open_manipualator_motion
- open_manipulator_move
- open_manipulator_moveit_config
- open_manipulator_simulation

To be able to succed in the building the package, you need to clone two more packages from the official repositories, which links are below:
- [dynamixel_workbench_msgs](https://github.com/ROBOTIS-GIT/dynamixel-workbench-msgs)
- [dynamixel_sdk](https://github.com/ROBOTIS-GIT/DynamixelSDK)
- in the directory /dynamixel-workbench-msgs/dynamixel_workbench_msgs/srv you need to create the JointCommand.srv, which is below:

      string unit
      uint8 id
      float32 goal_position
      ---
      bool result 

This message is used to send position command to dynamixel when we run the actual robot and testing code.

# OpenManipulator information

## Hardware
The openManipulator is based on the U2D2 converter connection between the robot and PC.
You can find here the instructions about how to make the connection with [U2D2](https://emanual.robotis.com/docs/en/parts/interface/u2d2/)

## Software
The  package structure:
- DynamixelSDK
