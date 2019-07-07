# This is universal Test Suite Runner for 'FESP' project

# standard library imports
from datetime import datetime

# local application imports
from data.EnvironmentData import EnvironmentData as Env
from data.TestFrameworkEnvironmentData import TestFrameworkEnvironmentData as Tenv

from classes.test_framework_classes.TestServiceAvailability import TestServicesAvailability as TestService
from classes.test_framework_classes.TestSuiteInitialSetup import TestSuiteInitialSetup as Tsis

# 3rd party library imports
from colorama import Fore, init
# initialization of colorama plugin
init()

# TEST SUITE IMPORTS
if Env.test_suite == 'test_suite_fesp_01_admin':
    from test_suits.test_suite_fesp_01_admin import TestSuite as Ts
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

        print(f"{Fore.YELLOW}SERVICES CHECK FOR {Env.environment} ENVIRONMENT STARTS:{Fore.RESET}")
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
            print(f"{Fore.YELLOW}TESTING FOR {Env.project_name} PROJECT HAS BEEN STARTED AT"
                  f" {datetime.now().strftime('%d-%m-%Y, %H:%M:%S')}!{Fore.RESET}")
            print(f"Environment: {Env.environment}")
            print(f"Test Suite: {Ts.test_suite_name}")
            print(f"All below Test Scenarios with all details can be find here:")
            print(f'{Fore.BLUE}{Ts.test_scenario_list_doc}{Fore.RESET}')
            print("*************************************************************")
            print()

            # now starts initialization of test suite and entire process of test suite testing
            Tsis.test_suite_initial_setup(Ts)

            # closing screen
            print(f"TESTING FOR {Env.project_name}/{Ts.test_suite_name} ON {Env.environment} FINISHED AT "
                  f"{datetime.now().strftime('%d-%m-%Y, %H:%M:%S')}")
            print()
        else:  # test suite was not found and not imported
            print(f"{Fore.RED}Test Suite not found. Automation Testing Aborted.{Fore.RESET}")
            from classes.web_classes.BrowserEngine import BrowserEngine as Be
            Be.close_browser()


if __name__ == '__main__':
    TestSuiteRunner.services_check()
