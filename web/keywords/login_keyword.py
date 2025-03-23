from selenium.webdriver.common.by import By


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
