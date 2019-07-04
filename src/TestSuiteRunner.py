# this is universal Test Suite Runner for every test suite within VISMA-FRONTEND-TEST project

# standard library imports
from datetime import datetime
import os

# 3rd party library imports
from termcolor import colored

# local application imports
from data.EnvironmentData import EnvironmentData as Env
from data.TestFrameworkEnvironmentData import TestFrameworkEnvironmentData as Tenv

from classes.test_framework_classes.TestServiceAvailability import TestServicesAvailability as TestService
from classes.test_framework_classes.TestScenarioResultCounter import TestScenarioResultCounter as Tsrc
from classes.test_framework_classes.TestEvaluation import TestEvaluation as Evaluation

# test suite imports
from test_suits.test_suite_01_app_user_management import TestSuite as Ts

project_name = 'VISMA-FRONTEND-TEST'


class TestSuiteRunner:
    """
    This class handles running of Test Suite for particular sport and entity.
    """

    @staticmethod
    def services_check():
        """
        This method is starting all the Automation Test by checking of availability of all services necessary for
        executing particular tests.
        In case of all services are available, testing starts by calling test_suite_runner method.
        In case of some service is unavailable, test running are cancelled.
        """

        print(colored(f"SERVICES CHECK FOR {Env.environment} ENVIRONMENT STARTS:",
                      attrs=[Tenv.stlundr, Tenv.stlbold]))
        service_check = TestService.test_service_runner()
        print("*******************************************************")
        print()

        if service_check:
            TestSuiteRunner.test_suite_runner()
        else:
            Tenv.overall_result = "FAIL!"

    @staticmethod
    def test_suite_runner():
        """
        This method brings introductory and closing screen with basic information and calls test_data_runner method for
        running particular scenarios.
        """

        # introductory screen
        print(colored(f"TESTING FOR {project_name} - {Ts.test_suite_name} HAS BEEN STARTED"
                      f" AT {datetime.now().strftime('%d-%m-%Y, %H:%M:%S')}!", attrs=[Tenv.stlbold]))
        print("Environment: " + colored(Env.environment, attrs=[Tenv.stlbold]))
        print(colored("All below Test Scenarios with all details can be find here:", Tenv.stlts))
        print('... link to Test Catalogue will be added ...')
        print("***************************************************")
        print()

        # now is called method for listing up all the test scenarios and it`s data - core of the automation test
        TestSuiteRunner.test_data_runner()

        # closing screen
        print(colored(f"TESTING FOR {project_name} - {Ts.test_suite_name} ON {Env.environment} FINISHED"
                      f" AT {datetime.now().strftime('%d-%m-%Y, %H:%M:%S')}", attrs=[Tenv.stlbold]))
        print()

    @staticmethod
    def test_data_runner():
        """
        This method at first set data for current sport, then reads Test Scenarios according to called sport value and
        entity value and also updates Jira results by calling UpdateJira class. In the end sets origin data back.
        """
        # initiation of list with result of each tested test scenario
        test_scenario_result_list = []

        # take every test scenario from imported list
        # example: [ts_01_foo ["DEV", "STAG"]]
        for test_scenario in Ts.test_scenario_list:
            if Env.environment in test_scenario[1]:  # check if has "DEV"/"STAG" value. If true, continue with run this
                # test scenario (ex. test_scenario[0] -> ts_01_foo) and add returned value into result list (0/1)
                test_scenario_result_list.append(Tsrc.test_scenario_result(test_scenario[0]))

        # method for evaluation of the every test suite based on test_scenario_result_list is called here
        Evaluation.test_suite_eval(test_scenario_result_list)


if __name__ == '__main__':
    TestSuiteRunner.services_check()
