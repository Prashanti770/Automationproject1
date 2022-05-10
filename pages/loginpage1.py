from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

class Loginpage1(BaseDriver):
    user_text = "//input[@id='user-name']"
    password_text = "//input[@id='password']"
    login_click = "//input[@id='login-button']"
    about_btn = "//div[@class='bm-burger-button']"
    allitems_xpath="//a[@id='inventory_sidebar_link']"
    closeabout_xpath ="//button[@id='react-burger-cross-btn']"
    logout_btn = "//a[@id='logout_sidebar_link']"
    # prdtitle_xpath ="//div[@class='header_secondary_container']"

    prdhometitle_xpath = "//span[@class='title']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def logindetails1(self, username, password):
        self.wait_until_element_is_clickable(By.XPATH, self.user_text).clear()
        self.wait_until_element_is_clickable(By.XPATH, self.user_text).send_keys(username)
        self.wait_until_element_is_clickable(By.XPATH, self.password_text).clear()
        self.wait_until_element_is_clickable(By.XPATH, self.password_text).send_keys(password)
        self.wait_until_element_is_clickable(By.XPATH, self.login_click).click()


    def hometitle(self):
        # hometitle = self.driver.title
        # return hometitle

        title_prd=self.wait_until_element_is_clickable(By.XPATH,self.prdhometitle_xpath).text
        return title_prd

    # def aboutclick(self):
    #     self.wait_until_element_is_clickable(By.XPATH,self.about_btn).click()
    #     self.wait_until_element_is_clickable(By.XPATH,self.allitems_xpath).click()
    #     self.wait_until_element_is_clickable(By.XPATH,self.closeabout_xpath).click()

    def logout(self):
        self.wait_until_element_is_clickable(By.XPATH,self.about_btn).click()
        self.wait_until_element_is_clickable(By.XPATH,self.logout_btn).click()

    def pagerefresh(self):
        self.driver.refresh()




