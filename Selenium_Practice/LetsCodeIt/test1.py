from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

url = "https://courses.letskodeit.com/practice"

driver = webdriver.Chrome()
driver.get(url)

class Practice():
    def fun1(self):
        driver.implicitly_wait(5)
# Radio buttons #
        radioButtonList = driver.find_elements(
            by=By.XPATH, value="//input[contains(@type, 'radio') and contains(@name, 'cars')]")
        for radioButtons in radioButtonList:
            isSelected = radioButtons.is_selected()
            if not isSelected:
                radioButtons.click()
                radio_options = len(radioButtonList)
                print(radio_options)

# Dropdown - select method
# 3 Ways to select, select by value, index and visible text
        drop_down = driver.find_element('id', 'carselect')
        select_method = Select(drop_down)
        select_method.select_by_value('honda')
        select_method.select_by_index(0)
        select_method.select_by_visible_text('Benz')
        all_options = select_method.options
        for options in all_options:
            print(options.text)
# Multiselect options #
        multi_select = driver.find_element('id', 'multiple-select-example')
        sel = Select(multi_select)
        sel.select_by_value('apple')
        sel.select_by_index(1)
        sel.select_by_visible_text('Peach')
        multi_options = sel.options
        for options in multi_options:
            print(options.text)
# Checkbox #
        driver.find_element('id', 'bmwcheck').click()
        driver.find_element('id', 'benzcheck').click()
        driver.find_element('id', 'hondacheck').click()


    def newWindow(self):
        #driver = webdriver.Chrome()
        #driver.get(url)
        # Parent window
        parentHandle = driver.current_window_handle
        # Clicking on New window
        driver.find_element('id', 'openwindow').click()
        # There should be 2 windows
        handles = driver.window_handles
        # Switch to new window
        for handle in handles:
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                driver.find_element('xpath', '//*[@id="navbar-inverse-collapse"]/ul/li[3]/a').click()
                time.sleep(5)
                driver.close()
                break # break the loop
        # Switch back to the parent window
        driver.switch_to.window(parentHandle)
        driver.find_element('id', 'enabled-example-input').send_keys('Test')
        time.sleep(5)
        driver.quit()

    def newTab(self):
         driver = webdriver.Chrome()
         driver.get(url)
         parentWindow1 = driver.current_window_handle
         driver.find_element('id', 'opentab').click()
         newHandles = driver.window_handles
         for handle1 in newHandles:
             if handle1 not in parentWindow1:
                 driver.switch_to.window(handle1)
                 time.sleep(5)
                 driver.find_element('xpath', '//input[@placeholder="Search Course"]').send_keys('Python')
                 time.sleep(5)
                 driver.close()
                 break
         driver.switch_to.window(parentWindow1)
         driver.find_element('id', 'displayed-text').send_keys('Testing')
         time.sleep(5)

    def newWindowTab(self):
        driver = webdriver.Chrome()
        driver.get(url)
        #driver.find_element('id', 'opentab').click()  # New tab
        driver.find_element('id', 'openwindow').click()  # New window
        print(driver.title)
        all_windows = driver.window_handles
        current_window = all_windows[0]
        new_window = all_windows[1]
        driver.switch_to.window(new_window)

        print(driver.title)
        driver.find_element('xpath', '//input[@placeholder="Search Course"]').send_keys('Python')
        time.sleep(5)
        driver.switch_to.window(current_window)
        driver.find_element('id', 'displayed-text').send_keys('Testing')
        time.sleep(5)

    def mouseHover(self):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.find_element('id', 'mousehover').click()
        driver.find_element(
            'css selector', '#mouse-hover-example-div > div > fieldset > div > div > a:nth-child(1)').click()

    def alert(self):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.find_element('id', 'name').send_keys('Test')
        driver.find_element('id', 'alertbtn').click()
        my_alert = driver.switch_to.alert
        t = my_alert.text
        assert t == "Hello Test, share this practice page and share your knowledge"
        print(t)
        driver.switch_to.alert.dismiss()

    def iFrame(self):
        driver = webdriver.Chrome()
        driver.get(url)
        my_frame = driver.find_element('id', 'courses-iframe')
        driver.switch_to.frame(my_frame)
        dd = driver.find_element('name', 'categories')
        dd.click()
        sel = Select(dd)
        sel.select_by_index(1)
        driver.switch_to.default_content()
        driver.find_element('id', 'bmwradio').click()
        time.sleep(5)
        driver.close()


#obj = Practice()
#obj.fun1()
#obj.newWindow()
#obj.newTab()
#obj.mouseHover()
#obj.newWindowTab()
#obj.alert()
#obj.iFrame()





