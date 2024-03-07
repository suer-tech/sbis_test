from locators import Locator
from pages.base_page import BasePage


class TenzorHomePage(BasePage):
    def check_power_in_people_block(self):
        assert self.find_element(Locator.POWER_IN_PEOPLE_BLOCK), "Раздел 'Сила в людях' не найден"

    def go_to_power_in_people_block_details(self):
        details = self.find_element(
            Locator.POWER_IN_PEOPLE_BLOCK_DETAILS
        )
        self.browser.execute_script("arguments[0].click();", details)

        assert (
                "https://tensor.ru/about" == self.browser.current_url
        ), "Ошибка открытия страницы 'Подробнее' из раздела 'Сила в людях'"
