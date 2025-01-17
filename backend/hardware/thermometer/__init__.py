"""
This module contains the implementations of the thermometer. See base.py for the abstract class used
and either the individual files or backend/config.py for configuration information.
"""
from hardware.thermometer.w1_therm import W1TempSensor
from hardware.thermometer.serial import SerialTempSensor

def createThermometer(thermometerConfig, devices):
  thermometerType = thermometerConfig['implementation']
  if thermometerType == "w1_therm":
    return W1TempSensor()
  elif thermometerType == "serial":
    return SerialTempSensor(thermometerConfig) 
  
  raise Exception("Unsupported thermometer type")
