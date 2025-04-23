import unittest , os , sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from keywords.mobile_common import Moblie_Keywword
from keywords.home_keyword import Home_keyword
from keywords.csv_file.csv import CSV


class CheckProductTest(unittest.TestCase):
    """Test case cho chức năng kiểm tra sản phẩm"""
    @classmethod
    def setUpClass(cls):
        cls.driver = Moblie_Keywword.open_app("Gake")
        data = CSV.read_csv_data('logindata.csv')
        [email, password] = data[1]
        Moblie_Keywword.login(cls.driver, email, password)
    
    def test_ProductList(self):
        """TC_FL_02: Kiểm tra bộ lọc danh mục sản phẩm rau củ"""
        Home_keyword.tap_product_type_by_label(self.driver, "Rau củ")
        Home_keyword.verify_product_display(self.driver,"cam\n200 VND")
    
    def test_check_productdetail(self):
        """TC_FL_03: Kiểm tra hiển thị chi tiết sản phẩm theo mục danh sách sản phẩm"""
        Home_keyword.tap_product(self.driver, "cam\n200 VND")
        Home_keyword.verify_product_detail_display(self.driver, "cam")
        Moblie_Keywword.tap_on_back_button(self.driver)
    
    def test_search_product(self):
        """TC_FL_05: Kiểm tra search sản phẩm"""
        Home_keyword.search_product(self.driver, "cam")
        Home_keyword.verify_product_not_display(self.driver, "Cà Rốt\n40000 VND")
    
    @classmethod
    def tearDownClass(cls):
        Moblie_Keywword.close_app(cls.driver)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
