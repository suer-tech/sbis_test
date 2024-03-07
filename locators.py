from selenium.webdriver.common.by import By


class Locator:
    CONTACTS = (By.XPATH, "//a[text()='Контакты']")

    TENZOR_BANNER = (By.XPATH, "//a[@href='https://tensor.ru/']")

    POWER_IN_PEOPLE_BLOCK = (By.XPATH, "//div[@class='tensor_ru-Index__block4-bg']")
    POWER_IN_PEOPLE_BLOCK_DETAILS = (By.CSS_SELECTOR, "a.tensor_ru-link[href='/about']")

    WORKING = (By.XPATH, "//h2[text()='Работаем']")
    IMAGE = (By.XPATH, "//div[@class='tensor_ru-About__block3-image-wrapper']")