# This is service availability check for FRONTEND AUTO TEST SAMPLE PROJECT project

# 3rd party library imports
import requests
from colorama import Fore

# local library imports
from data.EnvironmentData import EnvironmentData as Env
from data.TestFrameworkEnvironmentData import TestFrameworkEnvironmentData as Tenv


class TestServicesAvailability:

    # initialization of list for not available services. If service check finds service is not available, it will be
    # added into this list
    lst_of_na_services = []

    service_unavailable = f" {Tenv.unavailable}"
    service_ok = f" {Tenv.ok}"

    # EVALUATION OF ENTIRE SERVICE CHECK
    @staticmethod
    def test_service_runner():
        """
        This method runs quick tests for check the availability of particular service/server/etc.
        If checked point is unavailable, it is added into lst_of_na_services list.
        If in the end of the all service checks is list empty, this functions returning True as testing can start,
        and False in other cases.
        """

        # Run method for particular service availability check
        TestServicesAvailability.app_availability_check()

        # Evaluate entire service check based on lis_of_na_services
        if len(TestServicesAvailability.lst_of_na_services) == 0:
            print(f"ALL SERVICES AVAILABLE. TESTS CAN START.")
            return True
        else:
            print()
            print("Some services requiered for VISMA-FRONTEND-TEST testing are unavailable.")
            print("Check above services and restart the tests.")
            print(f"{Fore.RED}AUTOMATION TESTING FOR {Env.environment} ENV ABORTED (NOT FAIL!){Fore.RESET}")
            return False

    # TEST FOR WEB APP AVAILABILITY:
    @staticmethod
    def app_availability_check():
        service_name = "WEB APP"
        print(service_name, end="")
        test = requests.get(Env.app_url)
        test = test.status_code
        if test == 200:
            test = True
        else:
            test = False
        TestServicesAvailability.availability_resolution(test, service_name)

    # TEST FOR foo:
    # ...

    # AVAILABILITY RESOLUTION FOR EVERY TEST
    @staticmethod
    def availability_resolution(test, service_name):
        if test:
            print(TestServicesAvailability.service_ok)
        else:
            TestServicesAvailability.lst_of_na_services.append(service_name)
            print(TestServicesAvailability.service_unavailable)
