import pytest
import allure
from pytest import fixture
from allure_commons.types import AttachmentType
from pages.loginpage import Loginpage
from pages.homepage import Homepage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
import time

baseURL = Readconfig.getApplicationURL()
user = Readconfig.getUseremail()
pwd = Readconfig.getPassword()
logger1 = LogGen.loginfo()

@allure.severity(allure.severity_level.CRITICAL)
@pytest.fixture
@pytest.mark.run(order=2)
# @pytest.mark.dependency(depends=['test_hometitles'])
@pytest.mark.dependency()
def test_logintopage2(setup):
   logger1.info("********* Test_001_login *********")
   driver = setup
   driver.get(baseURL)
   logger1.info("********* Open Loginpage  *********")
   lp = Loginpage(driver)
   lp.logindetails(user,pwd)
   # yield lp
   logger1.info("********* Successfully login  into the page *********")
   time.sleep(5)

@allure.severity(allure.severity_level.MINOR)
@pytest.fixture
@pytest.mark.dependency()
def test_logo(setup):
   logger1.info("********* Verify Page Logo *********")
   logger1.warning("********* Test Skipped *********")
   pytest.skip("Test case is skipped")
   # driver.close()

@allure.severity(allure.severity_level.NORMAL)
@pytest.fixture
@pytest.mark.run(order=1)
@pytest.mark.dependency()
def test_hometitles(setup):
   logger1.info("********* Verify Homepage Title *********")
   driver = setup
   driver.get(baseURL)
   act_title = driver.title
   print(act_title)

   if act_title == "Swag Labs":
       logger1.info("********* Title is correct *********")
       print("title is", act_title)
       assert True
       driver.close()
   else:
       allure.attach(driver.get_screenshot_as_png(),name="Testcase01 title",attachment_type=AttachmentType.PNG)
       logger1.error("********* Title is incorrect *********")
       driver.save_screenshot(".\\Screenshots\\test_hometitle.png")
       assert False
       driver.close()




