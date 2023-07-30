import rospy, cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

bridge = CvBridge()

image = np.empty(shape=[0])

def usbcam_callback(data):
	global image
	image = bridge.imgmsg_to_cv2(data, "bgr8")

def nothing(x):
	pass
	
def start():
	global image
	rospy.init_node('Viewer')
	rospy.Subscriber("/usb_cam/image_raw/", Image, usbcam_callback)
	rospy.wait_for_message("/usb_cam/image_raw/", Image)
	print('--------- Node Initiating ---------')

	cv2.namedWindow('hsv')
	cv2.createTrackbar('H low' , 'hsv', 0, 255, nothing)
	cv2.createTrackbar('H high', 'hsv', 0, 255, nothing)
	cv2.createTrackbar('S low' , 'hsv', 0, 255, nothing)
	cv2.createTrackbar('S high', 'hsv', 0, 255, nothing)
	cv2.createTrackbar('V low' , 'hsv', 0, 255, nothing)
	cv2.createTrackbar('V high', 'hsv', 0, 255, nothing)

	while True:

		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

		if cv2.waitKey(1) & 0xFF == 27:
			break

		h_low  = cv2.getTrackbarPos('H low' , 'hsv')
		h_high = cv2.getTrackbarPos('H high', 'hsv')
		s_low  = cv2.getTrackbarPos('S low' , 'hsv')
		s_high = cv2.getTrackbarPos('S high', 'hsv')
		v_low  = cv2.getTrackbarPos('V low' , 'hsv')
		v_high = cv2.getTrackbarPos('V high', 'hsv')

		low_mask  = (h_low, s_low, v_low)
		high_mask = (h_high, s_high, v_high)

		hsv_img = cv2.inRange(hsv, low_mask, high_mask)
		cv2.imshow('hsv', hsv_img)

	cv2.destroyAllWindows()

if __name__ == "__main__":
	start()
