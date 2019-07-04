# This are app locators for User Management menu

# 3rd party library imports
from selenium.webdriver.common.by import By


class LocatorsUserManagement:

    um_users_menu = (By.XPATH, '//*[@id="menu_admin_viewSystemUsers"]')
    um_text_field_username = (By.XPATH, '//*[@id="searchSystemUser_userName"]')
    um_button_search = (By.XPATH, '//*[@id="searchBtn"]')
    um_table_username_firstrow = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr[1]/td[2]')

    @staticmethod
    def um_table_position_xpath(table_col='Username', table_row=1):

        if table_col == 'Username': table_col = 2
        if table_col == 'User Role': table_col = 3
        if table_col == 'Employee Name': table_col = 4
        if table_col == 'Status': table_col = 5

        um_table = (By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr[{table_row}]/td[{table_col}]')
        return um_table

    um_table_alt = (By.XPATH, f'/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody/tr/td')


