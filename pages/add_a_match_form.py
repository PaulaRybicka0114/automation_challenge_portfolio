from pages.base_page import BasePage


class Dashboard(BasePage):
    header_xpath = "//header"
    main_page_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]"
    players_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]"
    player_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]"
    matches_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]"
    reports_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[3]"
    changing_language_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]"
    sign_out_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]"
    form_header_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[1]/div/span"
    submit_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]"
    clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]"
pass
