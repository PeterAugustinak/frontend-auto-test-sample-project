# this is universal Test Suite Runner for every test suite within VISMA-FRONTEND-TEST project

# standard library imports
from datetime import datetime

# 3rd party library imports
from termcolor import colored

# local application imports
from data.EnvironmentData import EnvironmentData as Env
from data.TestFrameworkEnvironmentData import TestFrameworkEnvironmentData as Tenv

from classes.test_framework_classes.TestServiceAvailability import TestServicesAvailability as TestService
from classes.test_framework_classes.TestSuiteInitialSetup import TestSuiteInitialSetup as Tsis


project_name = 'VISMA-FRONTEND-TEST'


class TestSuiteRunner:
    """
    This class handles running of Test Suite for particular sport and entity.
    """

    @classmethod
    def services_check(cls):
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
            cls.test_suite_runner()
        else:
            Tenv.overall_result = "FAIL!"

    @staticmethod
    def test_suite_runner():
        """
        This method brings introductory and closing screen with basic information and calls test_data_runner method for
        running particular scenarios.
        """

        # introductory screen
        print(colored(f"TESTING FOR {project_name} - {Tenv.test_suite_name} HAS BEEN STARTED"
                      f" AT {datetime.now().strftime('%d-%m-%Y, %H:%M:%S')}!", attrs=[Tenv.stlbold]))
        print("Environment: " + colored(Env.environment, attrs=[Tenv.stlbold]))
        print(colored("All below Test Scenarios with all details can be find here:", Tenv.stlts))
        print(f'{Tenv.test_suite_catalogue}')
        print("***************************************************")
        print()

        # now starts initialization of test suite and entire process of test suite testing
        Tsis.test_suite_initial_setup()

        # closing screen
        print(colored(f"TESTING FOR {project_name} - {Tenv.test_suite_name} ON {Env.environment} FINISHED"
                      f" AT {datetime.now().strftime('%d-%m-%Y, %H:%M:%S')}", attrs=[Tenv.stlbold]))
        print()


if __name__ == '__main__':
    TestSuiteRunner.services_check()
