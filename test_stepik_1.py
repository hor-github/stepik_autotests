
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


def test_1():
    try:
        driver.get('http://suninjuly.github.io/simple_form_find_task.html')
        input1 = driver.find_element(By.TAG_NAME, "input").send_keys("Ivan")
        input2 = driver.find_element(By.NAME, "last_name").send_keys("Petrov")
        input3 = driver.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
        input4 = driver.find_element(By.ID, "country").send_keys("Russia")
        button = driver.find_element(By.CSS_SELECTOR, ".btn").click()

    finally:
        time.sleep(30)
        driver.quit()


#  Search elements with help Selenium WebD
def test_2():
    try:
        driver.get('http://suninjuly.github.io/find_link_text')
        a = str(math.ceil(math.pow(math.pi, math.e) * 10000))
        link1 = driver.find_element(By.PARTIAL_LINK_TEXT, "224592").click()

        input1 = driver.find_element(By.TAG_NAME, "input").send_keys("Ivan")
        input2 = driver.find_element(By.NAME, "last_name").send_keys("Petrov")
        input3 = driver.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
        input4 = driver.find_element(By.ID, "country").send_keys("Russia")
        button = driver.find_element(By.CSS_SELECTOR, ".btn").click()

    finally:
        time.sleep(10)
        driver.quit()

# 1.6 using method find_elementS_by
def test_3():
    try:
        driver.get('http://suninjuly.github.io/huge_form.html')
        elements = driver.find_elements(By.CSS_SELECTOR, ".first_block input")
        for element in elements:
            element.send_keys("my")
        button = driver.find_element(By.CSS_SELECTOR, ".btn").click()

    finally:
        time.sleep(10)
        driver.quit()

# Xpath
def test_4():
    try:
        driver.get('http://suninjuly.github.io/find_xpath_form')
        input1 = driver.find_element(By.TAG_NAME, "input").send_keys("Ivan")
        input2 = driver.find_element(By.NAME, "last_name").send_keys("Petrov")
        input3 = driver.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
        input4 = driver.find_element(By.ID, "country").send_keys("Russia")
        button = driver.find_element(By.XPATH, "//button[@type='submit']").click()
    finally:
        time.sleep(10)
        driver.quit()


def test_5():
    try:
        driver.get("http://suninjuly.github.io/registration2.html")
        input1 = driver.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        input2 = driver.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Ivanov")
        input3 = driver.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("111@mail.ru")

        # находим кнопку
        button = driver.find_element_by_css_selector("button.btn").click()

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        driver.quit()
