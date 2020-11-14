# didactic_agv
a didactic example of ros infrastructure for autonomous ground vehicles.

for this project ros melodic is required

simple start-up:

pull the repo (git clone <url>)

catkin_make 

cd didactic_agv

source devel/setup.bash

roslaunch m2wr_description spawn.launch: inizialization of the agv in gazebo

from different terminal tabs you can launch the following nodes. (Attention: if it doesn't work try to source your new terminal windows, terminator is highly raccomended).
For path planning and obstacle avoidance, a pre compile is needed.
For doing this, make this on the proper folder.
chmod gu+x path_planner.py
chmod gu+x obs_av.py

after the robot spawn in gazebo it is possible to testing its capabilities. The simplest test is to use the manual control to move the robot inside gazebo. The easiest and most common tool for this is "teleop_twist_keyboard" provided directly by ros for each version (http://wiki.ros.org/teleop_twist_keyboard)

roslaunch m2wr_description rviz.launch: rviz shows the different topic of the agv. here you can see camera captures and laser captures 

rosrun gazebo_ros gazebo: world simulator
here open the world avaible in the folder "world".
/scrivere come

rosrun teleop_twist_keyboard teleop_twist_keyboard.py: keyboard control of the robot

rosrun path_planning path_planner.py --point
--point: 	- beer
		- coke
		- person
		- home
		- hammer
e.g. rosrun path_planning path_planner.py beer 		

rosrun path_planning obs_av.py


