from selenium.webdriver.common.by import By
from locators import Locator
from pages.base_page import BasePage


class ContactPage(BasePage):

    def open_tensor_banner(self):
        assert self.check_element(Locator.TENZOR_BANNER) is True, "Не найден беннер Тензор"
        tensor_banner = self.find_element(Locator.TENZOR_BANNER)
        tensor_banner.click()

    def switch_to_tensor_home_page(self):
        windows = self.browser.window_handles
        if len(windows) > 1:
            self.browser.switch_to.window(windows[-1])

        assert (
                "https://tensor.ru/" in self.browser.current_url
        ), "Ошибка открытия страницы tensor.ru из раздела Контакты"

    def check_current_region(self, region):
        assert self.check_element(Locator.REGION) is True, "Не найден раздел выбора региона"
        current_region = self.find_element(Locator.REGION)
        assert current_region.text == region, f"Ошибка определения региона: ({current_region.text}) вместо ({region})"

    def check_partners_list(self, city):
        assert self.check_element(Locator.PARTNERS_LIST) is True, "Не найден раздел с партнерами региона"
        partners_lists = self.find_element(Locator.PARTNERS_LIST)
        partners_city = self.find_element(Locator.CITY)
        assert partners_lists, "Ошибка получения списка партнеров"
        assert partners_city.text == city, f"Ошибка определения списка партнеров: ({partners_city.text}) вместо ({city})"

    def modify_region(self, region_to_replace):
        region_to_replace_locator = (By.XPATH, f"//span[@title='{region_to_replace}']/span")
        region = self.find_element(Locator.REGION)
        region.click()
        modified_region = self.find_element(region_to_replace_locator)
        modified_region.click()

    def check_url_and_title(self):
        current_url = self.browser.current_url
        title = self.browser.title
        assert "kamchatskij-kraj" in current_url, "URL не содержит 'kamchatskij-kraj'"
        assert "Камчатский край" in title, f"Заголовок '{title}' не содержит ожидаемый текст 'Камчатский край'"

