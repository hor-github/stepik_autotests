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


def test_22 ():
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