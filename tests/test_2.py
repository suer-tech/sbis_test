import time

from pages.contact_page import ContactPage
from pages.home_page import HomePage


def test_go_to_contacts(browser):
    url = 'https://sbis.ru/'
    home_page = HomePage(browser, url)
    home_page.open_contacts_page()


def test_region_and_partners_list(browser):
    region = "Республика Башкортостан"
    partners_city = "Уфа"

    url = 'https://sbis.ru/'
    home_page = HomePage(browser, url)
    home_page.open_contacts_page()
    contact_page = ContactPage(browser, browser.current_url)
    contact_page.check_current_region(region)
    contact_page.check_partners_list(partners_city)


def test_modify_region(browser):
    region_to_replace = "Камчатский край"
    partners_city = "Петропавловск-Камчатский"

    url = 'https://sbis.ru/'
    home_page = HomePage(browser, url)
    home_page.open_contacts_page()
    contact_page = ContactPage(browser, browser.current_url)
    contact_page.modify_region(region_to_replace)
    time.sleep(3)
    contact_page.check_current_region(region_to_replace)
    contact_page.check_partners_list(partners_city)
    contact_page.check_url_and_title()




