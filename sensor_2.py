#!/usr/bin/python
import sys
import os
import time
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
temp_file = '/sys/bus/w1/devices/28-011452e96eaa/w1_slave'
 
def read_temp_file():
    f = open(temp_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_file()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.1)
        lines = read_temp_file()
    temp_output = lines[1].find('t=')
    if temp_output == -1:
        return -1
    temp_string = lines[1].strip()[temp_output+2:]
    temp_c = float(temp_string) / 1000.0
    return temp_c
temp_c = (read_temp())
while (temp_c !=85.0):
    print(temp_c)
    sys.exit(1)
