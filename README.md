# didactic_agv
a didactic example of ros infrastructure for autonomous ground vehicles.

for this project ros melodic is required

simple start-up:

pull the repo (git clone <url>)

catkin_make 

cd didactic_agv

source devel/setup.bash

from different terminal tabs you can launch:

roslaunch m2wr_description spawn.launch: inizialization of the agv in gazebo

after the robot spawn in gazebo it is possible to testing its capabilities. The simplest test is to use the manual control to move the robot inside gazebo. The easiest and most common tool for this is "teleop_twist_keyboard" provided directly by ros for each version (http://wiki.ros.org/teleop_twist_keyboard)

roslaunch m2wr_description rviz.launch: rviz shows the different topic of the agv. here you can see camera captures and laser captures 

rosrun gazebo_ros gazebo: world simulator

rosrun teleop_twist_keyboard teleop_twist_keyboard.py: keyboard control of the robot
