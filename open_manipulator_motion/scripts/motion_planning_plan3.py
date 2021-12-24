#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

def trajectory():
	waypoints = []
	waypoints.append(start)
	for i in range(0,res):
		point = copy.deepcopy(start)
		point = geometry_msgs.msg.Pose()
		point.position.x = 0.66
		point.position.y = 0
		point.position.z = 1.1
		waypoints.append(copy.deepcopy(point))
	waypoints.append(start)
	return waypoints
		

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_test3', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
arm_group = moveit_commander.MoveGroupCommander("arm")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)


#plan = arm_group.retime_trajectory(robot.get_current_state(), plan, .05)  # (0.02) time scaling factor
plan1 = arm_group.plan()

path_points = point( 100, arm_group.get_current_pose().pose)

display_trajectory = moveit_msgs.msg.DisplayTrajectory()
display_trajectory.trajectory_start = robot.get_current_state()
display_trajectory.trajectory.append(plan)
# Publish
display_trajectory_publisher.publish(display_trajectory);

arm_group.execute(plan, wait=True)
# Excutes trajectory

moveit_commander.roscpp_shutdown()
