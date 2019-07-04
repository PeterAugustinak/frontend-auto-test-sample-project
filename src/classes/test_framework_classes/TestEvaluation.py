# these are methods for evaluation of particular test stage - test case, test scenario, test suite

from data.TestFrameworkEnvironmentData import TestFrameworkEnvironmentData as Tenv
from termcolor import colored


class TestEvaluation:
    """
    This class evaluates every particular element of tests separately - test case, test scenario and entire test suite.
    """

    # evaluation of particular Test Case
    @staticmethod
    def test_case_eval(result_test_case):
        print(f" {result_test_case[1]}", end='')
        if result_test_case[0][0] == 0:
            print(f" FAIL")
            for expected, actual in zip(result_test_case[0][1], result_test_case[0][2]):
                if expected != actual:
                    print(f"   Expected value: {expected}, Actual value: {actual}")
        elif result_test_case[0][0] == 1:
            print(" OK")
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

        print("  *")
        print(colored(f" RESULT ({len(test_cases_result_list)} Test Cases) ---> ", 'yellow'), end="")
        if len(final_eval_list) == len(test_cases_result_list):
            print(colored("OK", 'green'))
            print("--------------------------------------------")
            return 1

        else:
            print(colored("FAIL", 'red'))
            print(colored(f" Failed Test Cases: {len(fail_result_list)}", 'red'))
            print("--------------------------------------------")
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
                Tenv.overall_result = colored("PASS!", Tenv.stlpass, attrs=[Tenv.stlbold,
                                                                            Tenv.stlundr])
                Tenv.jira_result = "PASS"
            else:
                Tenv.overall_result = colored("FAIL!", Tenv.stlfail, attrs=[Tenv.stlbold,
                                                                            Tenv.stlundr])
                Tenv.jira_result = "FAIL"
        else:
            Tenv.jira_result = "FAIL"

        # OVERALL RESULT PRINT
        print()
        print(f"TEST SCENARIOS EXECUTED: {len_tested_scenarios} ({Tenv.overall_tc} Test Cases)")
        print()

        # count total failed test cases
        tot_fail_test_cases = len(Tenv.total_failed_test_cases)
        # count total passed test cases
        tot_pass_test_cases = Tenv.overall_tc - tot_fail_test_cases

        print(colored(f"PASSED: {Tenv.overall_pass} ({tot_pass_test_cases} Test Cases)", Tenv.stlpass))

        # count overall failed test scenarios
        overall_fail = len_tested_scenarios - Tenv.overall_pass

        print(colored(f"FAILED: {overall_fail} ({len(Tenv.total_failed_test_cases)} Test Cases)", Tenv.stlfail))

        # count passed ratio
        if tot_pass_test_cases == 0 and tot_fail_test_cases == 0:
            passed_ratio = "ERROR"
        elif tot_pass_test_cases == 0:
            passed_ratio = "0"
        elif tot_fail_test_cases == 0:
            passed_ratio = "100"
        else:
            passed_ratio = round((100 / Tenv.overall_tc) * tot_pass_test_cases, 2)

        print(colored(f"PASSED RATIO: {passed_ratio}%", attrs=[Tenv.stlbold]))
        print()
        print(colored("OVERALL RESULT: ", attrs=[Tenv.stlbold, Tenv.stlundr]), end="")
        print(Tenv.overall_result)
        print()

