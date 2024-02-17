import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    options = Options()
    service = Service(executable_path='C:/Users/gnom/Desktop/Sprint_5/chromedriver.exe')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()