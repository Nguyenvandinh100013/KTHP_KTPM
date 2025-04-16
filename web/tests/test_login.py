import unittest , sys , os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from resources.init import *
from keywords.homePage_keyword import HomePage

class LoginTest(unittest.TestCase):
    """Testcase Cho chức năng đăng nhập"""
    @classmethod
    def setUpClass(cls):
        """Mở trình duyệt trước khi chạy tất cả các test"""
        cls.driver = BrowserSetup.get_driver()
        cls.driver.get(Config.LOGIN_URL)
        cls.login_page = LoginPage(cls.driver)
        Web_Common.wait_for_web_load_successfully(cls.driver)
        
    def test_login(self):
        """TC_DN_05-Kiểm tra đăng nhập khi nhập vào số điện thoại và mật khẩu đã được đăng ký."""
        self.login_page.open_login_page()
        self.login_page.enter_username(TestData.admin_account.email)
        self.login_page.enter_password(TestData.admin_account.password)
        self.login_page.click_login_btn()
        home_page = HomePage(self.driver)
        home_page.verify_logo_profile_visible()
        
    def test_login_fail(self):
        """TC_DN_06_Kiểm tra đăng nhập khi nhập sai email và password"""
        self.login_page.open_login_page()
        self.login_page.enter_username("emailWrong@gmail.com")
        self.login_page.enter_password("wrongpass")
        self.login_page.click_login_btn()
        self.login_page.verify_error_login()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

def TestSuite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(LoginTest("test_login_fail"))
    test_suite.addTest(LoginTest("test_login"))
    return test_suite

if __name__ == "__main__":
    runner = run_tests()
    runner.run(TestSuite())