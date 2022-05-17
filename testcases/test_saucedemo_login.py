import pytest
import allure
from pages.loginpage import Loginpage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
import time

baseURL = Readconfig.getApplicationURL()
user = Readconfig.getUseremail()
pwd = Readconfig.getPassword()
logger1 = LogGen.loginfo()

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("setup")
def test_logintopage(self):
    self.logger1.info("********* Test_001_login *********")
    # self.driver = setup
    # driver = self.driver
    self.driver.get(self.baseURL)
    self.logger1.info("********* Open Loginpage  *********")
    self.lp = Loginpage(self.driver)
    self.lp.logindetails(user,pwd)
    self.logger1.info("********* Successfully login  into the page *********")
    # time.sleep(5)

# @pytest.mark.usefixtures("setup")
def test_gettitle(self):
    driver = self.driver
    print(driver.title)