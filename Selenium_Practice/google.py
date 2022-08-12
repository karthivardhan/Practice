import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

browser_name = ''
url = 'https://www.google.co.in'
def setup(request):
browser_name = request.config.getoption("browser_name")
if browser_name == 'chrome':
driver = webdriver.Chrome()
elif browser_name == 'firefox':
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()

driver.find_element('name', 'q').send_keys('Selenium Automation')
driver.find_element('css selector', 'input[value="Google Search"]').click()
driver.find_element('xpath', "//h3[text()='Selenium']").click()
driver.back()
driver.find_element(by=By.LINK_TEXT, value="Videos").click()
driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Imag').click()
time.sleep(2)
driver.forward()
    #driver.save_screenshot("image.png")
time.sleep(2)
driver.close()
