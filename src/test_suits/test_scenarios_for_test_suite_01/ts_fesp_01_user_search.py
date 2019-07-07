# this is Test Scenario ts_01_user_search

# local library imports
from data.TestFrameworkEnvironmentData import TestFrameworkEnvironmentData as Tenv
from data.EnvironmentData import EnvironmentData as Env
from classes.test_framework_classes.TestCaseCompare import TestCaseCompare as Tc
from classes.test_framework_classes.TestEvaluation import TestEvaluation as Te
from classes.web_classes.AppAdminUserManagement import AdminUserManagement as Aum
from classes.general_classes.SpreadSheetReader import SpreadSheetReader as Ssr
from classes.web_classes.WebTableElement import WebTableElement as Wte
from locators.LocatorsUserManagement import LocatorsUserManagement as Lum

# 3rd party library imports
from colorama import Fore


class TestScenario:

    # data for spreadsheet reader
    ts_file_name = 'ts_fesp_admin_01_users'

    # TEST SCENARIO DATA
    # general information of the Test Scenario
    title = f'{Fore.YELLOW}{Ssr.read_ts_info(ts_file_name, 4, 3)}: {Fore.RESET}'
    description = f' Description: {Ssr.read_ts_info(ts_file_name, 5, 3)}'
    details = f' Details: {Fore.BLUE}{Ssr.read_ts_info(ts_file_name, 6, 3)}{Fore.RESET}'

    # TEST CASES
    '''
    TEST CASE EXPLANATION:
    Every particular test case is list, consists from:
         [
            type of test ('check', 'search', 'add' ...)
            description of the test case, read from scenario worksheet, col/row nr
            list of INPUT VALUES, - read from data worksheet, column nr
            list of EXPECTED VALUES - read from data worksheet, column nr,
            specific data for test case - in this scenario list of values of col/row to be checked
         ],
    '''

    test_cases_list = [
        # check - basic test cases for default values in the table
        # 01
        [
            'check',
            Ssr.read_ts_info(ts_file_name, 13, 5),
            Ssr.read_ts_data(ts_file_name, 1),
            Ssr.read_ts_data(ts_file_name, 2),
            ['checkbox', 1]
        ],

        # check - if user/data is present in the table by default
        # 03
        [
            'check',
            Ssr.read_ts_info(ts_file_name, 13, 6),
            Ssr.read_ts_data(ts_file_name, 3),
            Ssr.read_ts_data(ts_file_name, 4),
            []
        ],

        # search - test cases for searching values by filter
        # by Username
        # 03
        [
            'search',
            Ssr.read_ts_info(ts_file_name, 23, 5),
            Ssr.read_ts_data(ts_file_name, 5),
            Ssr.read_ts_data(ts_file_name, 6),
            ['Employee Name', 1]
        ],

    ]

    # runner method for start scenario and to create particular test cases
    @classmethod
    def test_case_runner(cls):

        # display information about particular test scenario
        print(cls.title)
        print(cls.description)
        print(cls.details)
        print()

        # initialization of list with test cases result and numbering of particular tested test case
        test_cases_result_list = []
        test_case_number = 1

        # loop through every test of given test scenario
        for test_case in cls.test_cases_list:

            # just small hack for better displaying test cases numbering (adding 0 for tc`s lower than 10)
            if test_case_number < 10:
                test_case_number_print = f"0{test_case_number}"
            else:
                test_case_number_print = f"{test_case_number}"

            # test_case[0]: type of test
            # test_case[1]: description
            # test_case[2]: input_data_list
            # test_case[3]: expected_data_list
            # test_case[4]: table_position
            result_test_case = [cls.test_case_execution(test_case[0], test_case[2], test_case[3], test_case[4]),
                                f"Test Case {test_case_number_print}: {test_case[1]}: "]

            # this calls method for evaluation of tested test case (for print evaluations only)
            Te.test_case_eval(result_test_case)

            # result of test case evaluation is added into test_cases_result list
            test_cases_result_list.append(result_test_case)

            # next test case number count
            test_case_number += 1

        test_cases_count = len(test_cases_result_list)

        '''
        - test_case_runner method returns list of results of all test cases within given scenario and test scenario title
        - it is powered by test_case_eval method
        '''

        return [Te.test_scenario_eval(test_cases_result_list), test_cases_count]

    @staticmethod
    def test_case_execution(type_of_test, input_data_list, expected_data_list, table_position):

        Tenv.expected_data_list = expected_data_list
        # table
        # table = Wte(Env.driver.find_element_by_xpath(Lum.um_table))
        column_name = table_position[0]
        row_number = table_position[1]

        # search users by Username
        for data in input_data_list:
            # check type of test and based on that decide what operation will be executed
            if type_of_test == 'search':
                # execute search by Username filter
                Aum.search_by_username(data)
            # check values in table
            current_data = Aum.check_table_position(column_name, row_number)
            Tenv.actual_data_list.append(current_data)

        return Tc.compare_test_case_result(Tenv.expected_data_list, Tenv.actual_data_list)
