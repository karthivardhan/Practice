from selenium import webdriver
import time

url = "https://www.expedia.co.in/"
driver = webdriver.Chrome()
driver.get(url)
dropdown = driver.find_element('css selector', "[aria-describedby='header-menu-expand_more-description']").click()
all_options = dropdown.options
for options in all_options:
    print(options.text)

driver.find_element('xpath', "//a[@aria-label='Cars']").click()
time.sleep(5)
'''driver.find_element('css selector', "[class*='uitk-form-field-trigger']").click()
search = driver.find_element('id', 'location-field-destination')
search.send_keys('Hyderabad')
time.sleep(5)
driver.find_element('css selector', "[class*='uitk-icon-leading']").click()
time.sleep(5)
driver.find_element('css selector', "[data-testid='submit-button']").click()'''
driver.quit()