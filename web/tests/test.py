import unittest
from selenium import webdriver
import os , sys , shutil , time
web_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(web_root)
report_dir = os.path.join(web_root, "reports")
if os.path.exists(report_dir):
    shutil.rmtree(report_dir)
# from keywords.web_common import Web_Common
from keywords.browser_setup import BrowserSetup
from keywords.login_keyword import LoginPage
# from keywords.homePage_keyword import HomePage
# from resources.testdata.testdata import TestData
from resources.config.config_web import Config
from tests.auto_generate_report import run_tests

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = BrowserSetup.get_driver()
        self.driver.get(Config.LOGIN_URL)
        self.login_page = LoginPage(self.driver)
    
    def test(self):
        self.driver.find_element("xpath","//p[contains(text(),'Chính sách đổi trả')]").click()
        time.sleep(10)
        
if __name__ == "__main__":
    runner = run_tests()
    runner.run(unittest.defaultTestLoader.loadTestsFromTestCase(Test))