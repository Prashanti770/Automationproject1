import time

import pytest
import allure
from pages.homepage1 import Homepage1
from testcases.test_cartpage import Test_003_Cartpage
from testcases.test_homepage1 import Test_002_homepage1
from testcases.test_loginpage import Test_001_login
from pages.checkoutpage import Checkoutinfo
from utilities.readProperties import Readconfig

# @pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("test_cartpage")
# @allure.severity(allure.severity_level.NORMAL)
class Test_004_Checkoutpage(Test_003_Cartpage):
    fname = Readconfig.getfname()
    lname = Readconfig.getlname()
    pcode = Readconfig.getpcode()

    # @allure.severity(allure.severity_level.CRITICAL)
    @pytest.fixture(scope="function")
    def test_checkoutpage(self):

        self.cip = Checkoutinfo(self.driver)
        self.cip.checkout_info(self.fname,self.lname,self.pcode)
        time.sleep(5)


