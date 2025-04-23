import unittest , os , sys, time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from keywords.mobile_common import Moblie_Keywword
from keywords.signup_keyword import SignUp_Keyword
from keywords.home_keyword import Home_keyword
from keywords.csv_file.csv import CSV


class SignUp_Test(unittest.TestCase):
    """Kieemm tra chưc năng đang kí"""
    @classmethod
    def setUpClass(cls):
        cls.driver = Moblie_Keywword.open_app("Gake")
        SignUp_Keyword.go_to_sign_up_page(cls.driver)
        
    def test_signup_successfully(self):
        """TC_DK_01: Đăng ký thanh công và dăng nhập tài khoản dã daăg kí"""
        new_email = f"phuc{int(time.time())}@gmail.com"
        new_password = "123123"
        SignUp_Keyword.sign_up(self.driver, "van", "phuc", new_email, new_password, new_password)
        SignUp_Keyword.verify_signup_successfully(self.driver)
        Moblie_Keywword.login(self.driver, new_email, new_password)
        Home_keyword.verìy_logo_shop_display(self.driver)
        CSV.write_csv_file("logindata.csv",[new_email, new_password])
        print(new_email, new_password)
        
    def test_signup_fail_first_name(self):
        """TC_DK_02: Đăng ký thất bại khi họ không hợp lệ"""
        SignUp_Keyword.sign_up(self.driver, "", "phuc", "phuc1215@gmail.com", "123123", "123123")
        SignUp_Keyword.verify_error_signup(self.driver, "Error creating user")
    
    def test_signup_fail_last_name(self):
        """TC_DK_03: Đăng ký thất bại khi tên không hợp lệ"""
        SignUp_Keyword.sign_up(self.driver, "phuc", "", "phuc1215@gmail.com", "123123", "123123")
        SignUp_Keyword.verify_error_signup(self.driver, "Error creating user")
    
    def test_signup_fail_email(self):
        """TC_DK_04: Đăng ký thất bại khi email không hợp lệ"""
        SignUp_Keyword.sign_up(self.driver, "phuc", "van", "phuc@gmail.com", "123123", "123123")
        SignUp_Keyword.verify_error_signup(self.driver, "Email already in use")
    
    def test_signup_fail_password(self):
        """TC_DK_05: Đăng ký thất bại khi mat khau không hợp lệ"""
        SignUp_Keyword.sign_up(self.driver, "phuc", "van", "phuc1215@gmail.com", "123123", "1231234")
        SignUp_Keyword.verify_error_signup(self.driver, "Mật khẩu xác nhận không khớp")
    
    def test_signup_fail_confirm_pass(self):
        """TC_DK_07: Đăng ký thất bại khi tat ca không hợp lệ"""
        SignUp_Keyword.sign_up(self.driver, "", "", "", "", "")
        SignUp_Keyword.verify_error_signup(self.driver, "Error creating user")

    @classmethod
    def tearDownClass(cls):
        Moblie_Keywword.close_app(cls.driver)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()