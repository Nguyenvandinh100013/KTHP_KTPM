from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os , sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from keywords.login_keyword import LoginPage
from keywords.homePage_keyword import HomePage
from resources.testdata.testdata import TestData

class Web_Common:        
    def Login(driver,email=TestData.admin_account.email,password=TestData.admin_account.password):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        login_page.open_login_page()
        login_page.enter_username(email)
        login_page.enter_password(password)
        login_page.click_login_btn()
        home_page.verify_logo_profile_visible()
