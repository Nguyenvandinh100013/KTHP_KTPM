import unittest , sys , os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from resources.init import *
from keywords.homePage_keyword import HomePage
from keywords.excel.excel_common import Excel

class LoginTest(unittest.TestCase):
    """Testcase Cho chức năng đăng nhập"""
    @classmethod
    def setUpClass(cls):
        """Mở trình duyệt trước khi chạy tất cả các test"""
        cls.driver = BrowserSetup.get_driver()
        cls.driver.get(Config.LOGIN_URL)
        cls.login_page = LoginPage(cls.driver)
        Web_Common.wait_for_web_load_successfully(cls.driver)
        data = Excel.get_login_data()
        cls.email, cls.password = data[0]
        
    def test_login_successfully(self):
        """TC_DN_01-Đăng nhập thành công với email và password hợp lệ"""
        self.login_page.open_login_page()
        self.login_page.enter_username(self.email)
        self.login_page.enter_password(self.password)
        self.login_page.click_login_btn()
        home_page = HomePage(self.driver)
        home_page.verify_logo_profile_visible()
    
    def test_login_fail_email(self):
        """TC_DN_02_Đăng nhập thất bại khi email không hợp lệ"""
        self.login_page.open_login_page()
        self.login_page.enter_username("emailWrong@gmail.com")
        self.login_page.enter_password(self.password)
        self.login_page.click_login_btn()
        self.login_page.verify_error_login()
    
    def test_login_fail_pass(self):
        """TC_DN_03_Đăng nhập thất bại khi password không hợp lệ"""
        self.login_page.open_login_page()
        self.login_page.enter_username(self.email)
        self.login_page.enter_password("123")
        self.login_page.click_login_btn()
        self.login_page.verify_error_login()
        
    def test_login_fail_empty(self):
        """TC_DN_04_Đăng nhập thất bại khi bỏ trống email và password"""
        self.login_page.open_login_page()
        self.login_page.enter_username("")
        self.login_page.enter_password("")
        self.login_page.click_login_btn()
        self.login_page.verify_error_login()
    
    def test_login_fail_both(self):
        """TC_DN_05_Đăng nhập thất bại khi cả email và password không hợp lệ"""
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
    test_suite.addTest(LoginTest("test_login_fail_email"))
    test_suite.addTest(LoginTest("test_login_fail_pass"))
    test_suite.addTest(LoginTest("test_login_fail_empty"))
    test_suite.addTest(LoginTest("test_login_fail_both"))
    test_suite.addTest(LoginTest("test_login_successfully"))
    return test_suite

if __name__ == "__main__":
    runner = run_tests()
    runner.run(TestSuite())