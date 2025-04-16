import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.stdout.reconfigure(encoding='utf-8')
from keywords.post_product_keyword import Post_Product
from keywords.login_keyword import LoginPage
from resources.init import *

class Post_Product_Test(unittest.TestCase):
    def setUp(self):
        self.driver = BrowserSetup.get_driver()
        self.driver.get(Config.LOGIN_URL)
        self.login_page = LoginPage(self.driver)
        self.post_product_page = Post_Product(self.driver)
        Web_Common.wait_for_web_load_successfully(self.driver)

    def test_post_product(self):
        """TC_SP_01-Kiểm tra xem sản phẩm có được thêm vào danh sách sản phẩm không khi thêm một sản phẩm mới với đầy đủ thông tin bắt buộc"""
        self.login_page.Login()
        self.post_product_page.post_product_by_admin("cam", "rau củ", "test post product", "200", "Shino", "Còn hàng", "cam1.jpg", "cam2.jpg", "cam3.jpg", "cam4.jpg")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    runner = run_tests()
    runner.run(unittest.defaultTestLoader.loadTestsFromTestCase(Post_Product_Test))