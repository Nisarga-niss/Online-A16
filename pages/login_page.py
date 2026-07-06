from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class LoginPage(BasePage):

    #----locators---
    USERNAME_FIELD = (By.ID,"username")
    PASSWORD_FIELD = (By.ID,"password")
    SUBMIT_BUTTON = (By.ID,"submit")
    ERROR_MESSAGE = (By.ID,"error")
    SUCCESS_MESSAGE = (By.TAG_NAME,"h1")

    #---initializers---
    def open_login_page(self,base_url):
        self.get_url(f"{base_url}/practice-test-login/")

    #----action methods----
    def enter_username(self,username):
        self.send_keys(self.USERNAME_FIELD,username)
        print(f"Entered username: {username}")

    def enter_password(self,password):
        self.send_keys(self.PASSWORD_FIELD,password)
        print(f"Entered password: {password}")

    def click_submit(self):
        self.click(self.SUBMIT_BUTTON)
        print("submit button is clicked")

    #----business methods-----
    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()
        sleep(2)

    def get_success_message(self):
        return self.find_element(self.SUCCESS_MESSAGE).text

    def get_error_message(self):
        try:
            return self.get_text(self.ERROR_MESSAGE)
        except TimeoutException:
            return None