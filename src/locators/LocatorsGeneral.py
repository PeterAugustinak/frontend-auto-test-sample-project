# 3rd party library imports
from selenium.webdriver.common.by import By


class LocatorsGeneral:

    # login page
    email_field = (By.XPATH, '//*[@id="txtUsername"]')
    password_field = (By.XPATH, '//*[@id="txtPassword"]')
    login_button = (By.XPATH, '//*[@id="btnLogin"]')

    # main page
    panel_wrapper = (By.XPATH, '//*[@id="panel_wrapper_1"]')
    welcome_admin_menu = (By.XPATH, '//*[@id="welcome"]')
    menu_panel = (By.XPATH, '/html/body/div[1]/div[2]')
    logout_item = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/ul/li[2]/a')

    # main page menu
    menu_admin = (By.XPATH, '/html/body/div[1]/div[2]/ul/li[1]/a/b')
    menu_user_management = (By.XPATH, '//*[@id="menu_admin_UserManagement"]')


