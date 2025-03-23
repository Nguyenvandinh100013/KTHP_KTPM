import unittest , time , os , sys
from selenium.webdriver.common.by import By
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from keywords.browser_setup import BrowserSetup
from keywords.login_keyword import LoginPage
from keywords.signup_keyword import SignUp
from resources.config.config_web import Config
from tests.auto_generate_report import run_tests

class SignupTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserSetup.get_driver()
        cls.driver.get(Config.LOGIN_URL)
        cls.signupPage = SignUp(cls.driver)
        cls.loginPage = LoginPage(cls.driver)

    def test_signup_fail(self):
        """TC_DK_03-Kiểm tra đăng ký khi nhập vào thông tin email tài khoản đã tồn tại."""
        new_email = "phuc@gmail.com"
        new_password = "123456"
        self.signupPage.SignUp("Phuc","Van",new_email,new_password,new_password)
        self.signupPage.Verify_error_email()
    
    def test_signup(self):
        """TC_DK_02-Tiến hành đăng ký tài khoản nhập vào các thông tin sau họ và tên, email,  mật khẩu ( từ 6 kí tự trở lên), xác nhập  mật khẩu và click ô đăng kí."""
        new_email = f"user{int(time.time())}@gmail.com"
        new_password = "123456"
        self.signupPage.SignUp("Phuc","Van",new_email,new_password,new_password)
        self.loginPage.verify_login_page_visible()
        print(f"Signup Sussesfully: {new_email} - {new_password}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
def TestSuite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(SignupTest("test_signup_fail"))
    test_suite.addTest(SignupTest("test_signup"))
    return test_suite

if __name__ == "__main__":
    runner = run_tests()
    runner.run(TestSuite())