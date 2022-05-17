import time

import pytest

import allure
from allure_commons.types import AttachmentType
from pages.loginpage import Loginpage
from pages.homepage1 import Homepage1
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from testcases.test_loginpage2 import test_logintopage2

baseURL = Readconfig.getApplicationURL()
user = Readconfig.getUseremail()
pwd = Readconfig.getPassword()
fname = Readconfig.getfname()
lname = Readconfig.getlname()
pcode = Readconfig.getpcode()
logger1 = LogGen.loginfo()
# hp = Homepage1.productsadd_tocart()

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.run(order=3)
@pytest.mark.dependency(depends=["testcases/test_loginpage2.py::test_logintopage2"])
def test_homepage2(test_logintopage2):

    driver = test_logintopage2
    # hp = Homepage1()
    Homepage1.productsadd_tocart(driver)
    time.sleep(5)


