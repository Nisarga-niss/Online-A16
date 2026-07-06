import os
import yaml
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SauceDemoLoginPage(BasePage):

    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def get_base_url(self):
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(base_path, 'config','config.yaml')

        with open(config_path) as config_file:
            config = yaml.safe_load(config_file)

        return config["environments"]["sauce_demo"]["base_url"]

    def open_login_page(self):
        base_url = self.get_base_url()
        self.get_url(base_url)

    #-----Action Methods-----
    def enter_username(self, username):
        self.send_keys(self.USERNAME, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)

    def click_submit(self):
        self.click(self.LOGIN_BUTTON)

    #-----Business Method-----
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()