
from locators import Locator
from pages.base_page import BasePage


class HomePage(BasePage):

    def open_contacts_page(self):
        self.go_to_site()
        assert self.check_element(Locator.CONTACTS) is True, "Не найден раздел 'Контакты'"
        contact_link = self.find_element(Locator.CONTACTS)
        contact_link.click()

    def open_download_sbis_page(self):
        self.go_to_site()
        assert self.check_element(Locator.DOWNLOAD_SBIS) is True, "Не найден элемент 'Скачать СБИС'"

        download_link = self.find_element(Locator.DOWNLOAD_SBIS)
        self.browser.execute_script("arguments[0].click();", download_link)
