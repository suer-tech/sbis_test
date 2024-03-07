from pages.contact_page import ContactPage
from pages.home_page import HomePage
from pages.tenzor_about_page import TenzorAbout
from pages.tenzor_home_page import TenzorHomePage


def test_go_to_contacts(browser):
    url = 'https://sbis.ru/'
    home_page = HomePage(browser, url)
    home_page.open_contacts_page()


def test_open_tenzor_baanner(browser):
    url = 'https://sbis.ru/'
    home_page = HomePage(browser, url)
    home_page.open_contacts_page()
    contact_page = ContactPage(browser, browser.current_url)
    contact_page.open_tensor_banner()
    contact_page.switch_to_tensor_home_page()


def test_power_in_people_block(browser):
    url = 'https://tensor.ru/'
    tenzor_home_page = TenzorHomePage(browser, url)
    tenzor_home_page.go_to_site()
    tenzor_home_page.check_power_in_people_block()


def test_open_power_in_people_block_details(browser):
    url = 'https://tensor.ru/'
    tenzor_home_page = TenzorHomePage(browser, url)
    tenzor_home_page.go_to_site()
    tenzor_home_page.go_to_power_in_people_block_details()


def test_width_and_height_images(browser):
    url = 'https://tensor.ru/about'
    tenzor_about = TenzorAbout(browser, url)
    tenzor_about.go_to_site()
    tenzor_about.find_working_block()
    tenzor_about.check_width_and_height_images()