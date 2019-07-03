# this is app_user_management test suite for visma-frontend-test project

# test scenario imports
from test_suits.test_scenarios_for_test_suite_01.ts_01_user_table_row_check import TestScenario as ts_01_user_table_row


class TestSuite:
    test_suite_name = 'APP USER MANAGEMENT'

    """
    list of test scenarios to be tested in format:
        [imported_test_scenario_name, [can be tested on DEV -> "DEV", can be tested on STAG -> "STAG"]],
    """

    test_scenario_list = [
        [ts_01_user_table_row, ["DEV", ]],
        # [TS_02_user_table_filter, ["DEV", "STAG"]],
        # ...
    ]

