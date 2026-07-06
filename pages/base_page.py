from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class BasePage:
    #---initializer---
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger(self.__class__.__name__)

    #---action methods---
    def get_url(self,url):
        self.logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def find_element(self,locator):
        self.logger.info(f"Finding element: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self,locator):
        self.logger.info(f"Clicking element: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self,locator,text):
        self.logger.info(f"Typing into element: {text}")
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self,locator):
        return self.find_element(locator).text

