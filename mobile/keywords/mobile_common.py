from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os , sys
moblie_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(moblie_root)
from resources.device.device_map import adnroid_device , appium_sever_url
from resources.locator.login_locator import Login_Locator
from resources.testdata.acccount import TestData

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
    @staticmethod
    def login(driver,username=TestData.user_account.email,password=TestData.user_account.password):
        username_field = driver.find_element(AppiumBy.XPATH,Login_Locator.txt_username)
        username_field.click()
        username_field.send_keys(username)
        email_field = driver.find_element(AppiumBy.XPATH,Login_Locator.txt_password)
        email_field.click()
        email_field.send_keys(password)
        driver.find_element(AppiumBy.XPATH,Login_Locator.btn_login_button).click()
    @staticmethod
    def scroll_down_to_element(driver, element_xpath,max_scrolls=5,timeout=30):
        sreen_size = driver.get_window_size()
        width = sreen_size['width']
        height = sreen_size['height']
        x = width // 2
        y_start = height*0.8
        y_end = height*0.2
        for _ in range(max_scrolls):
            try:
                wait = WebDriverWait(driver, timeout)
                element_visible = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, element_xpath)))
                return element_visible
            except:
                driver.swipe(x,y_start,x,y_end,800)
