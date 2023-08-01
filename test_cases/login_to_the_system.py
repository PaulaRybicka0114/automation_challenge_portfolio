import time

import allure
from selenium.webdriver.chrome.service import Service
import os
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.remind_password import RemindPassword
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en/login')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        user_login.assert_element_text(self.driver, "//h5", 'Scouts Panel')
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()

    def test_log_in_to_the_system_incorrect_data(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-12345')
        user_login.click_on_the_sign_in_button()
        user_login.error_info_visible()
        user_login.assert_element_text(self.driver, "//*[text()='Identifier or password invalid.']", "Identifier or password invalid.")
        user_login.assert_element_text(self.driver, "//h5", 'Scouts Panel')
        self.driver.save_screenshot('TC_02_Log_in')
        self.driver.quit()

    def test_remind_password(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.click_on_the_remind_password_button()
        remind_password = RemindPassword(self.driver)
        remind_password.type_in_email('user01@getnada.com')
        remind_password.click_on_send_button()
        user_login.message_sent_visible()
        user_login.assert_element_text(self.driver, "//h5", 'Scouts Panel')
        self.driver.save_screenshot('TC_03_Incorrect_login_data')
        self.driver.quit()

    @classmethod
    def tearDown(self):
        self.driver.quit()