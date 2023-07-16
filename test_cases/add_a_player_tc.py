import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.add_a_player import AddAPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestDashboard(unittest.TestCase):
    add_player_button_xpath = "//*/div[2]/div/div/a/button"
    add_player_form_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player()
        time.sleep(5)

    def test_add_player_form(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player()
        add_a_player = AddAPlayer(self.driver)
        add_a_player.type_in_email('user01@getnada.com')
        add_a_player.type_in_name("Jan")
        add_a_player.type_in_surname("Nowak")
        add_a_player.type_in_phone("123456789")
        add_a_player.type_in_weight("100")
        add_a_player.type_in_height("190")
        add_a_player.type_in_club("Culture Club")
        add_a_player.type_in_level("high")
        add_a_player.type_in_main_position("shooter")
        add_a_player.type_in_second_position("none")
        add_a_player.type_in_achievements("yes")
        add_a_player.click_on_submit_button()
        add_a_player.click_on_age()
        add_a_player.click_on_submit_button()
        add_a_player.wait_for_required()

    def test_clear_form(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player()
        add_a_player = AddAPlayer(self.driver)
        add_a_player.type_in_email('user01@getnada.com')
        add_a_player.type_in_name("Jan")
        add_a_player.type_in_surname("Nowak")
        add_a_player.type_in_phone("123456789")
        add_a_player.type_in_weight("100")
        add_a_player.type_in_height("190")
        add_a_player.type_in_club("Culture Club")
        add_a_player.type_in_level("high")
        add_a_player.type_in_main_position("shooter")
        add_a_player.type_in_second_position("none")
        add_a_player.type_in_achievements("yes")
        time.sleep(3)
        add_a_player.click_clear()
        time.sleep(3)


    @classmethod
    def tearDown(self):
        self.driver.quit()