# local library imports
from data.TestFrameworkEnvironmentData import TestFrameworkEnvironmentData as Tenv


class TestCaseCompare:

    @staticmethod
    def compare_test_case_result(data_list, data_new_list):
        """
        This method compares values received from execution method of particular test scenarios.
        """

        if_passed = 1
        for data in data_list:
            for data_new in data_new_list:
                if int(data) == int(data_new):
                    continue
                else:
                    if_passed = 0
                    Tenv.failed_list.append(Tenv.current_element)
                    continue

        # empty global lists for data / data_new
        Tenv.data_list = []
        Tenv.data_new_list = []

        return [if_passed, data_list, data_new_list]
