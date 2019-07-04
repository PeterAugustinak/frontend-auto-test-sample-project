# This is initialization of Test Suite and start of the entire process of testing

# local library imports
from data.EnvironmentData import EnvironmentData as Env
from data.TestFrameworkEnvironmentData import TestFrameworkEnvironmentData as Tenv
from classes.web_classes.BrowserEngine import BrowserEngine as Be
from classes.web_classes.AppLogin import AppLogin as Al
from classes.test_framework_classes.TestScenarioResultCounter import TestScenarioResultCounter as Tsrc
from classes.test_framework_classes.TestEvaluation import TestEvaluation as Evaluation


class TestSuiteInitialSetup:

    @classmethod
    def test_suite_initial_setup(cls):

        # open browser
        Be.open_url(Env.app_url)

        if Env.test_suite == 'test_suite_01_admin':
            from test_suits.test_suite_01_admin import TestSuite as Ts
            from classes.web_classes.AppAdminUserManagement import AdminUserManagement as Aum

            print(colored("All below Test Scenarios with all details can be find here:", Tenv.stlts))
            print(f'{Tenv.test_suite_catalogue}')

            # login into APP
            Al.login(Env.app_username, Env.app_password)
            # navigate to Admin
            Aum.navigate_to_admin()

        else:
            Tenv.test_suite_name = 'Test Suite name not found'
            Tenv.test_suite_catalogue = 'Test Suite Catalogue does not found'

        Tenv.test_suite_name = Ts.test_suite_name
        Tenv.test_suite_catalogue = Ts.test_suite_catalogue

        # start method for running data of Test Suite
        cls.test_data_runner(Ts.test_scenario_list)

        # logout from APP
        Al.logout()
        # close browser
        Be.close_browser()

    @staticmethod
    def test_data_runner(test_scenario_list):
        """
        This method at first set data for current sport, then reads Test Scenarios according to called sport value and
        entity value and also updates Jira results by calling UpdateJira class. In the end sets origin data back.
        """
        # initiation of list with result of each tested test scenario
        test_scenario_result_list = []

        # take every test scenario from imported list
        # example: [ts_01_foo ["DEV", "STAG"]]
        for test_scenario in test_scenario_list:
            if Env.environment in test_scenario[1]:  # check if has "DEV"/"STAG" value. If true, continue with run this
                # test scenario (ex. test_scenario[0] -> ts_01_foo) and add returned value into result list (0/1)
                test_scenario_result_list.append(Tsrc.test_scenario_result(test_scenario[0]))

        # method for evaluation of the every test suite based on test_scenario_result_list is called here
        Evaluation.test_suite_eval(test_scenario_result_list)
