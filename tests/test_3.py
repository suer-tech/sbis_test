from pages.home_page import HomePage


def test_go_to_download_sbis(browser):
    url = 'https://sbis.ru/'
    home_page = HomePage(browser, url)
    home_page.open_download_sbis_page()