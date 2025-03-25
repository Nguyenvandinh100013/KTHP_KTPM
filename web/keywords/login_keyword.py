from selenium.webdriver.common.by import By
import os , sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from keywords.homePage_keyword import HomePage
from resources.testdata.testdata import TestData

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.btn_menu_login = (By.XPATH,"//a[contains(text(),'Đăng nhập')]")
        self.txt_username_input = (By.XPATH, "//input[@id='email']") 
        self.txt_password_input = (By.XPATH, "//input[@id='password']") 
        self.btn_login_button = (By.XPATH, "//button[contains(text(),'Đăng nhập')]") 
        self.txt_error_messeges = (By.XPATH,"//div[@class='user-message-error']")
        
    def open_login_page(self):
        self.driver.find_element(*self.btn_menu_login).click()
    def enter_username(self,username):
        self.driver.find_element(*self.txt_username_input).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element(*self.txt_password_input).send_keys(password)
    def click_login_btn(self):
        self.driver.find_element(*self.btn_login_button).click()
    def verify_error_login(self):
        self.driver.find_element(*self.txt_error_messeges)
    def verify_login_page_visible(self):
        self.driver.find_element(*self.btn_login_button)
    def Login(self,email=TestData.admin_account.email,password=TestData.admin_account.password):
        home_page = HomePage(self.driver)
        self.open_login_page()
        self.enter_username(email)
        self.enter_password(password)
        self.click_login_btn()
        home_page.verify_logo_profile_visible()