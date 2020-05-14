import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time

import math
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyperclip

link = "https://fix-online.sbis.ru/auth/"


@pytest.fixture()
def browser():
    try:
        browser = WebDriver('/home/hor/ChromeDriver/chromedriver')
    # Авторизация
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".controls-InputBase__field .controls-InputBase__nativeField_theme_default_caretFilled").send_keys("Балаган")
        browser.find_element(By.CSS_SELECTOR, ".controls-Render__wrapper input[autocomplete="current-password"]").send_keys("Балаган123")
        browser.find_element(By.CSS_SELECTOR, ".auth-Form__submit").click()
        time.sleep(10)
    finally:
        yield browser
        browser.quit()


def test_1(browser):
    WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".NavigationPanels-Accordion__container a:nth-child(3)"))
        )
    browser.find_element(By.CSS_SELECTOR, ".NavigationPanels-Accordion__container a:nth-child(3)").clik()