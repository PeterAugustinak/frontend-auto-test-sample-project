# standard library imports
import time
import datetime
import inspect

# 3rd party library imports
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

# local library imports
from data.EnvironmentData import EnvironmentData as Env

driver = Env.driver


class ElementEngine:

    @staticmethod
    def custom_click(locator, timeout=60):
        """ Wait until webelement is not stale.
        @param webelement: A selenium webdriver webelement
        """

        element = ElementEngine.wait_until_element_displayed(locator)

        start_time = time.time()
        while (time.time() - start_time) <= timeout:
            if ElementEngine.is_element_stale(element):
                element = ElementEngine.wait_until_element_displayed(locator)
            else:
                element.click()
                break

    @staticmethod
    def is_element_stale(webelement):
        """ Checks if a webelement is stale.
        @param webelement: A selenium webdriver webelement
        """
        try:
            webelement.tag_name
        except StaleElementReferenceException:
            return True
        except:
            pass

        return False

    @staticmethod
    def wait_until_element_present(locator):
        try:
            element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise

    @staticmethod
    def wait_until_element_displayed(locator, timeout=30):
        try:
            element = WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            raise

    @staticmethod
    def wait_until_num_of_elements_lower_than(locator, lower_than_value, timeout=150):
        start_time = time.time()
        while (time.time() - start_time) <= timeout:
            if len(ElementEngine.get_all_elements(locator)) < lower_than_value:
                return True

        raise TimeoutException("Timeout for waiting for elements.")

    @staticmethod
    def get_all_elements(locator):
        try:
            return driver.find_elements(*locator)
        except:
            time.sleep(3)
            try:
                return driver.find_elements(*locator)
            except:
                time.sleep(3)
                return driver.find_elements(*locator)
