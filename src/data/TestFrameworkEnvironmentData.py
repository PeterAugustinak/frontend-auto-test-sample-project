# These are data manipulated and used by test framework

# 3rd party imports
from colorama import Fore


class TestFrameworkEnvironmentData:

    # global used elements
    test_suite_exist = 1

    # global used lists
    expected_data_list = []
    actual_data_list = []
    failed_list = []
    current_element = ""

    # global used lists and general lists for test cases/test scenarios count
    total_failed_test_cases = []
    overall_pass = 0
    overall_tc = 0
    overall_result = ""

    # style scheme for log output
    ok = f"{Fore.GREEN}OK{Fore.RESET}"
    fail = f"{Fore.RED}FAIL{Fore.RESET}"
    unavailable = f"{Fore.RED}UNAVAILABLE{Fore.RESET}"
    passed = f"{Fore.GREEN}PASSED: {Fore.RESET}"
    failed = f"{Fore.RED}FAILED: {Fore.RESET}"
