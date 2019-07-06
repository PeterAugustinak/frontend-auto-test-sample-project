# this is universal TestSuiteRunner for 'FRONTEND AUTO TEST SAMPLE PROJECT'

# standard library imports
from datetime import datetime

# local application imports
from data.EnvironmentData import EnvironmentData as Env
from data.TestFrameworkEnvironmentData import TestFrameworkEnvironmentData as Tenv

from classes.test_framework_classes.TestServiceAvailability import TestServicesAvailability as TestService
from classes.test_framework_classes.TestSuiteInitialSetup import TestSuiteInitialSetup as Tsis

# 3rd party library imports
from colorama import Fore, Style, init
init()

# test suite imports
if Env.test_suite == 'test_suite_01_admin':
    from test_suits.test_suite_01_admin import TestSuite as Ts
else:
    Tenv.test_suite_exist = 0


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

        print(f"{Style.BRIGHT}SERVICES CHECK FOR {Env.environment} ENVIRONMENT STARTS:{Style.RESET_ALL}")
        service_check = TestService.test_service_runner()
        print("*************************************************************")
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

        if Tenv.test_suite_exist:  # test suite was correctly imported
            # introductory screen
            print(f"{Style.BRIGHT}TESTING FOR {Env.project_name} HAS BEEN STARTED AT {datetime.now().strftime('%d-%m-%Y, %H:%M:%S')}!{Style.RESET_ALL}")
            print(f"Environment: {Env.environment}")
            print(f"Test Suite: {Ts.test_suite_name}")
            print(f"All below Test Scenarios with all details can be find here:")
            print(f'{Fore.BLUE}{Ts.test_suite_catalogue}{Fore.RESET}')
            print("*************************************************************")
            print()

            # now starts initialization of test suite and entire process of test suite testing
            Tsis.test_suite_initial_setup(Ts)

            # closing screen
            print(f"TESTING FOR {Env.project_name} - {Ts.test_suite_name} ON {Env.environment} FINISHED AT "
                  f"{datetime.now().strftime('%d-%m-%Y, %H:%M:%S')}")
            print()
        else:  # test suite was not found and not imported
            print("Test Suite not found. Automation Testing Aborted.")
            from classes.web_classes.BrowserEngine import BrowserEngine as Be
            Be.close_browser()


if __name__ == '__main__':
    TestSuiteRunner.services_check()
