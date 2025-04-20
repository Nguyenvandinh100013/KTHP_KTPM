from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys , os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from keywords.mobile_common import Moblie_Keywword
from resources.locator.productList_locator import ProductList_Locator
from resources.locator.home_locator import Home_Locator


class Home_keyword:
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

    @staticmethod
    def search_product(driver, product):
        Home_keyword.tap_product_type_by_label(driver, "Tất cả")
        driver.find_element(AppiumBy.XPATH, Home_Locator.txt_search).send_keys(product)
        
    @staticmethod
    def verify_product_not_display(driver, product):
        element = ProductList_Locator.lbl_product_image.replace("_DYNAMIC_",product)
        assert len(driver.find_elements(AppiumBy.XPATH, element)) == 0, "Product display"
        
    @staticmethod
    def tap_product(driver, product):
        element = ProductList_Locator.lbl_product_image.replace("_DYNAMIC_",product)
        driver.find_element(AppiumBy.XPATH, element).click()
    
    @staticmethod
    def verify_product_detail_display(driver, product):
        element = ProductList_Locator.txt_product_name.replace("_DYNAMIC_",product)
        driver.find_element(AppiumBy.XPATH, element)
        driver.find_element(AppiumBy.XPATH, ProductList_Locator.txt_brand_product)
        