from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.loginpage import Loginpage

class Checkout_overview(BaseDriver):

    finish_id = "finish"
    final_text_xpath = "//h2[contains(text(),'THANK YOU FOR YOUR ORDER')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def checkout_overview(self):
        self.wait_until_element_is_clickable(By.ID, self.finish_id).click()

    def checkout_complete(self):
       finaltext = self.wait_until_element_is_clickable(By.XPATH, self.final_text_xpath).text
       # print(finaltext)
       return finaltext








