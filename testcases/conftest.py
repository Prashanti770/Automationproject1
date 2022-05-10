import pytest
from selenium import webdriver

@pytest.fixture
# def setUpClass(cls):
def setup():
    # global driver
    driver = webdriver.Edge(executable_path="C:\\edgedriver_win64 (1)\\msedgedriver.exe")
    # driver.maximize_window()
    # driver.implicitly_wait(10)
    return driver
    # driver.get(url)
    # driver.maximize_window()
    # request.cls.driver = driver
    # yield
    # driver.close()

import os
import time

# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# driver = None
#
# @pytest.fixture(autouse=True)
# def setup(request, browser, url):
#     global driver
#     if browser == "chrome":
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#     elif browser == "firefox":
#         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     # elif browser == "edge":
#     #     driver = webdriver.Edge(EdgeChromiumDriverManager().install())
#     elif browser=='edge':
#         driver = webdriver.edge()
#     driver.get(url)
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.close()