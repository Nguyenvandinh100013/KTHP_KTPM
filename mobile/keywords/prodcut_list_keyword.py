from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys , os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from keywords.mobile_common import Moblie_Keywword
from resources.locator.productList_locator import ProductList_Locator


class Product_list:
    @staticmethod
    def tap_product_type_by_label(driver,product_type):
        element = ProductList_Locator.txt_product_type.replace("_DYNAMIC_",product_type)
        wait = WebDriverWait(driver, 30)
        element_visible = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, element)))
        element_visible.click()
    @staticmethod
    def verify_product_display(driver, product):
        element = ProductList_Locator.lbl_product_image.replace("_DYNAMIC_",product)
        Moblie_Keywword.scroll_down_to_element(driver, element)
