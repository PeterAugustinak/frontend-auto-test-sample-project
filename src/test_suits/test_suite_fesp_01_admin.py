# this is app_user_management test suite for frontend-auto-test-sample-project project

# test scenario imports
from test_suits.test_scenarios_for_test_suite_01.ts_fesp_01_user_search import TestScenario as ts_01_user_search


class TestSuite:

    test_suite_name = 'TEST SUITE 01 ADMIN'
    test_scenario_list_doc = 'https://bit.ly/2L6fnqK'

    """
    list of test scenarios to be tested in format:
        [imported_test_scenario_name, [can be tested on DEV -> "DEV", can be tested on STAG -> "STAG"]],
    """

    test_scenario_list = [
        [ts_01_user_search, ["DEV", ]],
        # [TS_02_job_titles, ["DEV", "STAG"]],
        # ...
    ]

