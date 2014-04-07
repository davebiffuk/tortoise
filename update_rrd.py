#!/usr/bin/python
from rrdtool import update as rrd_update
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

#for n,d in sensors.iteritems():
#	print n, read_sensor(d)
	
#for sensor in ['28-0000043e37d7', '28-00000457d048', '28-0000048be4e7']:
#	print sensor, read_sensor(sensor)

ret = rrd_update('temps.rrd', 'N:%s:%s:%s' %(read_sensor(sensors['white']),
	read_sensor(sensors['black']), read_sensor(sensors['ambient'])));

