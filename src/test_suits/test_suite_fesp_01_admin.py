# This is Test Suite test_suite_fesp_01_admin for FESP project

# test scenario imports
from test_suits.test_scenarios_for_test_suite_01.ts_fesp_01_user_search import TestScenario as ts_01_user_search


class TestSuite:

    test_suite_name = 'TEST SUITE FESP 01 ADMIN'
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

