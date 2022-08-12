from selenium import webdriver
import time

driver = webdriver.Chrome()
url = 'https://courses.letskodeit.com/practice'

driver.get(url)
driver.find_element('id', 'name').send_keys('Karthikeya')
alert_button = driver.find_element('id', 'alertbtn').click()
my_alert = driver.switch_to.alert
alert_txt = my_alert.text
assert alert_txt == 'Hello Karthikeya, share this practice page and share your knowledge'
print(alert_txt)
driver.switch_to.alert.dismiss()
time.sleep(5)
driver.quit()




