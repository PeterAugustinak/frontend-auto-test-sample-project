# This class handles navigation to and operation in User Management menu

# standard library imports
import time

# local library imports
from locators.LocatorsGeneral import LocatorsGeneral as Lg
from locators.LocatorsUserManagement import LocatorsUserManagement as Lum

from classes.web_classes.ElementEngine import ElementEngine as Ee


class AdminUserManagement:

    @staticmethod
    def navigate_to_admin():
        # click on Admin item in menu
        Ee.custom_click(Lg.menu_admin)
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
    def check_table_position(table_col, table_row):
        # looking for exact position in table based on col and row
        um_table_position = Lum.um_table_position(table_col, table_row)
        # alternative link to table value in case there is no position based on col and row
        um_table_position_alt = Lum.um_table_position_alt

        value = Ee.get_text_from_displayed_element_special(um_table_position, um_table_position_alt)
        return value
