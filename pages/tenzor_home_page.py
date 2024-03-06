from locators import Locator
from pages.base_page import BasePage


class TenzorHomePage(BasePage):
    def check_power_in_people_block(self):
        try:
            power_in_people_block = self.find_element(Locator.POWER_IN_PEOPLE_BLOCK)
            return True
        except:
            return False