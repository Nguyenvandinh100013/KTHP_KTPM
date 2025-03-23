from appium import webdriver
from appium.options.android import UiAutomator2Options
import os , sys
moblie_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(moblie_root)
from resources.device.device_map import adnroid_device , appium_sever_url

class Moblie_Keywword:    
    @staticmethod
    def open_app(app,NoReset=True):
        app_path = os.path.join(moblie_root,"app_file",f"{app}.apk")
        if not os.path.exists(app_path):
            raise FileNotFoundError(f"App {app_path} not found")
        adnroid_device["noReset"] = NoReset
        adnroid_device["app"] = app_path
        driver = webdriver.Remote(appium_sever_url,options=UiAutomator2Options().load_capabilities(adnroid_device))
        return driver

    def login(username,password):
        