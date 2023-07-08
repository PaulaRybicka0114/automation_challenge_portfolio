from pages.base_page import BasePage


class LoginPage(BasePage):
    headline_xpath = "//h5"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    remind_password_button_xpath = "//child::div/a"
    change_language_button_xpath = "//*/form/div/div[2]/div/input"
    sign_in_button_xpath = "//*[text()='Sign in']"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
