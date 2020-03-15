

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
import time

import math
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



#driver = WebDriver(executable_path='C://selenium//chromedriver.exe')
driver = WebDriver('/home/hor/ChromeDriver/chromedriver')
#driver = WebDriver.Chrome(r'/ChromeDriver/chromedriver')


def test_22 ():
    driver.get('https://habr.com/ru/post/273897/')