from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Web_Common: 
    @staticmethod       
    def genarate_xpath_by_value(xpath_element,value):
        return xpath_element.replace("_DYNAMIC_", value)
    @staticmethod
    def wait_for_web_load_successfully(driver):
        for i in range(10):
            try:
                WebDriverWait(driver, timeout=15).until(EC.presence_of_element_located((By.XPATH, "//img[@class='d-inline-block align-top']")))
            except:
                print(f"Chay lan {i + 1} web chua load")
