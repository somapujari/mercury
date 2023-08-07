import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def setup(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == 'chrome':
        option = webdriver.ChromeOptions()
        option.binary_location = r'C:\Users\Dell\AppData\Local\Google\Chrome\Application\chrome.exe'
        # path = ''
        # service = Service(path)
        # service.start()
        driver = webdriver.Chrome(options=option)
    else:
        driver = webdriver.Firefox()

    yield driver
    driver.quit()

