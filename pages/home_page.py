from locators import Locator
from pages.base_page import BasePage


class HomePage(BasePage):

    def open_contacts_page(self):
        self.go_to_site()
        contact_link = self.find_element(Locator.CONTACTS)
        contact_link.click()

    def open_download_sbis_page(self):
        self.go_to_site()
        download_link = self.find_element(Locator.DOWNLOAD_SBIS)
        download_link.click()