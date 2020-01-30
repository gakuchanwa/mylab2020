#!/usr/bin/env python3

import os
import time
from datetime import datetime

#--------------------------------------------------------------
#  Note: ds18b20's data pin must be connected to pin7(GPIO4).
#--------------------------------------------------------------

# Reads temperature from sensor and prints to stdout
# id is the id of the sensor
def readSensor(id):
    tfile = open("/sys/bus/w1/devices/"+id+"/w1_slave")
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000
    print ("Sensor: " + id  + " - Current temperature : %0.3f C" % temperature)
    o_file = open('/home/pi/googledrive/pydrive-example/src/ondo.txt','w')
    o_file.write(str(temperature) + ' '+ str( datetime.now()))
    o_file.close()


# Reads temperature from all sensors found in /sys/bus/w1/devices/
# starting with "28-...
def readSensors():
    count = 0
    sensor = ""
    for file in os.listdir("/sys/bus/w1/devices/"):
        if (file.startswith("28-")):
            readSensor(file)
            count+=1
    if (count == 0):
        print ("No sensor found! Check connection")

# read temperature every 2second for all connected sensors
def loop():
    while True:
        readSensors()
        time.sleep(2)

# Nothing to cleanup
def destroy():
    pass

# Main starts here
if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
