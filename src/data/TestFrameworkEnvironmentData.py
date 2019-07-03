# These are data manipulated and used by test framework


class TestFrameworkEnvironmentData:

    # global used lists
    data_list = []
    data_new_list = []
    failed_list = []
    current_element = ""

    # global used lists and general lists for test cases/test scenarios count
    total_failed_test_cases = []
    overall_pass = 0
    overall_tc = 0
    overall_result = ""

    # style scheme for log output
    stlfail = 'red'
    stlpass = 'green'
    stlts = 'yellow'
    stlimportant = 'red'
    stlbold = 'bold'
    stlundr = 'underline'
