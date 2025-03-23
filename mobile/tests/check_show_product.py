import unittest , os , sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from keywords.mobile_common import Moblie_Keywword

class CheckProductTest(unittest.TestCase):
    def setUp(self):
        self.driver = Moblie_Keywword.open_app("Flutter")
    
    def testProductList(self):
        """"""
        activity = self.driver.current_activity
        self.assertIsNone(activity,"Noo")
        
    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()