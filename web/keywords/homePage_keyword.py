import sys , os
from selenium.webdriver.common.by import By
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from resources.locators.homePage_locator import HomePage_Locator
from keywords.web_common import Web_Common

class HomePage:
    def __init__(self,driver):
        self.driver = driver
    def verify_logo_profile_visible(self):
        self.driver.find_element(*HomePage_Locator.lbl_logo_user)
    def select_product_type_by_label(self,product_type):
        product = Web_Common.genarate_xpath_by_value(HomePage_Locator.txt_type_product,product_type)
        self.driver.find_element(*HomePage_Locator.lbl_nav_bar_product_type).click()
        self.driver.find_element(By.XPATH,product).click()
    def select_option_menu_on_profile(self,option):
        option_admin = Web_Common.genarate_xpath_by_value(HomePage_Locator.txt_option_profile_select, option)
        self.driver.find_element(*HomePage_Locator.lbl_logo_user).click()
        self.driver.find_element(By.XPATH,option_admin).click()