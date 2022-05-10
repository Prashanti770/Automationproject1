import time

import pytest
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
from pages.loginpage import Loginpage
from pages.homepage1 import Homepage1
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from testcases.test_loginpage import Test_001_login

# @pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("test_logintopage")
@allure.severity(allure.severity_level.NORMAL)
class Test_002_homepage1(Test_001_login):

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.fixture(scope="function")
    def test_homepage(self):

        self.hp = Homepage1(self.driver)
        self.hp.productsadd_tocart()
        time.sleep(5)



