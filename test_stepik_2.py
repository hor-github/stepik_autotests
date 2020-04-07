# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
import time

import math
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

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


# 2.2 Работа со списками
def test_3():
    