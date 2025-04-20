class SignUp_Locator:
    txt_firstname = '//android.view.View[@content-desc="First Name"]/following-sibling::android.widget.EditText[1]'
    txt_lastname = '//android.view.View[@content-desc="First Name"]/following-sibling::android.widget.EditText[2]'
    txt_email = '//android.view.View[@content-desc="First Name"]/following-sibling::android.widget.EditText[3]'
    txt_password = '//android.view.View[@content-desc="First Name"]/following-sibling::android.widget.EditText[4]'
    txt_confirm_pass = '//android.view.View[@content-desc="First Name"]/following-sibling::android.widget.EditText[5]'
    btn_sign_up = '//android.widget.Button[@content-desc="SIGN UP"]'
    # DYNAMIC
    txt_error_signup = '//android.view.View[@content-desc="DYNAMIC"]'
