import rospy

from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

vel_pub = rospy.Publisher('TOPIC FOR VELOCITY INPUT TO CAR', Float32, queuesize=10)
turn_pub = rospy.Publisher('TOPIC FOR TURNING INPUT TO CAR', Float32, queuesize=10)
	
def callback(data): 
	x = data.linear.x
	# y = data.linear.y
	w = data.angular.z

	turn_pub.publish(w)
	vel_pub.publish(x)

def convert():
	
	rospy.init_node('twistToCmd', anonymous=True)
	twist_sub = rospy.Subscriber('TOPIC FROM THE MOVE_BASE', Twist, callback)

	# rate = rospy.Rate(10)

	rospy.spin();
	# while not rospy.is_shutdown():

	# 	rospy.loginfo()


if __name__ == '__main__':
	try:
		convert()
	except rospy.ROSInterruptException:
		pass

