from pages.base_page import BasePage


class LoginPage(BasePage):
    headline_xpath = "//h5"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    remind_password_button_xpath = "//child::div/a"
    change_language_button_xpath = "//*/form/div/div[2]/div/input"
    sign_in_button_xpath = "//*[text()='Sign in']"
    error_info_xpath = "//*[text()='Identifier or password invalid.']"
    message_sent_successfully_xpath = "//*[text()='Message sent successfully.']"
    expected_title = "Scouts panel - sign in"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    expected_text = "Scouts Panel"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def click_on_the_remind_password_button(self):
        self.click_on_the_element(self.remind_password_button_xpath)

    def error_info_visible(self):
        self.visibility_of_element_located(self.error_info_xpath)

    def message_sent_visible(self):
        self.visibility_of_element_located(self.message_sent_successfully_xpath)