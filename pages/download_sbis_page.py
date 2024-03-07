from locators import Locator
from pages.base_page import BasePage


class DownloadSbisPage(BasePage):
    def go_to_sbis_plugin(self):
        sbis_plugin = self.find_element(Locator.SBIS_PLUGIN)
        sbis_plugin.click()

    def open_page_for_windows(self):
        page_for_windows = self.find_element(Locator.WINDOWS)
        page_for_windows.click()

    def download_plugin(self):
        download_plugin_link = self.find_element(Locator.DOWNLOAD_PLUGIN_LINK)
        download_plugin_link.click()



