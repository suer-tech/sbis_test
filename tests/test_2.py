import time

import pytest

from pages.contact_page import ContactPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("browser", "logger")
def test_go_to_contacts(browser, logger):
    url = 'https://sbis.ru/'
    home_page = HomePage(browser, url)
    home_page.open_contacts_page()
    logger.info("Успешное открытие страницы 'Контакты'.")


@pytest.mark.usefixtures("browser", "logger")
def test_region_and_partners_list(browser, logger):
    region = "Республика Башкортостан"
    partners_city = "Уфа"

    url = 'https://sbis.ru/'
    home_page = HomePage(browser, url)
    home_page.open_contacts_page()
    contact_page = ContactPage(browser, browser.current_url)
    contact_page.check_current_region(region)
    logger.info("Регион определился успешно.")

    contact_page.check_partners_list(partners_city)
    logger.info("Список партнеров определился успешно.")


@pytest.mark.usefixtures("browser", "logger")
def test_modify_region(browser, logger):
    region_to_replace = "Камчатский край"
    partners_city = "Петропавловск-Камчатский"

    url = 'https://sbis.ru/'
    home_page = HomePage(browser, url)
    home_page.open_contacts_page()
    contact_page = ContactPage(browser, browser.current_url)
    contact_page.modify_region(region_to_replace)
    time.sleep(3)

    contact_page.check_current_region(region_to_replace)
    logger.info("Регион изменён успешно.")

    contact_page.check_partners_list(partners_city)
    logger.info("Список партнеров изменён успешно.")

    contact_page.check_url_and_title()
    logger.info("Url и title содержит информацию выбранного региона.")




