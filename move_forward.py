import rospy
from gazebo_msgs.srv import ApplyJointEffort, ApplyJointEffortRequest # Import the service message used by the service /gazebo/delete_model
import sys 

forwards = 1.0
backwards = -1.0

#front
front_leftControl = rospy.ServiceProxy('/gazebo/apply_joint_effort', ApplyJointEffort)
front_rightControl = rospy.ServiceProxy('/gazebo/apply_joint_effort', ApplyJointEffort)

aje_front_right = ApplyJointEffortRequest()
aje_front_left = ApplyJointEffortRequest()

aje_front_left.joint_name = 'front_left_wheel_hinge'
aje_front_right.joint_name = 'front_right_wheel_hinge'

#rear

rear_leftControl = rospy.ServiceProxy('/gazebo/apply_joint_effort', ApplyJointEffort)
rear_rightControl = rospy.ServiceProxy('/gazebo/apply_joint_effort', ApplyJointEffort)

aje_rear_right = ApplyJointEffortRequest()
aje_rear_left = ApplyJointEffortRequest()

aje_rear_left.joint_name = 'rear_left_wheel_hinge'
aje_rear_right.joint_name = 'rear_right_wheel_hinge'


while(True):
    val = raw_input("Input W/A/S/D: ")
    print(val)

    if (val == "w"):
        #front
        aje_front_right.effort = forwards
        aje_front_right.duration.secs = 1.0
        aje_front_left.effort = forwards
        aje_front_left.duration.secs = 1.0
        front_rightControl(aje_front_right)
        front_leftControl(aje_front_left)

        #rear
        aje_rear_right.effort = forwards
        aje_rear_right.duration.secs = 1.0
        aje_rear_left.effort = forwards
        aje_rear_left.duration.secs = 1.0
        rear_rightControl(aje_rear_right)
        rear_leftControl(aje_rear_left)

    elif (val == "s"):
        #front
        aje_front_right.effort = backwards
        aje_front_right.duration.secs = 1.0
        aje_front_left.effort = backwards
        aje_front_left.duration.secs = 1.0
        front_rightControl(aje_front_right)
        front_leftControl(aje_front_left)

    elif (val == "d"): #turn right

        aje_front_left.effort = forwards
        aje_front_left.duration.secs = 1.0
        aje_rear_right.effort = backwards
        aje_rear_right.duration.secs = 1.0
        rear_rightControl(aje_rear_right)
        front_leftControl(aje_front_left)
        

        aje_rear_left.effort = forwards
        aje_rear_left.duration.secs = 1.0
        aje_front_right.effort = backwards
        aje_front_right.duration.secs = 1.0
        rear_rightControl(aje_front_right)
        front_leftControl(aje_rear_left)

    elif (val == "a"):
        aje_right.effort = forwards
        aje_right.duration.secs = 1.0
        aje_left.effort = backwards
        aje_left.duration.secs = 1.0
        rightControl(aje_right)
        leftControl(aje_left)
    else:
        pass
    
