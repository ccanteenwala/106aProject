import rospy

from std_msgs.msg import Float32
from geometry_msgs.msg import Twist


# IMPORT FOR THE tfMessage
from tf.msg import tfMessage

def callback(data):


def convert():
	twist_pub = rospy.Publisher('TWIST FOR MOVE_BASE PLANNER', Twist, queuesize=10)
	
	rospy.init_node('cmdToTwist', anonymous=True)


	rate = rospy.Rate(10)

	while not rospy.is_shutdown():


		rospy.loginfo()


if __name__ == '__main__':
	try:
		convert()
	except rospy.ROSInterruptException:
		pass

