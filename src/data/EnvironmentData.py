# standard library imports
import os
import sys

# 3rd party library imports
from selenium import webdriver
import configparser

# this opens and reads config file with settings
config_parser = configparser.RawConfigParser()
config_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "config.ini")
config_parser.read_file(open(config_file_path))

driver = None


class EnvironmentData:

    # project name
    project_name = 'FRONTEND AUTO TEST SAMPLE PROJECT'

    # arguments for environment and web_driver
    test_suite = str(sys.argv[1])
    environment = str(sys.argv[2])
    web_driver = str(sys.argv[3])

    # WEB DRIVER
    if web_driver == 'FIREFOX':
        driver = webdriver.Firefox()
    elif web_driver == 'CHROME':
        driver = webdriver.Chrome()
    else:
        raise NameError('Wrong driver value.')

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


