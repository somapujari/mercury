import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def setup(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    yield driver
    driver.quit()
