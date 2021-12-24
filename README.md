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

To be able to succeed in the building the package, you need to clone two more packages from the official repositories, which links are below:
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
- In the terminal should be main topics belong to the controlling function of the robot:

      /dynamixel_state
      /goal_dynamixel_position
      /joint_states
      /rosout
      /rosout_agg
 
- By the line command below it's possible to check the each joint position:

      $ rostopic echo /joint_states -n1
      
It is possible to see in the terminal the data like that way:

      header: 
            seq: 3994
            stamp: 
                  secs: 1640324659
                  nsecs: 518055098
            frame_id: ''
      name: [id_11, id_12, id_13, id_14, id_15]
      position: [-0.0015339808305725455, -0.27458256483078003, 0.7439807057380676, 1.087592363357544, 0.42644667625427246]
      velocity: [0.0, 0.0, 0.0, 0.0, 0.0]
      effort: []
      ---
In the terminal represented name of joints and their positions respectively. Furthermore, it is possible to check the joints' positions after chacnging the actual robot state to be able to apply to the python code those parameters.

- The next step after applying postion parameters to the Python node we can test it directly. For that follow steps below:

            $ cd ~/catkin_ws
            $ source devel/setup.bash
            $ rospack profile
            $ roslaunch dynamixel_workbench_controllers position_control.launch 
In the new terminal:

            $ cd src/openmanipulator_move/scripts
            $ rosrun openmanipulator_move move_openmanipulator.py
             
#### The result of running the code:
![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/37059842/114139017-6fa9e680-9949-11eb-9ad4-70b69129e2e2.gif)     

# Simulation Gazebo + Rviz

Before moving to the actual robot for the trajectory planning task testing, it is important to test how the different trajectories are planning and executing in the Simulation. For that need to run the command line below:
