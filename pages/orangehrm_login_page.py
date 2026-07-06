# from pages import base_page # entire Page
from pages.base_page import BasePage # import particular class from page

class OrangeHrmLoginPage(BasePage): # single level inheritance

    # ----locators----

    USERNAME_FIELD = ("name","username")
    PASSWORD_FIELD = ("name","password")
    LOGIN_BUTTON = ("xpath",'//button[@type="submit"]')
    ERROR_MESSAGE = ("css selector",'[class="oxd-alert-content oxd-alert-content--error"]')

    def open_orangehrm_login_page(self,base_url):
        self.get_url(base_url)

    def enter_username(self,username):
        self.send_keys(self.USERNAME_FIELD,username)

    def enter_password(self,password):
        self.send_keys(self.PASSWORD_FIELD,password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    #----Business Method----

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()