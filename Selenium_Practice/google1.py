import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.google.co.in'
search_box = ('name', 'q')
search_button = ('css selector', 'input[value="Google Search"]')

class Google():

    def med1(self):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()

        driver.find_element(*search_box).send_keys('Selenium Automation') # Global variable
        driver.find_element('css selector', 'input[value="Google Search"]').click() # Class variable
        driver.find_element('xpath', "//h3[text()='Selenium']").click()
        driver.back()
        driver.find_element(by=By.LINK_TEXT, value="Videos").click()
        driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Imag').click()
        time.sleep(2)
        driver.forward()
            #driver.save_screenshot("image.png")
        time.sleep(2)
        driver.close()


obj = Google()
obj.med1()