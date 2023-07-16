from pages.base_page import BasePage

class RemindPassword(BasePage):
    remind_password_headline_xpath = "//h5"
    e_mail_label_xpath = "//label"
    remind_password_input_xpath = "//*[@id='__next']/div[1]/div/div[1]/div/div/input"
    back_to_sign_in_button_xpath = "//a"
    change_language_button_xpath = "//*/form/div/div[2]/div/input"
    send_password_button_xpath = "//button"

    def click_on_send_button(self):
        self.click_on_the_element(self.send_password_button_xpath)

    def type_in_email(self, email):
        self.field_send_keys(self.remind_password_input_xpath, email)