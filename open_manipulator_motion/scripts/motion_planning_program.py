#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
from std_msgs.msg import Header
import geometry_msgs.msg

print "==== starting setup"
moveit_commander.roscpp_initialize(sys.argv)                         # initializing the moveit_commander module
rospy.init_node('move_group_python_interface_test', anonymous=True)  # initializing a ROS node

robot = moveit_commander.RobotCommander()                            # RobotCommander object, an interface to robot
scene = moveit_commander.PlanningSceneInterface()                    # PlanningSceneInterface object is an interface to the world that surrounds the robot
group = moveit_commander.MoveGroupCommander("arm")                   # MoveGroupCommander object to interface manipulator group. Allows to interact with set of joints, full arm
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)   # topic of Publisher, to be able to visualize the planned motion through MoveIt Rviz

print ("hello trajectory")
pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.w = 1.0
pose_target.position.x = 0.96
pose_target.position.y = 0
pose_target.position.z = 1.18
group.set_pose_target(pose_target)

print ("hello plan")
plan1 = group.plan()    # here we are telling the arm group that we created to calculate the plan

print "============ Visualizing plan1"
display_trajectory = moveit_msgs.msg.DisplayTrajectory()

display_trajectory.trajectory_start = robot.get_current_state()
display_trajectory.trajectory.append(plan1)

display_trajectory_publisher.publish(display_trajectory)

group.execute(plan1, wait=True)
#print "============ Waiting while plan1 is visualized (again)..."
#rospy.sleep(5)

print ("hello hello")
moveit_commander.roscpp_shutdown()

