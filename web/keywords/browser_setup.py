from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os , sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from resources.config.config_web import Config

class BrowserSetup:
    @staticmethod
    def get_driver():
        driver_path = Config.WEBDRIVER_PATH
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(30)
        driver.maximize_window()
        return driver