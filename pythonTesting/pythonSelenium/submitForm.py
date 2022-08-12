from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element(by=By.NAME, value="name").send_keys('Karthikeya')
driver.find_element('name', "name").send_keys('Karthikeya')
driver.find_element('name', "email").send_keys("karthi.vardhan@gmail.com")
driver.find_element('id', "exampleCheck1").click()
driver.find_element('id', "inlineRadio2").click()
driver.find_element('xpath', "//input[@type='submit']").click()
print(driver.find_element('css selector', "[class*='alert']").text) #assertion
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
driver.find_element('css selector', "[class*='btn-info']").click()
time.sleep(10)
driver.find_element('css selector', "[class*='nav-link']").click()

driver.get('https://courses.letskodeit.com/practice')
driver.find_element('id', 'hondaradio').click()
#driver.find_element('')
#print(driver.find_element('class', 'text-success').text)



