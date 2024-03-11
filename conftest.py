import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import logging


download_dir = os.path.join(os.path.dirname(__file__), 'tests')


@pytest.fixture()
def browser():
    chrome_options = Options()
    prefs = {"download.default_directory": download_dir}
    chrome_options.add_experimental_option("prefs", prefs)

    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.quit()


@pytest.fixture(scope="function")
def logger():
    logger = logging.getLogger("automation_testing_logger")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    fh = logging.FileHandler("log_file.log", encoding="utf-8")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger


