# standard library imports
import os

# local library imports

# external library imports
from selenium import webdriver
import configparser

# this opens and reads config file with settings
config_parser = configparser.RawConfigParser()
config_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "config.ini")
config_parser.read_file(open(config_file_path))

# HARDCODED ENVIRONMENT VALUES
web_driver = 'FIREFOX'
environment = 'DEV'


class EnvironmentData:

    # WEB DRIVER
    if web_driver == 'FIREFOX':
        driver = webdriver.Firefox()
    elif web_driver == 'CHROME':
        directory = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
        chrome_driver_path = directory + "\\resources\\drivers\\chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver_path)
    else:
        raise NameError('Wrong driver value. ')

    if environment == "DEV":
        # WEB APP
        app_url = config_parser.get('dev', 'app-url')
        app_username = config_parser.get('dev', 'app-username')
        app_password = config_parser.get('dev', 'app-password')

    elif environment == "STAG":
        # WEB APP
        app_url = config_parser.get('stag', 'app-url')
        app_username = config_parser.get('stag', 'app-username')
        app_password = config_parser.get('stag', 'app-password')
    else:
        print("Wrong environment value ...")


