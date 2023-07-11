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
    leg_label_xpath = "//label[text()='Leg']"
    leg_input_xpath = "//div[8]/div/div/input"
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
    laczy_nas_pilka_label_xpath = "//label[text()='Łączy nas piłka']"
    laczy_nas_pilka_input_xpath = "//div[16]/div/div/input"
    90_minut_label_xpath = "//label[text()='90 minut']"
    90_minut_input_xpath = "//div[17]/div/div/input"
    facebook_label_xpath = "//label[text()='Facebook']"
    facebook_input_xpath = "//div[18]/div/div/input"
    add_link_to_youtube_button_xpath = "//div[19]/button"
    submit_button_xpath = "//*/div[3]/button[1]"
    clear_button_xpath = "//*/div[3]/button[2]"
pass