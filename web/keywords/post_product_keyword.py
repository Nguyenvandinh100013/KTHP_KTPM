import sys , os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
web_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(web_root)
from keywords.web_common import Web_Common
from resources.locators.post_product_locator import Post_Product_Locator
from keywords.homePage_keyword import HomePage

class Post_Product:
    def __init__(self,driver):
        self.driver = driver
        self.homepage = HomePage(self.driver)
    def post_product_by_admin(self, name, type_product, description, price, brand, status, img1,img2,img3,img4):
        self.homepage.select_option_menu_on_profile("Đăng sản phẩm")    
        product_type = Web_Common.genarate_xpath_by_value(Post_Product_Locator.txt_product_type,type_product)
        product_status = Web_Common.genarate_xpath_by_value(Post_Product_Locator.txt_product_status, status)
        self.driver.find_element(*Post_Product_Locator.txt_name_product).send_keys(name)
        self.driver.find_element(By.XPATH, product_type).click()
        self.driver.find_element(*Post_Product_Locator.txt_product_description).send_keys(description)
        self.driver.find_element(*Post_Product_Locator.txt_product_price).send_keys(price)
        self.driver.find_element(*Post_Product_Locator.txt_product_brand).send_keys(brand)
        self.driver.find_element(By.XPATH, product_status).click()
        img_path = os.path.join(web_root,"resources","testdata","upload_img")
        self.driver.find_element(*Post_Product_Locator.lbl_img_upload).send_keys(os.path.join(img_path,f"{img1}"))
        self.driver.find_element(*Post_Product_Locator.lbl_img_upload).send_keys(os.path.join(img_path,f"{img2}"))
        self.driver.find_element(*Post_Product_Locator.lbl_img_upload).send_keys(os.path.join(img_path,f"{img3}"))
        self.driver.find_element(*Post_Product_Locator.lbl_img_upload).send_keys(os.path.join(img_path,f"{img4}"))
        self.driver.find_element(*Post_Product_Locator.btn_post_product).click()
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.presence_of_element_located(*Post_Product_Locator.lbl_my_product_page))
