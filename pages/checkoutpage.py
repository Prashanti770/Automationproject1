import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.loginpage import Loginpage

class Checkoutinfo(BaseDriver):

    firstname_id = "first-name"
    lastname_id = "last-name"
    postalcode_id = "postal-code"
    continue_id = "continue"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def checkout_info(self,fname,lname,pcode):
        self.wait_until_element_is_clickable(By.ID,self.firstname_id).send_keys(fname)
        self.wait_until_element_is_clickable(By.ID, self.lastname_id).send_keys(lname)
        self.wait_until_element_is_clickable(By.ID, self.postalcode_id).send_keys(pcode)
        time.sleep(5)
        self.wait_until_element_is_clickable(By.ID, self.continue_id).click()









