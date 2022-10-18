import configparser
from selenium import webdriver
import pytest
# import parser

@pytest.fixture
def setup(browser):
    if browser=="edge":
        driver = webdriver.Edge()
        print("Launching Edge Browser...!")

    elif browser=="firefox":
        driver =webdriver.Firefox()
        print("Launching Firefox Browser...!")
    else:
        ops = webdriver.ChromeOptions()
        # ops.headless =True
        driver = webdriver.Chrome(options=ops)
        print("Launching Chrome Browser...!")
    return driver
'''@pytest.fixture()
def headless_chrome():
    ops = webdriver.ChromeOptions()      #######------>>>   HEAD LESS METHOD
    ops.headless = True
    driver = webdriver.Chrome(options=ops)
    return driver'''

parser=configparser.RawConfigParser
def pytest_addoption(parser):                           #This will get the value from command line/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.option.browser

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Plugins",None)