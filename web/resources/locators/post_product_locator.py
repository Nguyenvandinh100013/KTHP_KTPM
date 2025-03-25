from selenium.webdriver.common.by import By
class Post_Product_Locator:
    txt_name_product = (By.XPATH,"//input[@id='name']")
    txt_product_description = (By.XPATH,"//textarea[@id='description']")
    txt_product_price = (By.XPATH, "//input[@id='price']")
    txt_product_brand = (By.XPATH, "//input[@id='thuong_hieu']")
    lbl_img_upload = (By.XPATH, "//input[@id='img']")
    btn_post_product = (By.XPATH, "//button[contains(text(),'Thêm sản phẩm')]")
    lbl_my_product_page = (By.XPATH, "//p[@class='title-page']")
    
    # DYNAMIC XPATH
    txt_product_type = "//label[contains(text(),'_DYNAMIC_')]"
    txt_product_status = "//label[normalize-space()='_DYNAMIC_']"