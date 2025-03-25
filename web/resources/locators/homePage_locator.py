from selenium.webdriver.common.by import By
class HomePage_Locator:
    lbl_logo_user = (By.XPATH,"//div[@id='navbarSupportedContent']//a[@id='navbarDropdown']")
    lbl_nav_bar_product_type = (By.XPATH,"//a[@id='navbarDropdown']")
    # DYNAMIC XPATH
    txt_type_product = "//a[contains(text(),'_DYNAMIC_')]"
    txt_option_profile_select = "//a[contains(text(),'_DYNAMIC_')]"