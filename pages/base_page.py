from selenium.webdriver.support import expected_conditions as EC

from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def go_to_site(self):
        return self.browser.get(self.url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
            )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def check_element(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True