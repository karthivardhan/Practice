import pdb

from selenium import webdriver
import time

driver = webdriver.Chrome()
url = 'https://courses.letskodeit.com/practice'

driver.get(url)
driver.find_element('id', 'opentab').click()
print('Before to switching: ', driver.title)
all_window_habdles = driver.window_handles
original_window_handles = all_window_habdles[0] #current URL
new_window_handles = all_window_habdles[1] #new tab
driver.switch_to.window(new_window_handles)
print('After switching focus: ', driver.title)
driver.close() # close new tab
time.sleep(10)
driver.switch_to.window(original_window_handles)
driver.quit()

#import pdb; pdb.set_trace()
