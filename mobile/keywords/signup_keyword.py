from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os , sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from resources.locator.home_locator import Home_Locator
from resources.locator.login_locator import Login_Locator
from keywords.mobile_common import Moblie_Keywword
from resources.locator.signup_locator import SignUp_Locator


import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

class SignUp_Keyword:
    @staticmethod
    def go_to_sign_up_page(driver):
        try:
            wait = WebDriverWait(driver, 3)
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH,Home_Locator.lbl_logo_gake)))
            Moblie_Keywword.logout(driver)
            driver.find_element(AppiumBy.XPATH, Login_Locator.txt_sign_up).click()
        except:
            driver.find_element(AppiumBy.XPATH, Login_Locator.txt_sign_up).click()
    
    @staticmethod
    def sign_up(driver, first_name, last_name, email, password, confirm_pass):
        wait = WebDriverWait(driver, 3)
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, SignUp_Locator.txt_firstname)))
        frirst_name_input = driver.find_element(AppiumBy.XPATH, SignUp_Locator.txt_firstname)
        frirst_name_input.click()
        frirst_name_input.clear()
        frirst_name_input.send_keys(first_name)
        last_name_input = driver.find_element(AppiumBy.XPATH, SignUp_Locator.txt_lastname)
        last_name_input.click()
        last_name_input.clear()
        last_name_input.send_keys(last_name)
        email_input = driver.find_element(AppiumBy.XPATH, SignUp_Locator.txt_email)
        email_input.click()
        email_input.clear()
        email_input.send_keys(email)
        password_input = driver.find_element(AppiumBy.XPATH, SignUp_Locator.txt_password)
        password_input.click()
        password_input.clear()
        password_input.send_keys(password)
        Moblie_Keywword.scroll_down_to_element(SignUp_Locator.txt_confirm_pass)
        confirm_pass_input = driver.find_element(AppiumBy.XPATH, SignUp_Locator.txt_confirm_pass)
        confirm_pass_input.click()
        confirm_pass_input.clear()
        confirm_pass.send_keys(confirm_pass)
        Moblie_Keywword.scroll_down_to_element(SignUp_Locator.btn_sign_up)
        driver.find_element(AppiumBy.XPATH, SignUp_Locator.btn_sign_up).click()

    @staticmethod
    def verify_error_signup(driver, error):
        element = SignUp_Locator.txt_error_signup.replace("_DYNAMIC_",error)
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, element)))
