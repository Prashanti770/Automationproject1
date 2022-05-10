import time

import pytest
import allure
from pages.homepage1 import Homepage1
from testcases.test_homepage1 import Test_002_homepage1
from testcases.test_loginpage import Test_001_login
from pages.checkoutpage import Checkoutinfo
from pages.cartpage import Cartpage

# @pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("test_homepage")
@allure.severity(allure.severity_level.NORMAL)
class Test_003_Cartpage(Test_002_homepage1):


    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.fixture(scope="function")
    def test_cartpage(self):

        self.cp = Cartpage(self.driver)
        self.cp.productsadd_tocart()
        time.sleep(5)



