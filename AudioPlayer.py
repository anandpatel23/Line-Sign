#!/usr/bin/env python
import os
import sys
from optparse import OptionParser;

#Wait_Time = int(sys.argv[1])
Wait_Time = 5000
path = "/home/pi/Music/Villa_Musica/"
min = Wait_Time/60

def Bash_Time_func():
	return os.popen("omxplayer " + path + "Wait_Time_" + str(min) + "min.wav")

if isinstance(Wait_Time, (int, long)) == 0:
	exit(1)

if Wait_Time <= 0:
	exit(0)
elif Wait_Time > 0 and Wait_Time <= 450:
	min = 5
	Bash_Time = Bash_Time_func()
	print Bash_Time.read()
elif Wait_Time > 450 and Wait_Time <= 750:
	min = 10
	Bash_Time = Bash_Time_func() 
	print Bash_Time.read()
elif Wait_Time > 750 and Wait_Time <= 1050:
	min = 15
	Bash_Time = Bash_Time_func()
	print Bash_Time.read()
elif Wait_Time > 1050 and Wait_Time <= 1350:
	min = 20
	Bash_Time = Bash_Time_func()
	print Bash_Time.read()
elif Wait_Time > 1350 and Wait_Time <= 1650:
	min = 25
	Bash_Time = Bash_Time_func()
	print Bash_Time.read()
elif Wait_Time > 1650 and Wait_Time <= 1950:
	min = 30
	Bash_Time = Bash_Time_func()
	print Bash_Time.read()
elif Wait_Time > 1950 and Wait_Time <= 2250:
	min = 35
	Bash_Time = Bash_Time_func()
	print Bash_Time.read()
elif Wait_Time > 2250 and Wait_Time <= 2550:
	min = 40
	Bash_Time = Bash_Time_func()
	print Bash_Time.read()
elif Wait_Time > 2550 and Wait_Time <= 2850:
	min = 45
	Bash_Time = Bash_Time_func()
	print Bash_Time.read()
elif Wait_Time > 2850 and Wait_Time <= 3600:
	min = 60
	Bash_Time = Bash_Time_func()
	print Bash_Time.read()
elif Wait_Time > 3600 and Wait_Time <= 5400:
	min = 90
	Bash_Time = Bash_Time_func()
	print Bash_Time.read()
elif Wait_Time > 5400 and Wait_Time <= 7200:
	min = 120
	Bash_Time = Bash_Time_func()
	print Bash_Time.read()
elif Wait_Time > 7200 and Wait_Time <= 10800:
	min = 180
	Bash_Time = Bash_Time_func()
	print Bash_Time.read()
else:
	Bash_Time = os.popen("omxplayer " + path + "Wait_Time_TooLong.wav")
	print Bash_Time.read()


	
	
	
	
