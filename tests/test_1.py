import pytest

from pages.contact_page import ContactPage
from pages.home_page import HomePage
from pages.tenzor_about_page import TenzorAbout
from pages.tenzor_home_page import TenzorHomePage


@pytest.mark.usefixtures("browser", "logger")
def test_go_to_contacts(browser, logger):
    url = 'https://sbis.ru/'
    home_page = HomePage(browser, url)
    home_page.open_contacts_page()
    logger.info("Успешное открытие страницы 'Контакты'.")


@pytest.mark.usefixtures("browser", "logger")
def test_open_tenzor_baanner(browser, logger):
    url = 'https://sbis.ru/'
    home_page = HomePage(browser, url)
    home_page.open_contacts_page()
    contact_page = ContactPage(browser, browser.current_url)
    contact_page.open_tensor_banner()
    contact_page.switch_to_tensor_home_page()
    logger.info("Успешное открытие страницы https://tensor.ru/.")


@pytest.mark.usefixtures("browser", "logger")
def test_power_in_people_block(browser, logger):
    url = 'https://tensor.ru/'
    tenzor_home_page = TenzorHomePage(browser, url)
    tenzor_home_page.go_to_site()
    tenzor_home_page.check_power_in_people_block()
    logger.info("Раздел 'Cила в людях' успешно найден.")


@pytest.mark.usefixtures("browser", "logger")
def test_open_power_in_people_block_details(browser, logger):
    url = 'https://tensor.ru/'
    tenzor_home_page = TenzorHomePage(browser, url)
    tenzor_home_page.go_to_site()
    tenzor_home_page.go_to_power_in_people_block_details()
    logger.info("Успешный переход в 'Подробнее'.")


@pytest.mark.usefixtures("browser", "logger")
def test_width_and_height_images(browser, logger):
    url = 'https://tensor.ru/about'
    tenzor_about = TenzorAbout(browser, url)
    tenzor_about.go_to_site()
    tenzor_about.find_working_block()
    tenzor_about.check_width_and_height_images()
    logger.info("Проверка размеров изображений завершена.")