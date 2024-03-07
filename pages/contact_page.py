from locators import Locator
from pages.base_page import BasePage


class ContactPage(BasePage):

    def open_tensor_banner(self):
        tensor_banner = self.find_element(Locator.TENZOR_BANNER)
        tensor_banner.click()

    def switch_to_tensor_home_page(self):
        windows = self.browser.window_handles
        if len(windows) > 1:
            self.browser.switch_to.window(windows[-1])

        assert (
                "https://tensor.ru/" in self.browser.current_url
        ), "Ошибка открытия страницы tensor.ru из раздела Контакты"