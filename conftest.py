import pytest
from selenium import webdriver
import random
import string
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from data import TestData
from locators import TestLocators


@pytest.fixture(scope='function')
def driver():
    options = Options()
    service = Service(executable_path='C:/Users/gnom/Desktop/Sprint_5/chromedriver.exe')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture
def random_char():
    return str(''.join(random.choice(string.ascii_letters) for x in range(6)))

