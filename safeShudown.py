#!usr/bin/python

#Really safe shutdown
#The script requires the button to be pushed for at least 2 seconds before shutting down the Raspberry Pi
#In addition, the shutdown command is only fired once

#Config:
#The button is connected to pin 27 on the Raspberry Pi; change if desired
#The required time is set to 2 seconds; change line "if timeDiff > 2"

#This file should run in the boot. To add, edit or remove it from the boot sequence, do the following:
#In terminal: sudo nano /etc/rc.local
#Edit or remove the next line, that's placed just before exit: sudo python /home/pi/safeShudown.py &

import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)

global timeFirst, timeSecond, shutdownFired
timeFirst = False
shutdownFired = False

while True:

    if GPIO.input(27) and not shutdownFired:

        if not timeFirst:
            timeFirst = time.time()

        if GPIO.input(27):
            timeSecond = time.time()
            timeDiff =  timeSecond - timeFirst

            if timeDiff > 2:
                print('System is going to shutdown')
                timeFirst = False
                GPIO.cleanup()
                os.system("sudo shutdown -h now")
                shutdownFired = True

    if not GPIO.input(27):
        timeFirst = False

    time.sleep(0.2)
