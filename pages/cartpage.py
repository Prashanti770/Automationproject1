from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.loginpage import Loginpage

class Cartpage(BaseDriver):

    # cart_click_xpath = "//a[@class='shopping_cart_link']"
    checkout_btn_xpath = "//button[@class='btn btn_action btn_medium checkout_button']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def productsadd_tocart(self):

        # self.wait_until_element_is_clickable(By.XPATH,self.cart_click_xpath).click()
        self.wait_until_element_is_clickable(By.XPATH, self.checkout_btn_xpath).click()




