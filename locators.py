from selenium.webdriver.common.by import By


class Locator:
    CONTACTS = (By.XPATH, "//a[text()='Контакты']")

    TENZOR_BANNER = (By.XPATH, "//a[@href='https://tensor.ru/']")
    REGION = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    PARTNERS_LIST = (By.CSS_SELECTOR, "div[name='itemsContainer']")
    CITY = (By.ID, "city-id-2")

    POWER_IN_PEOPLE_BLOCK = (By.XPATH, "//div[@class='tensor_ru-Index__block4-bg']")
    POWER_IN_PEOPLE_BLOCK_DETAILS = (By.CSS_SELECTOR, "a.tensor_ru-link[href='/about']")

    WORKING = (By.XPATH, "//h2[text()='Работаем']")
    IMAGE = (By.XPATH, "//div[@class='tensor_ru-About__block3-image-wrapper']")

    DOWNLOAD_SBIS = (By.LINK_TEXT, 'Скачать локальные версии')
    SBIS_PLUGIN = (By.XPATH, "//div[@class='controls-TabButton controls-TabButton__right-align controls-ListView__item undefined ws-enabled ws-control-inactive ws-component' and ./div[@class='controls-TabButton__inner']/div[@class='controls-TabButton__wrapper']/div[@class='controls-TabButton__caption' and text()='СБИС Плагин']]")
    WINDOWS = (By.XPATH, '//span[text()="Windows"]')
    DOWNLOAD_PLUGIN_LINK = (By.XPATH, "//a[text()='Скачать (Exe 8.17 МБ) ']")
    DOWNLOAD_PLUGIN_SIZE = 8.17


