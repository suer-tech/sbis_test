from locators import Locator
from pages.base_page import BasePage


class TenzorAbout(BasePage):

    def go_to_power_in_people_block_details(self):
        details = self.find_element(Locator.POWER_IN_PEOPLE_BLOCK_DETAILS)
        if details:
            sila_details = details[3]
            sila_details.click()

    def find_working_block(self):
        try:
            block_working = self.find_element(Locator.WORKING)
            return True
        except:
            return False

    def check_width_and_height_images(self):
        images = self.find_elements(Locator.IMAGE)
        first_image_size = (images[0].size['width'], images[0].size['height'])

        for image in images[1:]:
            size = (image.size['width'], image.size['height'])
            assert size == first_image_size, "Размеры изображений не совпадают"