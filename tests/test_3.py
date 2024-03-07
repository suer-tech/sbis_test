from pages.download_sbis_page import DownloadSbisPage
from pages.home_page import HomePage


def test_go_to_download_sbis(browser):
    url = 'https://sbis.ru/'
    home_page = HomePage(browser, url)
    home_page.open_download_sbis_page()


def test_download_plugin(browser):
    url = 'https://sbis.ru/'
    home_page = HomePage(browser, url)
    home_page.open_download_sbis_page()
    download_sbis_page = DownloadSbisPage(browser, browser.current_url)
    download_sbis_page.go_to_sbis_plugin()
    download_sbis_page.open_page_for_windows()




