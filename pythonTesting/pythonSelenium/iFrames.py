from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
url = 'https://courses.letskodeit.com/practice'
driver.get(url)

# Switch to iFrame
# We can switch to the frame use: Webelement, ID, Name and Index
# By Name
my_frame = driver.find_element('id', 'courses-iframe')
driver.switch_to.frame(my_frame)
driver.find_element('xpath', '//*[@id="navbar-inverse-collapse"]/ul/li[2]/a')
driver.implicitly_wait(5)

drop_down_element = driver.find_element('name', 'categories')
select_drop_down = Select(drop_down_element)
select_drop_down.select_by_index(2)
select_drop_down.select_by_value('1606')
select_drop_down.select_by_visible_text('Python')
# Number of option in drop down
all_options = select_drop_down.options
for options in all_options:
    print(options.text)

# Switch back to main content
driver.switch_to.default_content()
driver.find_element('id', 'displayed-text').send_keys('Test')
driver.quit()
