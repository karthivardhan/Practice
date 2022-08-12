from selenium import webdriver
import time

invalid_email = 'test1@test.com'

url = "http://demostore.supersqa.com/my-account/"

class InvalidLogin():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def page(self):
        self.driver.get(url)

    def email(self):
        email_field = self.driver.find_element('id', 'username')
        email_field.send_keys(invalid_email)

    def password(self):
        password_field = self.driver.find_element('id', 'password')
        password_field.send_keys('abcds')

    def login(self):
        self.driver.find_element('name', 'login').click()

    def errorMsg(self):
        err_ele = self.driver.find_element('xpath', '//*[@id="content"]/div/div[1]/ul')
        err_msg = err_ele.text
        assert err_msg == "Unknown email address. Check again or try your username."
        print(err_msg)
        self.driver.close()

    def main(self):
        self.page()
        self.email()
        self.password()
        self.login()
        self.errorMsg()

# if __name__ == '__main__':

obj = InvalidLogin()
obj.main()



