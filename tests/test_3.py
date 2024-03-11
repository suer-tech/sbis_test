import pytest

from conftest import download_dir
from pages.download_sbis_page import DownloadSbisPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("browser", "logger")
def test_download_plugin(browser, logger):
    url = 'https://sbis.ru/'
    home_page = HomePage(browser, url)
    home_page.open_download_sbis_page()
    logger.info("Ссылка 'Скачать СБИС' успешно найдена.")

    download_sbis_page = DownloadSbisPage(browser, browser.current_url)
    download_sbis_page.go_to_sbis_plugin()
    download_sbis_page.open_page_for_windows()
    download_sbis_page.download_plugin()
    logger.info("Файл плагина найден, началась загрузка.")

    file_name = "sbisplugin-setup-web.exe"
    download_sbis_page.check_download_plugin(download_dir, file_name)
    logger.info("Файл скачан")

    download_sbis_page.check_plugin_size(download_dir, file_name)
    logger.info("Размер файла верный.")
