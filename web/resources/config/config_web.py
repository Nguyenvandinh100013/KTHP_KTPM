import os , sys
web_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(web_root)
class Config:
    # WEBDRIVER_PATH = "C:/webdrivers/chromedriver.exe"
    WEBDRIVER_PATH = os.path.join(web_root, "driver", "chromedriver.exe")
    LOGIN_URL = "https://webbanhang-6.onrender.com/"