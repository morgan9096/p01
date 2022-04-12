from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://habr.com';

    def __find(self, presence, fail_message, timeout):
        return WebDriverWait(self.driver, timeout).until(presence, message=fail_message)

    def find_element(self, locator, timeout=10):
        fail_message = f'Cannot find element by locator ${locator}'
        return self.__find(EC.presence_of_element_located(locator), fail_message, timeout)


    def find_elements(self, locator, timeout=10):
        fail_message = f'Cannot find any elements by locator ${locator}'
        return self.__find(EC.presence_of_all_elements_located(locator), fail_message, timeout)

    def go_to_url(self):
        return self.driver.get(self.base_url)

    def press_enter(self, element):
        element.sendKeys(Keys.RETURN)