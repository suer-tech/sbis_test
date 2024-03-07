from locators import Locator
from pages.base_page import BasePage


class ContactPage(BasePage):

    def open_tensor_banner(self):
        tensor_banner = self.find_element(Locator.TENZOR_BANNER)
        tensor_banner.click()