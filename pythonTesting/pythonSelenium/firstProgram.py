from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#driver = webdriver.Chrome(executable_path="/Users/apparaojajimoggala/PycharmProjects/chromedriver.exe")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://www.google.co.in/")
driver.maximize_window() # method to maximize window
print(driver.title)  # prints the title of the web
print(driver.current_url) # Prints current url of web
driver.get("https://www.google.co.in/imghp?hl=en&authuser=0&ogbl")  # Navigate to another page
driver.back()  # come back to previous page
driver.refresh()
driver.delete_all_cookies()