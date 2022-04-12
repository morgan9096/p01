import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome('../_chrome_driver/chromedriver')
    yield driver
    driver.quit()