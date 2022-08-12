from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
baseUrl = "https://google.co.in"
driver.get(baseUrl)
google = driver.find_element('name', 'q')
google.send_keys('hello')
#driver.find_element('body', '')
driver.find_element(by=By.XPATH, value="//body>div>button[@class='M6CB1c.rr4y5c']").click()
driver.find_element('name', 'btnK').click()