import pytest
import allure
from pytest import fixture
from allure_commons.types import AttachmentType
from pages.loginpage import Loginpage
from pages.homepage import Homepage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
import time


# @pytest.mark.usefixtures("setUpClass")
@allure.severity(allure.severity_level.NORMAL)

class Test_001_login():
    baseURL = Readconfig.getApplicationURL()
    user = Readconfig.getUseremail()
    pwd = Readconfig.getPassword()
    logger1 = LogGen.loginfo()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.fixture(scope="function")

    @pytest.mark.run(order=2)
    # @pytest.mark.dependency(depends=['Test_001_login::test_hometitles'])
    @pytest.mark.dependency()
    def test_logintopage(self,setup):
        self.logger1.info("********* Test_001_login *********")
        # self.driver = driver
        self.driver = setup
        self.driver.get(self.baseURL)

        self.logger1.info("********* Open Loginpage  *********")
        self.lp = Loginpage(self.driver)
        self.lp.logindetails(self.user,self.pwd)
        self.logger1.info("********* Successfully login  into the page *********")
        time.sleep(5)
        # self.driver.close()

    @allure.severity(allure.severity_level.MINOR)
    # @pytest.mark.dependency()
    def test_logo(self,setup):
        self.logger1.info("********* Verify Page Logo *********")
        self.logger1.warning("********* Test Skipped *********")
        pytest.skip("Test case is skipped")
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=1)
    @pytest.mark.dependency()
    def test_hometitles(self,setup):

        self.logger1.info("********* Verify Homepage Title *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title)

        if act_title == "Swag Labs":
            self.logger1.info("********* Title is correct *********")
            print("title is", act_title)
            assert True
            self.driver.close()


        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="Testcase01 title",attachment_type=AttachmentType.PNG)
            self.logger1.error("********* Title is incorrect *********")
            self.driver.save_screenshot(".\\Screenshots\\test_hometitle.png")
            assert False
            self.driver.close()




