from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.loginpage import Loginpage

class Homepage(BaseDriver):
    product_addition_1_xpath = "//button[@id='add-to-cart-sauce-labs-backpack']"
    product_addition_2_xpath = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    cart_click_xpath = "//a[@class='shopping_cart_link']"
    checkout_btn_xpath ="//button[@class='btn btn_action btn_medium checkout_button']"
    firstname_id = "first-name"
    lastname_id = "last-name"
    postalcode_id = "postal-code"
    continue_id = "continue"
    finish_id = "finish"
    final_text_xpath = "//h2[contains(text(),'THANK YOU FOR YOUR ORDER')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def productsadd_tocart(self):
        self.wait_until_element_is_clickable(By.XPATH,self.product_addition_1_xpath).click()
        self.wait_until_element_is_clickable(By.XPATH,self.product_addition_2_xpath).click()
        self.wait_until_element_is_clickable(By.XPATH,self.cart_click_xpath).click()

    def cartpage(self):
        self.wait_until_element_is_clickable(By.XPATH,self.checkout_btn_xpath).click()

    def checkout_info(self,fname,lname,pcode):
        self.wait_until_element_is_clickable(By.ID,self.firstname_id).send_keys(fname)
        self.wait_until_element_is_clickable(By.ID, self.lastname_id).send_keys(lname)
        self.wait_until_element_is_clickable(By.ID, self.postalcode_id).send_keys(pcode)
        self.wait_until_element_is_clickable(By.ID, self.continue_id).click()

    def checkout_overview(self):
        self.wait_until_element_is_clickable(By.ID, self.finish_id).click()

    def checkout_complete(self):
       finaltext = self.wait_until_element_is_clickable(By.XPATH, self.final_text_xpath).text
       return finaltext








