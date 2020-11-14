#! /usr/bin/env python
import rospy
import math
import argparse
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Point, Twist
from nav_msgs.msg import Odometry
from tf import transformations

class path():
    
    def __init__(self):
        parser = argparse.ArgumentParser()
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.odom = rospy.Subscriber('/odom', Odometry, self.clbk_odom)
        parser.add_argument("point")
        args = parser.parse_args()
        if args.point == 'beer':
            goal_point = Point(5, 5, 0)
        elif args.point == 'hammer':
            goal_point = Point(5, 0, 0)
        elif args.point == 'coke':
            goal_point = Point(0, 3, 0)
        elif args.point == 'man':
            goal_point = Point(2, 7, 0)
        elif args.point == 'home':
            goal_point = Point(0, 0, 0)
        else:
            goal_point = Point(-1, -1, 0)
        self.goal = goal_point
        self.yaw_ = 0.01
        self.err_pos = 0.01
        self.delta_yaw = 0.2
        self.Yaw_Precision_ = 0.19
        self.Dist_Precision_ = 0.20
        self.twist = Twist()
        self.state = 0
    
    def clearmsg(self):
        self.twist.linear.x = 0
        self.twist.angular.z = 0
    
    def goahead(self):
        if self.Dist_Precision_ < self.err_pos :
            self.twist.linear.x = 0.5
            self.pub.publish(self.twist)	
            self.clearmsg()
            if self.Yaw_Precision_ < math.fabs(self.delta_yaw):
                self.state = 0

        else:
         self.state = 2
    
    def fixheading(self):
        if self.Yaw_Precision_ < math.fabs(self.delta_yaw):
            if 0 > self.delta_yaw :
                self.twist.angular.z = 0.3 
            else: 
                self.twist.angular.z = -0.3
            self.pub.publish(self.twist)
            self.clearmsg()			
        else:
            self.state = 1
             #change state
    
    def done(self):
        self.twist.linear.x = 0
        self.twist.angular.z = 0
        self.pub.publish(self.twist)
        rospy.loginfo('done!')
    
    #callback
    def clbk_odom(self, msg):
        pos_ = msg.pose.pose.position
        or_ = msg.pose.pose.orientation
        quaternion = (
        or_.x,
        or_.y,
        or_.z,
        or_.w)
        euler = transformations.euler_from_quaternion(quaternion)
        self.yaw_ = euler[2]
        self.delta_yaw = math.atan2(self.goal.y - pos_.y, self.goal.x - pos_.x) - self.yaw_
        self.err_pos = math.sqrt(pow(pos_.y - self.goal.y, 2) + pow(pos_.x - self.goal.x, 2))
        rospy.loginfo(self.delta_yaw)
        rospy.logerr(self.err_pos)
        if self.state == 0:
            rospy.loginfo('heading!')
            self.fixheading()
        elif self.state == 1:
            rospy.loginfo('straight!')
            self.goahead()
        elif self.state == 2:
            rospy.loginfo('done!')
            self.done()
            pass
        else:
            rospy.logerr('Unknown state!')
            pass

def main():
    rospy.init_node('go_to_point')
    planner = path()
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        rate.sleep()
        rospy.loginfo(planner.state)

if __name__ == '__main__':
    main()
