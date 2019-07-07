# This are app locators for User Management menu

# 3rd party library imports
from selenium.webdriver.common.by import By


class LocatorsUserManagement:

    um_users_menu = (By.XPATH, '//*[@id="menu_admin_viewSystemUsers"]')
    um_text_field_username = (By.XPATH, '//*[@id="searchSystemUser_userName"]')
    um_button_search = (By.XPATH, '//*[@id="searchBtn"]')

    # table locators
    # um_table = (By.XPATH, '//table[@id="resultTable"]')
    um_table = '//table[@id="resultTable"]'
    um_table_by_id = (By.ID, 'resultTable')
    um_table_row = (By.TAG_NAME, "tr")
    um_table_col = (By.TAG_NAME, "td")

    @staticmethod
    def um_table_position(column_name='Username', row_number=1):

        if column_name == 'checkbox': column_number = 1
        elif column_name == 'Username': column_number = 2
        elif column_name == 'User Role': column_number = 3
        elif column_name == 'Employee Name': column_number = 4
        elif column_name == 'Status': column_number = 5
        else:
            column_number = 0

        um_table_position = (By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr['
                             f'{row_number}]/td[{column_number}]')
        return um_table_position

    um_table_position_alt = (By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td')


