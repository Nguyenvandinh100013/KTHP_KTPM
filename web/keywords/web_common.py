from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Web_Common: 
    @staticmethod       
    def genarate_xpath_by_value(xpath_element,value):
        return xpath_element.replace("_DYNAMIC_", value)