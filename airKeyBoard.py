import Leap, sys, helper
from Leap import KeyTapGesture

class KeyboardListener(Leap.Listener):
	# when is this called?
	def on_init(self, controller):
		print "Init LeapMotion program"

	# when LeapMotion connects to program
	def on_connect(self, controller):
		print "Connected!"

		#config gestures
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)

	# on disconnect
	def on_disconnect(self, controller):
		print "Disconnected!"

	# on LeapMotion exit
	def on_exit(self, controller):
		print "Exited!"

	# each frame
	def on_frame(self, controller):
		#returns most recent frame
		frame = controller.frame()
		helper.printNumFingers(frame)


def startAirKeyboard():
	#create listener and controller
	listener = KeyboardListener();
	controller = Leap.Controller();

	#add listener to this LeapMotion device
	controller.add_listener(listener)	

	# Keep this process running until Enter is pressed
	print "Press Enter to quit..."
	sys.stdin.readline()

	# Remove the sample listener when done
	controller.remove_listener(listener)

startAirKeyboard()