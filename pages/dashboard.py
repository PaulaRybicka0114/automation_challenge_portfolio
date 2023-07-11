import time

import self as self

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"
    header_xpath = "//header"
    main_page_button_xpath = "//*/ul[1]/div[1]"
    players_button_xpath = "//*/ul[1]/div[2]"
    changing_language_button_xpath = "//*/ul[2]/div[1]"
    sign_out_button_xpath = "//*/ul[2]/div[2]"
    players_count_xpath = "//*/main/div[2]/div[1]/div"
    matches_count_xpath = "//*/main/div[2]/div[2]"
    reports_count_xpath = "//*/main/div[2]/div[3]"
    events_count_xpath = "//*/main/div[2]/div[4]"
    scouts_panel_img_xpath = "//*[@title='Logo Scouts Panel']"
    scouts_panel_title_xpath = "//h2[text()='Scouts Panel']"
    scouts_panel_description_xpath = "//p"
    dev_team_contact_button_xpath = "//*/div[3]/a"
    shortcuts_headline_xpath = "//h2[text()='Shortcuts']"
    add_player_button_xpath = "//*/div[2]/div/div/a/button"
    activity_headline_xpath = "//h2[text()='Activity']"
    last_created_player_description_xpath = "//h6[text()='Last created player']"
    last_created_player_button_xpath = "//*/div[3]/div/div/a[1]/button"
    last_updated_player_description_xpath = "//h6[text()='Last updated player']"
    last_updated_player_button_xpath = "//*/div[3]/div/div/a[2]/button"
    last_created_match_description_xpath = "//h6[text()='Last created match']"
    last_created_match_button_xpath = "//*/div[3]/div/div/a[3]/button"
    last_updated_match_description_xpath = "//h6[text()='Last updated match']"
    last_updated_match_button_xpath = "//*/div[3]/div/div/a[4]/button"
    last_updated_report_description_xpath = "//h6[text()='Last updated report']"
    last_updated_report_button_xpath = "//*/div[3]/div/div/a[5]/button"
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"
    add_player_form_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player(self):
        time.sleep(5)
        self.click_on_the_element(self.add_player_button_xpath)