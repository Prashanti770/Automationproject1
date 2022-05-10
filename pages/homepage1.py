from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.loginpage import Loginpage

class Homepage1(BaseDriver):
    product_addition_1_xpath = "//button[@id='add-to-cart-sauce-labs-backpack']"
    product_addition_2_xpath = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    cart_click_xpath = "//a[@class='shopping_cart_link']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def productsadd_tocart(self):
        self.wait_until_element_is_clickable(By.XPATH,self.product_addition_1_xpath).click()
        self.wait_until_element_is_clickable(By.XPATH,self.product_addition_2_xpath).click()
        self.wait_until_element_is_clickable(By.XPATH, self.cart_click_xpath).click()
        # self.driver.find_element(By.XPATH, self.product_addition_1_xpath).click()
        # self.driver.find_element(By.XPATH, self.product_addition_2_xpath).click()
        # self.driver.find_element(By.XPATH, self.cart_click_xpath).click()

