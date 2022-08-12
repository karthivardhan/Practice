from selenium import webdriver
from makeMyTrip import MakeMyTripSite

class MakeMyTripTest():
    def test(self):
        baseUrl = "https://www.makemytrip.com"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        var = MakeMyTripSite(driver)
        var.flights()

obj = MakeMyTripTest()
obj.test()


