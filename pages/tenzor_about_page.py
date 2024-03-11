from locators import Locator
from pages.base_page import BasePage


class TenzorAbout(BasePage):
    def find_working_block(self):
        assert self.check_element(Locator.WORKING) is True, "Не найден раздел 'Работаем'"

    def check_width_and_height_images(self):
        assert self.check_element(Locator.IMAGE) is True, "Не найден блок с изображениями"
        images = self.find_elements(Locator.IMAGE)
        first_image_size = (images[0].size['width'], images[0].size['height'])

        for image in images[1:]:
            size = (image.size['width'], image.size['height'])
            assert size == first_image_size, "Размеры изображений не совпадают"