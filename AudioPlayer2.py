#!/usr/bin/env python
import os
import sys
from optparse import OptionParser
import time
import math
f = open("/var/www/html/Bell/waittime.txt", "r")
a = []
for line in f:
	a.append(line)

print a[0]
Wait_Time = 8000
#Wait_Time = 5000
path = "/home/pi/Music/Villa_Musica/"
min = str(math.floor(Wait_Time/60))

def Bash_Time_func(name):
	return os.popen("omxplayer " + path + "Wait_Time_" +str(name) + ".wav")


def Second_Dig(num):
	return os.popen("omxplayer " + path + "Wait_Time_" + str(num) + "0.wav")


def Teens(num):
	return os.popen("omxplayer " + path + "Wait_Time_1" + str(num) + ".wav")


if isinstance(Wait_Time, (int, long)) == 0:
	exit(1)

if Wait_Time <= 0:
	exit(0)


Bash_Time = os.popen("omxplayer " + path + "Wait_Time_Start.wav")
print Bash_Time.read()

min_len = int(len(min))
if min_len == 3:
	Bash_Time = Bash_Time_func(100)
	print Bash_Time.read()
	time.sleep(1)
	if min[1] == 1:
		Bash_Time = Bash_Time_func(min[2])
		print Bash_Time.read() 
	else:
		Bash_Time = Second_Dig(min[1])
		print Bash_Time.read()
		Bash_Time = Bash_Time_func(min[2])
		print Bash_Time.read()
elif min_len == 2:
	if min[0] == 1:
		Bash_Time = Bash_Time_func(min[1])
		print Bash_Time.read()
	else:
		Bash_Time = Second_Dig(min[0])
		print Bash_Time.read()
		Bash_Time = Bash_Time_func(min[1])
		print Bash_Time.read()
elif min_len == 1:
	Bash_Time = Bash_Time_func(min)
	print Bash_Time.read()
else:
	print "Nothing"

Bash_Time = os.popen("omxplayer " + path + "Wait_Time_Minutes.wav")
print Bash_Time.read()
