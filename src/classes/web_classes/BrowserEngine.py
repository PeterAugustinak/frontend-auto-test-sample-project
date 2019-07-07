# This is the Browser Engine for operating with browsers and urls

# local library imports
from data.EnvironmentData import EnvironmentData as Env


class BrowserEngine:
    driver = Env.driver

    @classmethod
    def open_url(cls, url):
        cls.open_browser()
        cls.driver.get(url)

    @classmethod
    def open_browser(cls):
        cls.driver.implicitly_wait(0.5)
        cls.driver.maximize_window()

    @classmethod
    def close_browser(cls):
        cls.driver.quit()
