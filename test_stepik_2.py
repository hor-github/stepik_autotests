# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time

import math
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyperclip

# driver = WebDriver(executable_path='C://selenium//chromedriver.exe')
driver = WebDriver('/home/hor/ChromeDriver/chromedriver')


# основные методы Selenium

def test_1():
    try:
        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))

        driver.get("http://suninjuly.github.io/math.html")
        x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
        y = calc(x)
        input1 = driver.find_element(By.CSS_SELECTOR, ".form-group input").send_keys(y)
        checkbox = driver.find_element(By.CSS_SELECTOR, ".form-check #robotCheckbox,#robotsRule").click()
        # radio = driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
        btnsubmit = driver.find_element(By.CSS_SELECTOR, ".btn").click()
    finally:
        time.sleep(30)
        driver.quit()

# 2.1 get_attribute
def test_2():
    try:
        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))

        driver.get("http://suninjuly.github.io/get_attribute.html")
        # находим элемент
        x = driver.find_element(By.CSS_SELECTOR, ".nowrap ~ img ")
        # получаем значение атрибута valuex
        art = x.get_attribute("valuex")
        # подставляем в формулу значение атрибута valuex
        y = calc(art)
        input1 = driver.find_element(By.CSS_SELECTOR, ".form-group #answer").send_keys(y)
        checkbox = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
        radiobutton = driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
        button = driver.find_element(By.CSS_SELECTOR, ".btn").click()
    finally:
        time.sleep(10)
        driver.quit()


# 2.2 Работа с файлами, списками и js-скриптами

# Работа со списками
def test_3():
    try:
        driver.get("http://suninjuly.github.io/selects1.html")
        num1 = driver.find_element(By.CSS_SELECTOR, ".container span:nth-child(2)").text
        num2 = driver.find_element(By.CSS_SELECTOR, ".container span:nth-child(4)").text
        # sum = int(num1) + int(num2)

        # находим выпадающий список
        select = Select(driver.find_element(By.CSS_SELECTOR, ".custom-select"))
        # выбираем значение суммы переменной sum
        select.select_by_value(str(int(num1) + int(num2)))
        driver.find_element(By.CSS_SELECTOR, ".btn").click()

    finally:
        time.sleep(10)
        driver.quit()

# Работа с js скриптами и прокруткой до нужного элемента
def test_4():
    try:
        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))

        driver.get(" http://SunInJuly.github.io/execute_script.html")
        x = driver.find_element(By.CSS_SELECTOR, ".form-group .nowrap:nth-child(2)").text
        y = calc(x)

        # скроллим страницу до кнопки Submit
        btn = driver.find_element(By.CSS_SELECTOR, ".form-check ~ .btn")
        driver.execute_script("return arguments[0].scrollIntoView({block: 'center'});", btn)

        # Вводим ответ в текстовое поле
        input1 = driver.find_element(By.CSS_SELECTOR, "#answer").send_keys((y))

        # кликаем чекбокс и радиобаттон
        driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
        driver.find_element(By.CSS_SELECTOR, ".form-radio-custom :nth-child(2)").click()

        btn.click()
    finally:
        time.sleep(10)
        driver.quit()

# Загрузка файлов
def test_5():
    try:
        driver.get("http://suninjuly.github.io/file_input.html")
        # driver.find_element(By.CSS_SELECTOR, ".form-group :nth-child(2)").send_keys("text")
        # driver.find_element(By.CSS_SELECTOR, ".form-group :nth-child(4)").send_keys("text")
        # driver.find_element(By.CSS_SELECTOR, ".form-group :nth-child(6)").send_keys("text")

        # заполняем все 3 инпута
        elements = driver.find_elements(By.CSS_SELECTOR, ".form-control")
        for element in elements:
            element.send_keys("text")
        # з
        current_dir = os.path.abspath(os.path.dirname("Autotests_for_Stepik"))  # получаем путь к директории текущего исполняемого файла
        file_path = os.path.join(current_dir, '222.txt')  # добавляем к этому пути имя файла
        driver.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path) # применяем метов сендкейс к кнопке "Загрузить файл"

        btn = driver.find_element(By.CSS_SELECTOR, ".btn").click()

    finally:
        time.sleep(10)
        driver.quit()


# 2.3 Работа с окнами
def test_accept_alert ():
    try:
        driver.get("http://suninjuly.github.io/alert_accept.html")
        driver.find_element(By.CSS_SELECTOR, ".container>.btn").click()
        # переключаемся на модальное окно и соглашаемся
        cnf = driver.switch_to.alert.accept()

        # решаем капчу
        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))
        x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
        y = calc(x)
        driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
        btn = driver.find_element(By.CSS_SELECTOR, ".btn").click()

        # помещаем всплывшее число в буфер обмена
        # переключаемся на всплывшее окно
        alert = driver.switch_to.alert
        # получаем весь текст всплывшего окна
        alert_text = alert.text
        # парсим и преобразуем нужное нам число
        addToClipBoard = alert_text.split(': ')[-1]
        # копируем нужное число в буфер обмена
        pyperclip.copy(addToClipBoard)
    finally:
        time.sleep(10)
        driver.quit()


# 2.3 Работа с окнами - переход на новую вкладку
def test_6 ():
    try:
        driver.get("http://suninjuly.github.io/redirect_accept.html")
        driver.find_element(By.CSS_SELECTOR, ".container .btn").click()

        # ищем вновь открытую вкладку и переходим на нее
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)

        # решаем капчу
        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))

        x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
        y = calc(x)
        driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
        btn = driver.find_element(By.CSS_SELECTOR, ".btn").click()

        # помещаем всплывшее число в буфер обмена
        # переключаемся на всплывшее окно
        alert = driver.switch_to.alert
        # получаем весь текст всплывшего окна
        alert_text = alert.text
        # парсим и преобразуем нужное нам число
        addToClipBoard = alert_text.split(': ')[-1]
        # копируем нужное число в буфер обмена
        pyperclip.copy(addToClipBoard)

    finally:
        time.sleep(10)
        driver.quit()


# 2.4 Настройка ожиданий
def test_7 ():
    try:
        driver.get("http://suninjuly.github.io/explicit_wait2.html")
        # ожидаем 15 секунд значение 100 баксов
        price = WebDriverWait(driver, 15).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".card-title~#price"), "$100")
        )
        driver.find_element(By.CSS_SELECTOR, "#book").click()

        # решаем капчу
        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))

        x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
        y = calc(x)
        driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
        btn = driver.find_element(By.CSS_SELECTOR, ".form-group~.btn").click()

        # помещаем всплывшее число в буфер обмена
        # переключаемся на всплывшее окно
        alert = driver.switch_to.alert
        # получаем весь текст всплывшего окна
        alert_text = alert.text
        # парсим и преобразуем нужное нам число
        addToClipBoard = alert_text.split(': ')[-1]
        # копируем нужное число в буфер обмена
        pyperclip.copy(addToClipBoard)

    finally:
        time.sleep(10)
        driver.quit()

