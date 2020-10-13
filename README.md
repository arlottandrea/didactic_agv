# didactic_agv
a didactic example of ros infrastructure for autonomous ground vehicles.

for this project ros melodic is required

simple start-up:
pull the repo
catkin_make inside simulation_ws folder
source simulation_ws/devel/setup

from different terminal tabs you can launch:

roslaunch m2wr_description spawn.launch : inizialization of the agv in gazebo

roslaunch m2wr_description rviz.launch : rviz shows the different topic of the agv. here you can see camera captures and laser captures 

rosrun gazebo_ros gazebo : world simulator

rosrun teleop_twist_keyboard teleop_twist_keyboard.py : keyboard control of the robot
