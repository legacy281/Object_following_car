
import RPi.GPIO as gpio
gpio.setwarnings(False)

import os, time

edgetpu=0 # If Coral USB Accelerator connected, then make it '1' otherwise '0'



def init_gpio():
	gpio.setmode(gpio.BCM)
	gpio.setup(17,gpio.OUT)
	gpio.setup(22,gpio.OUT)
	gpio.setup(23,gpio.OUT)
	gpio.setup(24,gpio.OUT)
	

def back():
	print("moving back!!!!!!")
	gpio.output(17,False)
	gpio.output(22,True)
	gpio.output(23,False)
	gpio.output(24,True)
    
def right():
	gpio.output(17,True)
	gpio.output(22,False)
	gpio.output(23,False)
	gpio.output(24,True)

def left():
	gpio.output(17,False)
	gpio.output(22,True)
	gpio.output(23,True)
	gpio.output(24,False)
	
def forward():
	gpio.output(17,True)
	gpio.output(22,False)
	gpio.output(23,True)
	gpio.output(24,False)
	
def stop():
	gpio.output(17,False)
	gpio.output(22,False)
	gpio.output(23,False)
	gpio.output(24,False)

def speak_tts(text,gender):
	cmd="python /home/rasppi3/Downloads/robotics-level-4-main/earthrover/speaker/speaker_tts.py '" + text + "' " + gender + " &"
	os.system(cmd)
	
def camera_light(state):
	print(0)