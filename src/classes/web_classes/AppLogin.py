# This class log into and log out from the App

# standard library imports
import time

# local library imports
from locators.LocatorsGeneral import LocatorsGeneral as Agl
from classes.web_classes.ElementEngine import ElementEngine as Ee


class AppLogin:

    @staticmethod
    def login(username, password):
        # email
        email_field = Ee.wait_until_element_displayed(Agl.email_field)
        email_field.clear()
        email_field.send_keys(username)

        # password
        password_field = Ee.wait_until_element_displayed(Agl.password_field)
        password_field.clear()
        password_field.send_keys(password)

        # click to login button
        Ee.custom_click(Agl.login_button)

        # wait until logout button is displayed
        Ee.wait_until_element_displayed(Agl.panel_wrapper)

    @staticmethod
    def logout():
        # open Welcome Admin menu and click to Logout item
        Ee.custom_click(Agl.welcome_admin_menu)
        Ee.custom_click(Agl.logout_item)

        # wait until Login button on login page is displayed
        Ee.wait_until_element_displayed(Agl.login_button)


# BrowserEngine.open_url(Env.app_url)
# time.sleep(2)
# AppLogin.login(Env.app_username, Env.app_password)
# time.sleep(2)
# AppLogin.logout()
# time.sleep(2)
# BrowserEngine.close_browser()



