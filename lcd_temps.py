#!/usr/bin/python

# datasheet at http://adafruit.com/datasheets/HD44780.pdf
# suggests degree symbol is B0

import RPi.GPIO as GPIO
import time
import urllib2
import sys
from subprocess import call

# http://www.raspberrypi-spy.co.uk/2012/07/16x2-lcd-module-control-using-python/
from message2 import *

GPIO.setwarnings(False)

LCD_RS = 25
LCD_E  = 24
LCD_D4 = 23
LCD_D5 = 17
# 21/27 is rev1/rev2 board
#LCD_D6 = 21
LCD_D6 = 27
LCD_D7 = 22

GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
GPIO.setup(LCD_E, GPIO.OUT)  # E
GPIO.setup(LCD_RS, GPIO.OUT) # RS
GPIO.setup(LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD_D7, GPIO.OUT) # DB7

# Initialise display
lcd_init()

import re

# 28-0000043e37d7 white
# 28-00000457d048 black
# 28-0000048be4e7 ambient

sensors = {'white': '28-0000043e37d7',
	'black': '28-00000457d048',
	'ambient': '28-0000048be4e7'}

def read_sensor(sensor):
	tries = 0
	while True:
		tries = tries + 1
		if tries == 5:
			print "error"
			break
		f = open("/sys/bus/w1/devices/" + sensor + "/w1_slave")
		first = f.readline()
		second = f.readline()
		f.close()
		if not(re.search("crc=.. YES", first)): continue
		temp = re.sub(".*t=", "", second)
		temp = float(temp) / 1000
		return temp
		break

def network_on():
    try:
        response=urllib2.urlopen('http://192.168.1.13',timeout=1)
        return True
    except:
        print "network problem?", sys.exc_info()[0]
        return False

#########    except urllib2.URLError as err: pass

#for n,d in sensors.iteritems():
#	print n, read_sensor(d)
	
#for sensor in ['28-0000043e37d7', '28-00000457d048', '28-0000048be4e7']:
#	print sensor, read_sensor(sensor)




#lcd_byte(LCD_LINE_1, LCD_CMD)
#lcd_byte(0xB0, LCD_CHR)

# # Send some test
# lcd_byte(LCD_LINE_1, LCD_CMD)
# lcd_string("Hello")
# lcd_byte(LCD_LINE_2, LCD_CMD)
# lcd_string("World")
# 
# time.sleep(3) # 3 second delay



while True:
	output=("%s %3.1f%s" % ("ambient", read_sensor('28-0000048be4e7'), chr(0xb0) + "C"),
		"%s %3.1f%s" % ("basking", read_sensor('28-0000043e37d7'), chr(0xb0) + "C"),
		"%s %3.1f%s" % ("in hide", read_sensor('28-00000457d048'), chr(0xb0) + "C"),
		)
	t=time.strftime("%H:%M", time.localtime())
	gotnet = network_on()
	if(not gotnet):
		t += " (no net)"
	for s in output:
		lcd_init()
		#print s
		time.sleep(0.1)
		lcd_string(s)
		lcd_byte(LCD_LINE_2, LCD_CMD)
		lcd_string(t)
		time.sleep(10)
#	if(not gotnet):
#		call("/bin/sync")
#		call("/usr/bin/sudo /sbin/reboot -f")
