# from pages.orangehrm_login_page import OrangeHrmLoginPage
# from selenium import webdriver
#
# def test_valid_login():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://opensource-demo.orangehrmlive.com/")
#     login_page = OrangeHrmLoginPage(driver)
#     # login_page.login("Admin","admin123")
#     # print("Login Test Passed")
#     login_page.enter_username("Admin")
#     login_page.enter_password("admin123")
#     login_page.click_login_button()
import pytest

from pages.orangehrm_login_page import OrangeHrmLoginPage
from utils.config_reader import ConfigReader
import allure

# @pytest.mark.smoke
@allure.feature("Orange Login")
def test_orangehrm_login(cross_browser_driver):
    config = ConfigReader.read_config()
    orange_config = config["environments"]["orange_hrm"]

    base_url = orange_config["base_url"]
    username = orange_config["username"]
    password = orange_config["password"]

    login_page = OrangeHrmLoginPage(cross_browser_driver)
    with allure.step("Open Orange login page"):
        login_page.open_orangehrm_login_page(base_url)
        login_page.login(username, password)