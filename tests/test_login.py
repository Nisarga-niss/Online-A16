# from selenium import webdriver
import pytest
import allure
from pages.login_page import LoginPage
from tests.base_test import BaseTest

@pytest.mark.smoke
@allure.feature("Login Feature")
class TestLogin(BaseTest):

    @pytest.mark.regression
    @allure.title("Verify user can login with valid credentials")
    def test_valid_login(self):
        self.logger.info("Starting valid login test")
        env = self.config["environments"]["practice_test_automation"]

        with allure.step("Open Login Page"):
            login_page = LoginPage(self.driver)
            login_page.open_login_page(env["base_url"])
            self.logger.info("Opened login page")

        with allure.step("Enter valid credentials and login"):
            login_page.login(env["valid_username"],env["valid_password"])
            self.logger.info("Entered valid credentials")

        assert "Logged In Successfully" in login_page.get_success_message()
        self.logger.info("Valid login test passed")

    @pytest.mark.regression
    @allure.title("Verify user can login with invalid credentials")
    def test_invalid_login(self):

        self.logger.info("Starting Invalid login test")
        env = self.config["environments"]["practice_test_automation"]


        with allure.step("Open Login Page"):
            login_page = LoginPage(self.driver)
            login_page.open_login_page(env["base_url"])
            self.logger.info("Opened login page")

        with allure.step("Enter invalid credentials and login"):
            login_page.login(env["invalid_username"],env["invalid_password"])

        assert "Your username is invalid!" in login_page.get_error_message()
        self.logger.info("Invalid login test passed")