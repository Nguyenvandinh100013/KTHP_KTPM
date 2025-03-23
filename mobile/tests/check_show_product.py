import unittest , os , sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from keywords.mobile_common import Moblie_Keywword
from keywords.prodcut_list_keyword import Product_list

class CheckProductTest(unittest.TestCase):
    def setUp(self):
        self.driver = Moblie_Keywword.open_app("Flutter")
        Moblie_Keywword.login(self.driver)
    
    def testProductList(self):
        """Kiểm tra sản phẩm rau củ"""
        Product_list.tap_product_type_by_label(self.driver, "Rau củ")
        Product_list.verify_product_display(self.driver,"Shino\n1 VND")
        
    def tearDown(self):
        if self.driver:
            self.driver.terminate_app("com.example.man_hinh")
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
