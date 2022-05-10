import pytest
import allure
from pytest import fixture
from allure_commons.types import AttachmentType
from pages.loginpage import Loginpage
from pages.homepage import Homepage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
import time
from utilities import XLutilities
from pages.loginpage1 import Loginpage1

# @pytest.mark.usefixtures("setUpClass")
@allure.severity(allure.severity_level.NORMAL)

class Test_001_login():
    baseURL = Readconfig.getApplicationURL()
    logger1 = LogGen.loginfo()

    path = ".\\testdata\\Login3.xlsx"

    rows = XLutilities.getRowCount(path, 'Sheet1')

    @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.fixture(scope="function")
    def test_logintopage1(self,setup):
        self.logger1.info("********* Test_001_login *********")
        # self.driver = driver
        self.driver = setup
        self.driver.get(self.baseURL)

        self.logger1.info("********* Open Loginpage  *********")

        for r in range(2, self.rows + 1):  # starts from 2 row
            # extract data from each column
            username = XLutilities.readData(self.path, 'Sheet1', r, 1)
            password = XLutilities.readData(self.path, 'Sheet1', r, 2)
            # time.sleep(5)
            self.lp = Loginpage1(self.driver)
            self.lp.logindetails1(username,password)
            time.sleep(5)
            prd_title = self.lp.hometitle()
            print("title is " , prd_title)
            # time.sleep(5)

            if prd_title == "PRODUCTS _" :
                print("test is failed")
                XLutilities.writeData(self.path, 'Sheet1', r, 3, "test failed")
                assert False


            elif prd_title == "PRODUCTS" :
                print("test is passed")
                XLutilities.writeData(self.path, 'Sheet1', r, 3, "test passed")
                assert True

            else:
                # self.lp.refresh()
                self.driver.refresh()

            # self.lp.pagerefresh()
            # if prd_title == "PRODUCTS":
            # # if prd_title == "Sauce Labs Backpack":
            #     print("test is passed")
            #     XLutilities.writeData(self.path, 'Sheet1', r, 3, "test passed")
            #     self.logger1.info("********* Successfully login  into the page *********")
            #     self.lp.logout()
            #     # self.lp.pagerefresh()
            #
            # else:
            #    print("test failed")
            #    XLutilities.writeData(self.path, 'Sheet1', r, 3, "test failed")
            #    time.sleep(10)
            #    self.driver.close()
            #     # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            # # time.sleep(5)
            # # self.driver.refresh()

        # self.lp.pagerefresh()

        # self.driver.refresh()
                # time.sleep(5)
            # self.lp.refresh()
            # self.driver.refresh()
        # self.driver.back()
        # self.driver.forward()





