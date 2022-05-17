import time
import pytest
from selenium import webdriver

# @pytest.fixture(params =["chrome","edge"], scope='class')
# def init__driver(request):
#     driver = None
#     if request.param == 'chrome':
#         driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
#         print("Launching chrome browser.................")
#     elif request.param == 'edge':
#         driver = webdriver.Edge(executable_path="C:\\edgedriver_win64 (1)\\msedgedriver.exe")
#         print("Launching Edge browser ...................")
#     else:
#         driver = webdriver.Firefox()
#         print("Launching Firefox browser ...................")
#
#     driver.implicitly_wait(10)
#     request.cls.driver = driver
#     yield request.cls.driver
#     # yield
#     time.sleep(5)
#     request.cls.driver.quit()

    # return _driver

@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        print("Launching chrome browser.................")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser ...................")
    else:
        driver =webdriver.Edge(executable_path="C:\\edgedriver_win64 (1)\\msedgedriver.exe")
        print("Launching Edge browser ...................")

    return driver

def pytest_addoption(parser): #gets the value from CLI/hook
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #returns browser value to setup method
    return request.config.getoption("--browser")



