# This class handles navigation to and operation in User Management menu

# standard library imports
import time

# local library imports
from data.EnvironmentData import EnvironmentData as Env

from locators.LocatorsGeneral import LocatorsGeneral as Lg
from locators.LocatorsUserManagement import LocatorsUserManagement as Lum


from classes.web_classes.BrowserEngine import BrowserEngine
from classes.web_classes.ElementEngine import ElementEngine as Ee

#tentative imports
from classes.web_classes.AppLogin import AppLogin


class AdminUserManagement:

    @staticmethod
    def navigate_to_admin():
        # click on Admin item in menu
        Ee.custom_click(Lg.menu_admin)
        print("nav to admin done")
        time.sleep(1)

    @staticmethod
    def navigate_to_user_management():
        # click on User Management menu
        Ee.custom_click(Lg.menu_user_management)
        time.sleep(1)

    @staticmethod
    def navigate_to_users():
        # click on Users menu
        Ee.custom_click(Lum.um_users_menu)

    # navigation directly from Home screen to Users
    @classmethod
    def direct_navigate_users(cls):
        cls.navigate_to_admin()
        cls.navigate_to_user_management()
        # cls.navigate_to_users()
        Ee.wait_until_element_displayed(Lum.um_button_search)

    @staticmethod
    def search_by_username(username):
        # click to Username field, clear field and input value
        user_name_field = Ee.wait_until_element_displayed(Lum.um_text_field_username)
        user_name_field.clear()
        user_name_field.send_keys(username)

        # click to search button
        Ee.custom_click(Lum.um_button_search)

    @staticmethod
    def check_table(table_col, table_row):
        # create xpath with custom table position
        um_table_custom_position = Lum.um_table_position_xpath(table_col, table_row)
        value = Ee.get_text_from_displayed_element(um_table_custom_position)
        return value


# BrowserEngine.open_url(Env.app_url)
# time.sleep(2)
# AppLogin.login(Env.app_username, Env.app_password)
# time.sleep(2)
# AdminUserManagement.direct_navigate_users()
# time.sleep(2)
# print(AdminUserManagement.check_table('Username', 4))
# print(AdminUserManagement.check_table('User Role', 2))
# print(AdminUserManagement.check_table('Employee Name', 1))
# print(AdminUserManagement.check_table('Status', 1))


# AdminUserManagement.search_by_username('blabla')
# time.sleep(5)
# AdminUserManagement.search_by_username('3333')
# time.sleep(5)
# AppLogin.logout()
# BrowserEngine.close_browser()



