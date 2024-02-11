import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    url = "https://www.saucedemo.com"
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
    driver.close()