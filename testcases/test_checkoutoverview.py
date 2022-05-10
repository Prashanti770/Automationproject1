import time

import pytest
import allure
from testcases.test_checkoutpage import Test_004_Checkoutpage
from pages.checkoutovervview import Checkout_overview


# @pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("test_checkoutpage")
@allure.severity(allure.severity_level.NORMAL)
class Test_00_Checkoutoverview(Test_004_Checkoutpage):

    @allure.severity(allure.severity_level.CRITICAL)
    def test_checkoutoverview(self):

        self.cop = Checkout_overview(self.driver)
        self.cop.checkout_overview()
        time.sleep(5)
        act_text = self.cop.checkout_complete()
        # print(act_text)
        time.sleep(5)

        if act_text == "THANK YOU FOR YOUR ORDER":
            print("THANK YOU FOR YOUR ORDER")
            assert True


        else:
            assert False

