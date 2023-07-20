import time

from pages.base_page import BasePage

class AddAPlayer(BasePage):
    header_xpath = "//header"
    main_page_button_xpath = "//*/ul[1]/div[1]"
    players_button_xpath = "//*/ul[1]/div[2]"
    changing_language_button_xpath = "//*/ul[3]/div[1]"
    sign_out_button_xpath = "//*/ul[3]/div[2]"
    form_header_xpath = "//form/div[1]/div/span"
    email_label_xpath = "//label[text()='E-mail']"
    email_input_xpath = "//div[1]/div/div/input"
    name_label_xpath = "//label[text()='Name']"
    name_input_xpath = "//div[2]/div/div/input"
    surname_label_xpath = "//label[text()='Surname']"
    surname_input_xpath = "//div[3]/div/div/input"
    phone_label_xpath = "//label[text()='Phone']"
    phone_input_xpath = "//div[4]/div/div/input"
    weight_label_xpath = "//label[text()='Weight']"
    weight_input_xpath = "//div[5]/div/div/input"
    height_label_xpath = "//label[text()='Height (cm)']"
    height_input_xpath = "//div[6]/div/div/input"
    age_label_xpath = "//label[text()='Age']"
    age_input_xpath = "//div[7]/div/div/input"
    age_required_label_xpath = "//div[7]/div/p"
    leg_label_xpath = "//label[text()='Leg']"
    leg_dropdown_button = "//*[@id='mui-component-select-leg']"
    right_leg_xpath = "//div[3]/ul/li[1]"
    left_leg_xpath = "//div[3]/ul/li[2]"
    club_label_xpath = "//label[text()='Club']"
    club_input_xpath = "//div[9]/div/div/input"
    level_label_xpath = "//label[text()='Level']"
    level_input_xpath = "//div[10]/div/div/input"
    main_position_label_xpath = "//label[text()='Main position']"
    main_position_input_xpath = "//div[11]/div/div/input"
    second_position_label_xpath = "//label[text()='Second position']"
    second_position_input_xpath = "//div[12]/div/div/input"
    district_input_xpath = "//div[13]/div/div/input"
    achievements_label_xpath = "//label[text()='Achievements']"
    achievements_input_xpath = "//div[14]/div/div/input"
    add_language_button_xpath = "//div[15]/button"
    languages_label_xpath = "//label[text()='Languages']"
    languages_input_xpath = "//div[15]/div/div/div/input"
    remove_language_button_xpath = "//div[15]/div/button"
    laczy_nas_pilka_label_xpath = "//label[text()='Łączy nas piłka']"
    laczy_nas_pilka_input_xpath = "//div[16]/div/div/input"
    ninety_minuts_label_xpath = "//label[text()='90 minut']"
    ninety_minuts_input_xpath = "//div[17]/div/div/input"
    facebook_label_xpath = "//label[text()='Facebook']"
    facebook_input_xpath = "//div[18]/div/div/input"
    add_link_to_youtube_button_xpath = "//div[19]/button"
    youtube_label_xpath = "//label[text()='YouTube']"
    youtube_input_xpath = "//div[19]/div/div/div/input"
    remove_link_to_youtube_button_xpath = "//div[19]/div/button"
    submit_button_xpath = "//*/div[3]/button[1]"
    clear_button_xpath = "//*/div[3]/button[2]"
    expected_text = "Required"

    def type_in_email(self, email):
        self.field_send_keys(self.email_input_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_input_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_input_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_input_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_input_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.height_input_xpath, height)

    def type_in_club(self, club):
        self.field_send_keys(self.club_input_xpath, club)

    def type_in_level(self, level):
        self.field_send_keys(self.level_input_xpath, level)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_input_xpath, main_position)

    def type_in_second_position(self, second_position):
        self.field_send_keys(self.second_position_input_xpath, second_position)

    def type_in_achievements(self, achievements):
        self.field_send_keys(self.achievements_input_xpath, achievements)

    def click_on_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def wait_for_required(self):
        self.visibility_of_element_located(self.age_required_label_xpath)

    def click_on_age(self):
        self.click_on_the_element(self.age_input_xpath)

    def click_clear(self):
        self.click_on_the_element(self.clear_button_xpath)

    def select_leg(self, leg):
        self.click_on_the_element(self.leg_dropdown_button)
        time.sleep(3)
        if leg == "right":
            self.click_on_the_element(self.left_leg_xpath)
        else:
            self.click_on_the_element(self.right_leg_xpath)

