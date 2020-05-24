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
        browser.find_element(By.CSS_SELECTOR, ".controls-InputBase__field_theme_default_margin input").send_keys("Балаган")
        browser.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("Балаган123")
        browser.find_element(By.CSS_SELECTOR, ".auth-Form__submit").click()
        time.sleep(5)
        # переход на главную Бизнес
        # Кликаем 2 раза по Бизнесу
        WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".NavigationPanels-Accordion__container a:nth-child(3)"))
        ).click()

        WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".NavigationPanels-SubMenu__lvl-1  .acc-menu-prevent-default:nth-child(2)"))
        ).click()
        time.sleep(5)

    finally:
        yield browser
        browser.quit()


def test_operation_filter(browser):
    # Кликаем 2 раза по Бизнесу
    WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".NavigationPanels-Accordion__container a:nth-child(3)"))
        ).click()
