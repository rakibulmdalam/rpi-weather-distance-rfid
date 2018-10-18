import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 17 
ECHO = 18

print "Distance Measurement In Progress"

try:
	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)

	GPIO.output(TRIG, False)
	print "Waiting For Sensor To Settle"
	time.sleep(2)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	echo_state = 0
	while echo_state == 0:
		echo_state = GPIO.input(ECHO)
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
  		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 2)

	print "Distance:",distance,"cm"
finally:
	GPIO.cleanup()
