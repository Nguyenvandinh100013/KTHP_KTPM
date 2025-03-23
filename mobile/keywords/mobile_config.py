import unittest
from appium import webdriver
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from resources.device.device_map import capabilities

def open_app(app,NoReset=True):
print("Capabilities:", capabilities)