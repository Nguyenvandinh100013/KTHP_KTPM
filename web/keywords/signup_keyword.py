from selenium.webdriver.common.by import By


class SignUp:
    def __init__(self,driver):
        self.driver = driver
        self.btn_signup_home = (By.XPATH,"//a[contains(text(),'Đăng ký')]")
        self.txt_first_name = (By.XPATH,"//input[@id='firstname']")
        self.txt_last_name = (By.XPATH,"//input[@id='lastname']")
        self.txt_email = (By.XPATH,"//input[@id='email']")
        self.txt_password = (By.XPATH,"//input[@id='password']")
        self.txt_corfirm_password = (By.XPATH,"//input[@id='confirmPassword']")
        self.btn_button_on_signUp = (By.XPATH,"//button[@type='submit'][contains(text(),'Đăng ký')]")
        self.txt_error = (By.XPATH,"//div[@class='user-message-error']")
        
    def SignUp(self,first_name,last_name,email,password,corfirm_password):
        self.driver.find_element(*self.btn_signup_home).click()
        self.driver.find_element(*self.txt_first_name).send_keys(first_name)
        self.driver.find_element(*self.txt_last_name).send_keys(last_name)
        self.driver.find_element(*self.txt_email).send_keys(email)
        self.driver.find_element(*self.txt_password).send_keys(password)
        self.driver.find_element(*self.txt_corfirm_password).send_keys(corfirm_password)
        self.driver.find_element(*self.btn_button_on_signUp).click()
    
    def get_error_signup(self):
        text_fail = self.driver.find_element(*self.txt_error).text
        return text_fail
    
    def Verify_error_email(self):
        text_email_fail = SignUp.get_error_signup(self)
        assert text_email_fail == "Vui lòng nhập email hợp lệ!"

    def get_result_signup(self, is_login_visible):
        if is_login_visible:
                return "PASS"
        else:
            return SignUp.get_error_signup(self)
    
    def verify_error_signup(self, error):
        text_email_fail = SignUp.get_error_signup(self)
        assert text_email_fail == error
