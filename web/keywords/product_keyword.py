import sys , os
from selenium.webdriver.common.by import By
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from keywords.web_common import Web_Common

class Product:
    def __init__(self,driver):
        self.driver = driver
        self.web_common = Web_Common()
        self.txt_product_name = "//a[normalize-space()='_DYNAMIC_']"
    def verify_product_name_visble(self,product_name):
        product_element = self.web_common.genarate_xpath_by_value(self.txt_product_name, product_name)
        self.driver.find_element(By.XPATH,product_element)