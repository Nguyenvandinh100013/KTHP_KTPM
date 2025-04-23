import unittest , time , os , sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from resources.init import *
from keywords.signup_keyword import SignUp
from keywords.excel.excel_common import Excel

class SignupTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserSetup.get_driver()
        cls.driver.get(Config.LOGIN_URL)
        cls.signupPage = SignUp(cls.driver)
        cls.loginPage = LoginPage(cls.driver)
        Web_Common.wait_for_web_load_successfully(cls.driver)

    def test_signup_successfully(self):
        """TC_DK_01-Đăng ký thành công với thông tin hợp lệ (họ, tên, email, mật khẩu hợp lệ)"""
        new_email = f"user{int(time.time())}@gmail.com"
        new_password = "123456"
        self.signupPage.SignUp("Phuc","Van",new_email,new_password,new_password)
        is_login_visible = self.loginPage.verify_login_page_visible()
        result = self.signupPage.get_result_signup(is_login_visible)
        Excel.write_data_to_excel(new_email, new_password, result)
        print(f"Signup Sussesfully: {new_email} - {new_password} - {result}")

    def test_signup_fail_email_name(self):
        """TC_DK_04-Đăng ký thất bại khi email không hợp lệ"""
        new_email = "phuc"
        new_password = "123456"
        self.signupPage.SignUp("Phuc","Van", new_email, new_password, new_password)
        self.signupPage.Verify_error_email()
    
    def test_signup_fail_password(self):
        """TC_DK_05-Đăng ký thất bại khi mật khẩu không hợp lệ"""
        new_email = f"user{int(time.time())}@gmail.com"
        new_password = "123"
        self.signupPage.SignUp("Phuc","Van",new_email,new_password,new_password)
        self.signupPage.verify_error_signup("Vui lòng nhập mật khẩu chỉ có số và văn bản và ít nhất 6 ký tự!")
    
    def test_signup_fail_confirm_pass(self):
        """TC_DK_06-Đăng ký thất bại khi xác nhận mật khẩu không khớp"""
        new_email = f"user{int(time.time())}@gmail.com"
        new_password = "123456"
        self.signupPage.SignUp("Phuc","Van",new_email,new_password,"123678")
        self.signupPage.verify_error_signup("Mật khẩu phải khớp!")
        
    def test_signup_fail_all(self):
        """TC_DK_07-Đăng ký thất bại khi tất cả thông tin không hợp lệ"""
        self.signupPage.SignUp("","","","","")
        self.signupPage.verify_error_signup("Vui lòng nhập email hợp lệ!")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

def TestSuite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(SignupTest("test_signup_fail_email_name"))
    test_suite.addTest(SignupTest("test_signup_fail_password"))
    test_suite.addTest(SignupTest("test_signup_fail_confirm_pass"))
    test_suite.addTest(SignupTest("test_signup_fail_all"))
    test_suite.addTest(SignupTest("test_signup_successfully"))
    return test_suite

if __name__ == "__main__":
    runner = run_tests()
    runner.run(TestSuite())