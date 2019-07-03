# this is Test Scenario ts_01_user_table_row_check

# local library imports
from data.EnvironmentData import EnvironmentData as Env
from data.TestFrameworkEnvironmentData import TestFrameworkEnvironmentData as Tenv
from classes.test_framework_classes.TestCaseCompare import TestCaseCompare as Tc
from classes.test_framework_classes.TestEvaluation import TestEvaluation as Tse

# 3rd party library imports
from termcolor import colored


class TestScenario:

    # test scenario data
    title = "TEST SCENARIO 01: USER TABLE ROW CHECK: "
    description = "Test if specific user is present in table of user list: "

    # runner method for start scenario and to create particular test cases
    @staticmethod
    def test_case_runner():

        """
        - test case engine is called by method test_case* method of Test Case class
        - this test compares totalCount value between elastic search and feed in xml, json and json-p format
        - iteration is set to create 1 Test Case for every index
        """

        # display introduction info to scenario
        print(colored(TestScenario.title, 'yellow', attrs=[Tenv.stlundr]))
        print(" Details: ")
        print(" *")

        # initialization of local lists / variables
        test_cases_result_list = []
        test_case_number = 1

        # create test cases based on data
        # test_case_01 - check for existing users
        # test_case_02 - check for non existing users

        print(" Test Case " + str(test_case_number) + ": index = [" +
              (colored(index, attrs=[Tenv.stlbold])) + "], " + TestScenario.description, end="")
        result_test_case = TestScenario.test_case_execution()
        Tse.test_case_eval(result_test_case)

        test_cases_result_list.append(result_test_case)
        test_case_number += 1

        test_cases_count = len(test_cases_result_list)

        return [Tse.test_scenario_eval(test_cases_result_list, TestScenario.title), test_cases_count]

    # execution method for above created test cases

    @staticmethod
    def test_case_execution():


        return Tc.compare_test_case_result(Tenv.data_list, Tenv.data_new_list)
