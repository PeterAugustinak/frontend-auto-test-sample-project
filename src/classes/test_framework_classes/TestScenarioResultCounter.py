# This the counter for particular Test Scenarios

# local library imports
from data.TestFrameworkEnvironmentData import TestFrameworkEnvironmentData as Env


class TestScenarioResultCounter:
    """
    This class increments overall result and overall tested Test Cases for every rule sent to this function
    """

    @staticmethod
    def test_scenario_result(test_scenario):

        # this result is list of [1/0 from rule evaluation] + [number of test cases tested within this rule]
        result = test_scenario.test_case_runner()

        # this set variables as global and then increment overall_pass and overal_tc to global variables
        Env.overall_pass = Env.overall_pass + result[0]

        Env.overall_tc = Env.overall_tc + result[1]

        return [Env.overall_pass, Env.overall_tc]

