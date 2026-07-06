import pytest
import allure
from pages.sauce_demo_login_page import SauceDemoLoginPage
from utils.excel_reader import get_test_data

test_data = get_test_data()

@pytest.mark.parametrize("username,password", test_data)
@allure.feature("SauceDemo Login")
def test_sauce_demo_login(driver, username, password):

    login_page = SauceDemoLoginPage(driver)
    allure.dynamic.title(f"SauceDemo Login Test - User: {username}")

    #Opens URL from config.yaml automatically
    with allure.step("Open SauceDemo login page"):
        login_page.open_login_page()

    #Perform Login
    with allure.step(f"Login with username: {username}"):
        login_page.login(username, password)

    # with allure.step("Verify Successful Login (Intentional Failure)"):
    #     assert False, "This is Intentional Failure ScreenShot for Allure"

# def test_addition():
#     assert 12+3 == 15 # True
#     # assert 13+2==20 # False