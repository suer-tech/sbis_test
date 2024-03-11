import os
import time

from locators import Locator
from pages.base_page import BasePage


class DownloadSbisPage(BasePage):
    def go_to_sbis_plugin(self):
        sbis_plugin = self.find_element(Locator.SBIS_PLUGIN)
        assert self.check_element(Locator.SBIS_PLUGIN) is True, "Не найден раздел 'СБИС Плагин'"
        self.browser.execute_script("arguments[0].click();", sbis_plugin)

    def open_page_for_windows(self):
        assert self.check_element(Locator.WINDOWS) is True, "Не найден раздел 'WINDOWS'"
        page_for_windows = self.find_element(Locator.WINDOWS)
        page_for_windows.click()

    def download_plugin(self):
        assert self.check_element(Locator.DOWNLOAD_PLUGIN_LINK) is True, "Не найден файл плагина для скачивания"
        download_plugin_link = self.find_element(Locator.DOWNLOAD_PLUGIN_LINK)
        download_plugin_link.click()

    def check_download_plugin(self, download_dir, file_name, timeout=60):
        start_time = time.time()
        while True:
            file_path = os.path.join(download_dir, file_name)
            if os.path.exists(file_path):
                return  # Файл скачан
            if time.time() - start_time > timeout:
                assert False, 'Плагин не был скачан'

    def check_plugin_size(self, download_dir, file_name):
        plugin_size = Locator.DOWNLOAD_PLUGIN_SIZE
        file_path = os.path.join(download_dir, file_name)
        if os.path.exists(file_path):
            file_size = round(os.path.getsize(file_path) / (1024 * 1024), 2)
            assert plugin_size == file_size, 'Неверный размер скачанного файла'
        else:
            assert False, 'Файл не существует'