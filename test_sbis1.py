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
        browser.find_element(By.CSS_SELECTOR, "input[name='login']").send_keys("Балаган")
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("Балаган123")
        browser.find_element(By.CSS_SELECTOR, ".auth-Form__submit").click()
        time.sleep(5)
        # переход на главную Бизнес
        # Кликаем 2 раза по Бизнесу
        WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".NavigationPanels-Accordion__container a:nth-child(4)"))
        ).click()
        time.sleep(2)
        WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".NavigationPanels-SubMenu__headTitle"))
        ).click()
        time.sleep(7)

    finally:
        yield browser
        browser.quit()


def test_operation_filter(browser):
    """
    # В течение 15сек ждем текст=$100 из элемента с id=price
    price2 = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".controls-GridViewV__itemsContainer .business-page__grid-result-value"), "Продажи за период")
            )
    price2.click()
   """
    # Открываем панель построения отчета
    browser.find_element(By.CSS_SELECTOR, "div.business-accordion-block:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span").click()
    time.sleep(5)

    # кликаем на фильтр Операции
    operations = browser.find_element(By.CSS_SELECTOR, ".controls-StickyHeaderController div[name = 'popupTarget']").click()
