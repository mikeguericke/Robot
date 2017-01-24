import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

enableleft = 02
enableright = 14
in_left_1 = 03
in_left_2 = 04
in_right_1 = 15
in_right_2 = 17
pwm_left = 500
pwm_right = 500

GPIO.setup(enableleft, GPIO.OUT)
GPIO.setup(enableright, GPIO.OUT)
GPIO.setup(in_left_1, GPIO.OUT)
GPIO.setup(in_left_2, GPIO.OUT)
GPIO.setup(in_right_1, GPIO.OUT)
GPIO.setup(in_right_2, GPIO.OUT)

# set up motors and look here to alter
motor_pwm_left = GPIO.PWM(enableleft, pwm_left)
motor_pwm_right = GPIO.PWM(enableright, pwm_right)
motor_pwm_left.start(0)
motor_pwm_right.start(0)

def forward(duty):
	GPIO.output(in_left_1, True)
	GPIO.output(in_right_1, True)
	GPIO.output(in_left_2, False)
	GPIO.output(in_right_2, False)
	motor_pwm_left.ChangeDutyCycle(duty)
	motor_pwm_right.ChangeDutyCycle(duty)

def reverse(duty):
	GPIO.output(in_left_1, False)
	GPIO.output(in_right_1, False)
	GPIO.output(in_left_2, True)
	GPIO.output(in_right_2, True)
	motor_pwm_left.ChangeDutyCycle(duty)
	motor_pwm_right.ChangeDutyCycle(duty)

def stop():
	GPIO.output(in_left_1, False)
	GPIO.output(in_left_2, False)
	GPIO.output(in_right_1, False)
	GPIO.output(in_right_2, False)

try:
	while True:
		direction = raw_input('Enter direction letter (f - forward, r - reverse, s - stop, x - exit): ')
		if direction[0] == 's':
			stop()
		elif direction[0] =='x':
			stop()
			break
		else:
			duty = input('Enter Duty Cycle (0 to 100): ')
			if direction[0] == 'f':
				forward(duty)
			elif direction[0] == 'r':
				reverse(duty)
finally:
	print("Cleaning up")
	GPIO.cleanup()
