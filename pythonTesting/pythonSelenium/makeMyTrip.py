from selenium import webdriver
import time

from selenium.webdriver.support.select import Select


class MakeMyTripSite():
    def __init__(self, driver):
        self.driver = driver

    def flights(self):
        self.driver.find_element('css selector', "[data-cy='menu_Hotels']").click()
        self.driver.find_element('css selector', "[data-cy='menu_Flights']").click()
        self.driver.find_element('id', 'fromCity').send_keys('Hyderabad')
        time.sleep(5)
        element = self.driver.find_element('xpath', "//div[@class='calc60']")
        ele = Select(element)
        ele.select_by_visible_text('Hyderabad, India')
        self.driver.close()






