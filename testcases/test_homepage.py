import pytest
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
from pages.loginpage import Loginpage
from pages.homepage import Homepage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen

@allure.severity(allure.severity_level.NORMAL)
class Test_002_homepage():
    baseURL = Readconfig.getApplicationURL()
    user = Readconfig.getUseremail()
    pwd = Readconfig.getPassword()
    fname = Readconfig.getfname()
    lname= Readconfig.getlname()
    pcode = Readconfig.getpcode()
    logger1 = LogGen.loginfo()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage(self,setUpClass):
        self.logger1.info("********* Test_001_login *********")
        self.driver = setUpClass
        self.driver.get(self.baseURL)
        self.logger1.info("********* Open Loginpage  *********")
        self.lp = Loginpage(self.driver)
        self.lp.logindetails(self.user,self.pwd)
        self.logger1.info("********* Successfully login  into the page *********")
        # self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_cartpage(self,setUpClass):
        self.driver = setUpClass
        self.driver.get(self.baseURL)
        self.logger1.info("********* Open Loginpage  *********")
        self.lp = Loginpage(self.driver)
        self.lp.logindetails(self.user, self.pwd)
        self.hp = Homepage(self.lp.driver)
        # self.hp = Homepage(self.driver)
        self.hp.productsadd_tocart()
        self.hp.cartpage()
        self.hp.checkout_info(self.fname,self.lname,self.pcode)
        self.hp.checkout_overview()
        finish_text =self.hp.checkout_complete()

        if finish_text == "THANK YOU FOR YOUR ORDER" :
            assert True
            print(finish_text)
            self.driver.close()

        else:
            assert False



