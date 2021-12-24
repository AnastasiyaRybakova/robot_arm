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
### Testing the actual robot and some motions by it.

The first step I have started with was setting and testing the actual robot with the Python node, which allows us to see movement by it. 
For that you have to follow the steps below:
- Let's run the node to activate the motors of the actual robot by:
 
      $ roslaunch dynamixel_workbench_controllers position_control.launch  

- After the motors will be ready, you will not be able to move any joint by hand.
- In the terminal we can see topics by using the command line:

      $ rostopic list
- In the terminal should be main topics belong to the 

