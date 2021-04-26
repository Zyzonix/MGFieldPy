#!/usr/bin/python3
#
# written by @author ZyzonixDev
# published by ZyzonixDevelopments 
# -
# date      | 25/04/2021
# python-v  | 3.5.3
# -
# file      | static/dataHandler.py
# project   | MGFieldPy
# project-v | 0.1
# 
from datetime import datetime
import random
import psutil
import board    
import os                                   
import busio                                       
import adafruit_ads1x15.ads1115 as ADS         
from adafruit_ads1x15.analog_in import AnalogIn 
import mgfield

class inputMethods():
    # input from file (virtual enviroment)
    def importDataFromFile(self):
        value_list = []
        input_file = open(os.getcwd() + "/static/data.txt", "r")
        for line in input_file:
            value_list.append(str(line))
        # getting random value
        result = value_list[random.randint(1, len(value_list) - 1)]
        result = result.rstrip(result[-1])
        result = result.rstrip(result[-1])
        print(mgfield.Core.getCTime(self), "got", result, "as value")
        return float(result)

    # input from sensor
    def importDataFromSensor(self):
        i2c = busio.I2C(board.SCL, board.SDA)                          
        # creating the ADC object using the I2C bus
        ads = ADS.ADS1115(i2c) 
        # creating single-ended input on channel 0
        x = AnalogIn(ads, ADS.P0)
        y = AnalogIn(ads, ADS.P1)
        z = AnalogIn(ads, ADS.P2)
        # calculating value
        result = (((x.value * x.value) + (y.value * y.value) + (z.value * z.value)) ** 0.5)          ##
        print(mgfield.Core.getCTime(self), "got", result, "as value")
        return result

# retrieving current temperature from 1-wire sensor
def getTemperature():
    # opening file that contains the temperature
    try:
        sensor = open('/sys/bus/w1/devices/28-01193a114ec3/w1_slave')
        temp_raw = sensor.read()
        sensor.close()

        # selecting / calculating temperature
        temp_string = temp_raw.split("\n")[1].split(" ")[9]
        temp = float(temp_string[2:]) / 1000
        value = str('%6.2f' % temp)
    except:
        value = 1.00
    return value

# retrieving ram utilisation
def getSystemStatistics():
    ram_percent = float(psutil.virtual_memory().percent)
    return ram_percent

# input method resolver
def handleInputMethod(self):
    if self.input == 1:
        self.inputMethod = getattr(inputMethods, "importDataFromSensor")
    else:
        self.inputMethod = getattr(inputMethods, "importDataFromFile")
