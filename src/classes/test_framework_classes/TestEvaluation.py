# These are methods for evaluation of particular test stage - test case, test scenario, test suite

# local library imports
from data.TestFrameworkEnvironmentData import TestFrameworkEnvironmentData as Tenv

# 3rd party libary imports
from colorama import Fore


class TestEvaluation:
    """
    This class evaluates every particular element of tests separately - test case, test scenario and entire test suite.
    """

    # evaluation of particular Test Case
    @staticmethod
    def test_case_eval(result_test_case):
        print(f" {result_test_case[1]}", end='')
        if result_test_case[0][0] == 0:
            print(Tenv.fail)
            for expected, actual in zip(result_test_case[0][1], result_test_case[0][2]):
                if expected != actual:
                    print(f"   Expected value: {expected}, Actual value: {actual}")
        elif result_test_case[0][0] == 1:
            print(Tenv.ok)
        else:
            print(" ERROR: Evaluation Failed ...")

        # this delete list of uuid`s after evaluation of particular Test Cases for whole test scenario is finished so
        # now is prepared empty for the next test scenario
        Tenv.failed_list = []

    # evaluation of particular Test Scenario
    @staticmethod
    def test_scenario_eval(test_cases_result_list):

        final_eval_list = []
        fail_result_list = []

        for test_case_result in test_cases_result_list:
            if test_case_result[0][0] == 1:
                final_eval_list.append(test_case_result[0][0])
            else:
                fail_result_list.append(1)
                Tenv.total_failed_test_cases.append(1)

        print()
        print(f" {Fore.YELLOW}RESULT ({len(test_cases_result_list)} Test Cases) ---> ", end="")
        f"{Fore.RESET}"
        if len(final_eval_list) == len(test_cases_result_list):
            print(Tenv.ok)
            print("----------------------------------------------")
            return 1

        else:
            print(Tenv.fail)
            print(f" Failed Test Cases: {len(fail_result_list)}")
            f"{Fore.RESET}"
            print("----------------------------------------------")
            return 0

    # evaluation of particular Test Suite
    @staticmethod
    def test_suite_eval(test_scenario_result_list):

        len_tested_scenarios = len(test_scenario_result_list)

        # if overall_PASS value is equal to number of Test Scenarios, Test Suite is evaluates as PASS as all
        # scenarios passed
        if not Tenv.overall_result:  # in case that overall_result is already set to FAIL because of cmd value
            # fail in SetEventEngine test
            if Tenv.overall_pass == len_tested_scenarios:
                Tenv.overall_result = "PASS!"
            else:
                Tenv.overall_result = "FAIL!"

        # OVERALL RESULT PRINT
        print()
        print(f"TEST SCENARIOS EXECUTED: {len_tested_scenarios} ({Tenv.overall_tc} Test Cases)")
        print()

        # count total failed test cases
        tot_fail_test_cases = len(Tenv.total_failed_test_cases)
        # count total passed test cases
        tot_pass_test_cases = Tenv.overall_tc - tot_fail_test_cases

        print(f"{Tenv.passed} {Tenv.overall_pass} ({tot_pass_test_cases} Test Cases)")

        # count overall failed test scenarios
        overall_fail = len_tested_scenarios - Tenv.overall_pass

        print(f"{Tenv.failed} {overall_fail} ({len(Tenv.total_failed_test_cases)} Test Cases)")

        # count passed ratio
        if tot_pass_test_cases == 0 and tot_fail_test_cases == 0:
            passed_ratio = "ERROR"
        elif tot_pass_test_cases == 0:
            passed_ratio = "0"
        elif tot_fail_test_cases == 0:
            passed_ratio = "100"
        else:
            passed_ratio = round((100 / Tenv.overall_tc) * tot_pass_test_cases, 2)

        print(f"PASSED TC's RATIO: {passed_ratio}%")
        if Tenv.overall_result == "PASS!":
            print(f"{Fore.GREEN}")
            print(f"OVERALL RESULT: {Tenv.overall_result}")
            print(Fore.RESET)
        else:
            print(f"{Fore.RED}")
            print(f"OVERALL RESULT: {Tenv.overall_result}")
            print(Fore.RESET)
