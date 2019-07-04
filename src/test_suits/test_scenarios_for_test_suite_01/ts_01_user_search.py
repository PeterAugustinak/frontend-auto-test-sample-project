# this is Test Scenario ts_01_user_table_row_check

# local library imports
from data.EnvironmentData import EnvironmentData as Env
from data.TestFrameworkEnvironmentData import TestFrameworkEnvironmentData as Tenv
from classes.test_framework_classes.TestCaseCompare import TestCaseCompare as Tc
from classes.test_framework_classes.TestEvaluation import TestEvaluation as Te
from classes.web_classes.BrowserEngine import BrowserEngine as Be
from classes.web_classes.AppLogin import AppLogin as Al
from classes.web_classes.AppAdminUserManagement import AdminUserManagement as Aum

# 3rd party library imports


class TestScenario:

    # general information of the Test Scenario
    title = 'TEST SCENARIO 01 USER SEARCH: '
    description = ' Test if specific user is present in table of user list'
    details = ''

    # display information about particular test scenario
    print(title)
    print(description)
    print(f" Details: {details}")
    print()

    # TEST CASES
    '''
    TEST CASE EXPLANATION:
    Every particular test case is list, consists from:
         [
            description of the test case,
            [list of INPUT VALUES],
            [list of EXPECTED VALUES],
         ],
    '''

    test_cases_list = [
        # 01
        [
            'Test for search of existing users: ',
            ['Admin', 'fiona.grace', 'hannah.flores'],
            ['', 'Fiona Grace', 'Hannah Flores']
        ],

        # 02
        [
            'Test for search non existing useres: ',
            ['Peter', 'Rafael', 'Tadas'],
            ['No Records Found']
        ]
    ]

    # runner method for start scenario and to create particular test cases
    @classmethod
    def test_case_runner(cls):
        # initialization of list with test cases result and numbering of particular tested test case
        test_cases_result_list = []
        test_case_number = 1

        # loop through every test of given test scenario
        for test_case in cls.test_cases_list:

            # just small hack for better displaying test cases numbering (adding 0 for tc`s lower than 10)
            if test_case_number < 10:
                test_case_number_prnt = f"0{test_case_number}"
            else:
                test_case_number_prnt = f"{test_case_number}"

            # test_case[0]: description
            # test_case[1]: input_data_list
            # test_case[2]: expected_data_list
            result_test_case = [cls.test_case_execution(test_case[1], test_case[2]),
                                f"Test Case {test_case_number_prnt}: {test_case[0]}"]

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
    def test_case_execution(input_data_list, expected_data_list):

        Tenv.expected_data_list = expected_data_list

        # search users by Username
        for user in input_data_list:
            # check value in result table
            Aum.search_by_username(user)
            current_data = Aum.check_table('Employee Name', 1)
            Tenv.actual_data_list.append(current_data)

        return Tc.compare_test_case_result(Tenv.expected_data_list, Tenv.actual_data_list)
