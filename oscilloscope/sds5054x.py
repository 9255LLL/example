#!/c/Users/CSJY/AppData/Local/Programs/Python/Python37/python.exe

Version = "V1.0.0"

import serial
import threading
import time
import sys

import pyvisa as visa

rm = visa.ResourceManager()

dev = rm.list_resources()

print(dev)

usb_dev = dev[2]

usb_inst = rm.open_resource(usb_dev)
 
print(usb_inst.query("*IDN?")) 


usb_inst.write ("MEAS ON")					#开启测量
usb_inst.write("MEAS:MODE ADV")				#使用高级测量
usb_inst.write("MEAS:ADV:P1 ON")			#使用P1位
usb_inst.write("MEAS:ADV:P1:TYPE MEAN")	

usb_inst.write("MEAS:ADV:P1:SOUR1 C1")		#信号源为模拟通道1

usb_inst.write("MEAS:ADV:STAT:RES")			#复位，从新开始计算平均值和监测最值


time.sleep(5)

print("p3 VALUE =", usb_inst.query("MEAS:ADV:P1:VAL?"))
print("P1 AVERAGE VALUE =", usb_inst.query("MEAS:ADV:P1:STAT? MEAN"))

	
	
	


