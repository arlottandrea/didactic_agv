# didactic_agv by Arlotta A. and Gandolfi F.
## a didactic example of ros infrastructure for autonomous ground vehicles.

*for this project ros melodic is required*

The Aim of this project is to develop a ros infrastructure for an autonomous ground vehicle, for didactic use. 
For this reason the nodes doesn't require external plugin or third-party app. The work tarted from a blank installation of Ubuntu 18, a new build of ROS Melodic, and the basic installation like git or python.

### simple start-up:

* pull the repo (```git clone <url>```)

* ```catkin_make```

* ```cd didactic_agv```

* ```source devel/setup.bash```

* ```roslaunch m2wr_description spawn.launch``` inizialization of the agv in gazebo

from different terminal tabs you can launch the following nodes. (Attention: if it doesn't work try to source your new terminal windows, terminator is highly raccomended).

### launching other nodes
For path planning and obstacle avoidance, a pre-compile is needed.
For doing this, make this on the proper folder. <br />
	* ```chmod gu+x path_planner.py``` <br />
	* ```chmod gu+x obs_av.py``` <br />

after the robot spawn in gazebo it is possible to testing its capabilities. The simplest test is to use the manual control to move the robot inside gazebo. The easiest and most common tool for this is "teleop_twist_keyboard" provided directly by ros for each version (http://wiki.ros.org/teleop_twist_keyboard)

* ```rosrun teleop_twist_keyboard teleop_twist_keyboard.py```: keyboard control of the robot

* ```roslaunch m2wr_description rviz.launch```: rviz shows the different topic of the agv. here you can see camera captures and laser captures 

* ```rosrun gazebo_ros gazebo```: world simulator

here open the world avaible in the folder "world".
/scrivere come afre ad aprire il mondo

* ```rosrun path_planning path_planner.py --point``` <br />
--point: 	** beer<br />
		** coke<br />
		** person<br />
		** home<br />
		** hammer<br />
e.g. ```rosrun path_planning path_planner.py beer ```		

* ```rosrun path_planning obs_av.py```

* GUI:
from a sourced terminal run: ```rqt -p didactic_agv_GUI.perspective ```
this will open a new gui. to set up the right configuration of rViz tool, click on "File" button and then "Open Congfig". Then source the "gui_config.rViz" in the workspace folder.



