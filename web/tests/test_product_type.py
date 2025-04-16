import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from keywords.product_keyword import Product
from keywords.homePage_keyword import HomePage
from resources.init import *

class Product_Test(unittest.TestCase):
    def setUp(self):
        self.driver = BrowserSetup.get_driver()
        self.driver.get(Config.LOGIN_URL)
        self.product_keyword = Product(self.driver)
        self.home_keyword = HomePage(self.driver)
        Web_Common.wait_for_web_load_successfully(self.driver)
    
    def test_product_raucu(self):
        """TC_CTSP_01-Kiểm tra xem sản phẩm chi tiết sản phẩm rau củ."""
        self.home_keyword.select_product_type_by_label("Rau củ")
        self.product_keyword.verify_product_name_visble("Shino")
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    runner = run_tests()
    runner.run(unittest.defaultTestLoader.loadTestsFromTestCase(Product_Test))