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

* ```roslaunch m2wr_description sim.launch``` inizialization of the agv in gazebo, the gui and the rviz visualization

from different terminal tabs you can launch the following nodes. (Attention: if it doesn't work try to source your new terminal windows, terminator is highly raccomended).

### launching other nodes
For path planning and obstacle avoidance, a pre-compile is needed.
For doing this, make this on the proper folder. <br />
	* ```chmod gu+x path_planner.py``` <br />
	* ```chmod gu+x obs_av.py``` <br />

after the robot spawn in gazebo it is possible to testing its capabilities. The simplest test is to use the manual control to move the robot inside gazebo. The easiest and most common tool for this is "teleop_twist_keyboard" provided directly by ros for each version (http://wiki.ros.org/teleop_twist_keyboard)

* ```roslaunch path_planning keyboard.launch```: keyboard control of the robot + obstacle avoidance algorithm

* ```roslaunch path_planning obs_av.launch```: rviz shows the different topic of the agv. here you can see camera captures and laser captures 

* ```roslaunch path_planning goto**.launch```<br />
	point: 	** beer<br />
		** coke<br />
		** person<br />
		** home<br />
		** hammer<br />
e.g. ```roslaunch path_planning gotobeer.launch```		
these launch files start path planning node to reach the desired destination, plus the obstacle avoidance node to avoid collisions. Nodes shutdown after the goal are reached.

* GUI:
the user interface is based on rqt_gui node.
```roslaunch m2wr_description sim.launch``` will open a new window. To set up the right configuration of rViz tool, click on "File" button and then "Open Congfig". Then source the "gui_config.rViz" in the workspace folder.

### The algorithm behind the robot motion
* "bug 0" algorithm
this algorithm is a simple way to provide path planning and obstacle avoidance to a robot.
**Preconditions :** the robot knows the position of the goal and has sensor to detect obstacles.
**Algorithm steps :**  a) the robot heads toward the goal. b) when obstacle encountered it follows the obstacle until it can head the goal again. c) go straight to the goal.
Simple maps are convenient for this kind of robot. more complex maps can foil the algorithm!


![alt text](https://github.com/arlottandrea/didactic_agv/blob/launch_files_added/bug0.jpg?raw=true)

### node interconnection:
![alt text](https://github.com/arlottandrea/didactic_agv/blob/launch_files_added/rosgraph.png?raw=true)
