from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


baseUrl = "https://courses.letskodeit.com/"

class LetsCode():
    def __init__(self, driver):
        self.driver = driver
        #driver = webdriver.Firefox()
        #driver.get(baseUrl)

        ### Radio buttons and checkboxes ###
    def allFields(self):
        bmwradio = self.driver.find_element('id', 'bmwradio')
        bmwradio.click()
        hondaradio = self.driver.find_element('id', 'hondaradio')
        hondaradio.click()
        self.driver.find_element('id', 'bmwcheck').click()
        self.driver.find_element('id', 'hondacheck').click()
        print("bmwradio Radio button is selected: " + str(bmwradio.is_selected()))
        print("hondaradio Radio button is selected: " + str(hondaradio.is_selected()))

        ##### DropDown #####
        element = self.driver.find_element('id', 'carselect')
        sel = Select(element)
        sel.select_by_value('benz')
        print("Select by value")
        sel.select_by_index("2") #Index as a string
        print("Select by index")
        sel.select_by_visible_text('BMW')
        print("Select by visible text")
        sel.select_by_index(2) #Index as a number
        print("Select by index")
        time.sleep(10)
        #count number of options in dropdown
        all_options = sel.options
        for options in all_options:
            print(options.text)


        #################### select all the radio button options - Loop #################
    def loops(self):
        #driver = webdriver.Firefox()
        #driver.get(baseUrl)
        radioButtonsList = self.driver.find_elements(
            'xpath', "//input[contains(@type, 'radio') and contains(@name, 'cars')]")
        size = len(radioButtonsList)
        print(size)

        for radioButtons in radioButtonsList:
            isSelected = radioButtons.is_selected()

            if not isSelected:
                radioButtons.click()
        time.sleep(10)
        print("loop is completed")
        #self.driver.close()

    def hideButton(self):
        #driver = webdriver.Firefox()
        #driver.get(baseUrl)
        #time.sleep(10)
        textbox = self.driver.find_element('id', 'displayed-text')
        textBoxState = textbox.is_displayed()
        print("Textbox is enabled?: " +str(textBoxState))

        # click on Hide button and check the state
        self.driver.find_element('id', 'hide-textbox').click()
        textbox = self.driver.find_element('id', 'displayed-text')
        textBoxState = textbox.is_displayed()
        print("Textbox is enabled?: " + str(textBoxState))

        # Click on show button on find the state
        self.driver.find_element('id', 'show-textbox').click()
        textbox = self.driver.find_element('id', 'displayed-text')
        textbox.send_keys('Testing')
        time.sleep(10)
        textBoxState = textbox.is_displayed()
        print("Textbox is enabled?: " + str(textBoxState))

        ### Using Dynamic Xpath - Useful whenever we find duplicate locators###
    def dynamicXpath(self):
        self.driver.get(baseUrl + 'login')
        time.sleep(2)
        self.driver.find_element('id', 'email').send_keys('test@email.com')
        self.driver.find_element('id', 'password').send_keys('abcabc')
        self.driver.find_element('xpath', "//input[@value='Login']").click()
        time.sleep(5)


        # Select Course
        link = "//a[contains(@class, 'dynamic-link') and contains(text(), '{0}')]"
        ele = link.format('ALL COURSES')
        self.driver.find_element('xpath', ele).click()
        time.sleep(5)
        self.driver.find_element('name', 'course').send_keys("JavaScript")

        self.driver.find_element('xpath', "//button[@type='submit']").click()
        #course = "//div[contains(@class, 'dynamic-heading) and contains(text(), 'JavaScript for beginners')]"
        course = "//h4[contains(@class, 'dynamic-heading') and contains(text(), '{0}')]" # {0}->to replace with actual text
        courseElement = course.format('JavaScript for beginners')
        print(courseElement)
        self.driver.find_element('xpath', courseElement).click()
        time.sleep(5)
        self.driver.close()


'''obj = LetsCode()
obj.allFields()
obj.loops()
obj.hideButton()'''

