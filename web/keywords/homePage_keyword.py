import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from resources.locators.homePage_locator import HomePage_Locator

class HomePage:
    def __init__(self,driver):
        self.driver = driver
    def verify_logo_profile_visible(self):
        self.driver.find_element("xpath",HomePage_Locator.lbl_logo_user)
    def 