
from letsCodeIt import LetsCode

from selenium import webdriver

class TestFile():
    def testMethod(self):
        baseUrl = "https://courses.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.get(baseUrl + 'practice')
        hw = LetsCode(driver)

        hw.allFields()
        hw.loops()
        hw.hideButton()
        hw.dynamicXpath()

obj1 = TestFile()
obj1.testMethod()
