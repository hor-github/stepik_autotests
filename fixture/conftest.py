
from selenium.webdriver.chrome.webdriver import WebDriver
import pytest


@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    driver = WebDriver('/home/hor/ChromeDriver/chromedriver')
    # этот код выполняется после каждого теста
    yield driver
    print("\nquit browser..")
    driver.quit()


