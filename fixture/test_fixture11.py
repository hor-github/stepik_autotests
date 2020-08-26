"""
3.6 PyTest - параметризация, конфигурирование, плагины
Задание: параметризация тестов
"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
import os
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyperclip


# driver = WebDriver('/home/hor/ChromeDriver/chromedriver')


# в качестве параметров устанавливам части URL
@pytest.mark.parametrize('param', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_1(driver, param):
    answer = math.log(int(time.time()))
    # подставляем параметры в ссылку
    link = f"https://stepik.org/lesson/{param}/step/1"
    driver.get(link)
    # ожидание элемента 10 сек
    driver.implicitly_wait(10)
    input1 = driver.find_element(By.CSS_SELECTOR, ".page-fragment .textarea").send_keys(str(answer))

    button1 = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    button1.click()

    time.sleep(3)
    # считываем сообщение об успешном выполнени
    pole = driver.find_element(By.CSS_SELECTOR, ".smart-hints__feedback .smart-hints__hint").text

    # Сравниваем результат
    assert pole == "Correct!"



