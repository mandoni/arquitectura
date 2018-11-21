import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)

def CarForwards(time):
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	 
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)
	 
	sleep(time)

def CarBackwards(time):
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
	 
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)
	 
	sleep(time)

def CarLeft(time):
	#right motor forwards
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)

	#left motor backwards 
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)

	sleep(time)

def CarRight(time):
	#left motor forwards 
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)

	#right motor backwards 
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)

	sleep(time)

def CarDisplacement (x, y):
	time = 2.5
	turnTime = 0.25

	i = 0
	while i < x:
		i += 1
		print("CarForwards x = " + str(i))
		CarForwards(time)
		

	print("CarLeft")
	CarLeft(turnTime)

	i = 0
	while i < y:
		i += 1
		print("CarForwards y = " + str(i))
		CarForwards(time)
	
	#insert to database method 
	print("Database inserts")
	sleep(10)

	print("CarRight")
	CarRight(turnTime)

	i = 0
	while i < x:
		i += 1
		CarBackwards(time)
		print("CarBackwards x = " + str(i))

	print("CarLeft")
	CarLeft(turnTime)

	i = 0
	while i < y:
		i += 1
		CarBackwards(time)
		print("CarBackwards y = " + str(i))

	print("CarRight")
	CarRight(turnTime)

	#wait for another pic scan 
	print("PicScan")
	sleep(30)

CarDisplacement(2,5)