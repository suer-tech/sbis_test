from locators import Locator
from pages.base_page import BasePage


class HomePage(BasePage):

    def open_contacts_page(self):
        self.go_to_site()
        contact_link = self.find_element(Locator.CONTACTS)
        contact_link.click()

