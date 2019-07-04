# This compares data from particular trest cases

# local library imports
from data.TestFrameworkEnvironmentData import TestFrameworkEnvironmentData as Tenv


class TestCaseCompare:

    @staticmethod
    def compare_test_case_result(expected_data_list, actual_data_list):
        """
        This method compares values received from execution method of particular test scenarios.
        """

        if_passed = 1
        for expected_data in expected_data_list:
            for actual_data in actual_data_list:
                if expected_data == actual_data:
                    continue
                else:
                    if_passed = 0
                    Tenv.failed_list.append(Tenv.current_element)
                    continue

        # empty global expected / actual data lists
        Tenv.actual_data = []
        Tenv.data_new_list = []

        return [if_passed, expected_data_list, actual_data_list]
