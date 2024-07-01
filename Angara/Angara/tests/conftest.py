import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from Angara.utils import config
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setUp():
    if config.Driver.lower() == "chrome":
        chrome_options = Options()
        option = webdriver.ChromeOptions()
        if config.Headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
        else:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            driver.get(config.base_url)
            driver.maximize_window()
            yield driver
            driver.quit()


    elif config.Driver.lower() == "firefox":
        firefox_options = FirefoxOptions()
        if config.Headless:
            firefox_options.add_argument("--headless")

        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
        driver.maximize_window()
        yield driver
        driver.quit()
    else:
        print("Browser not supported. Suggested values are [Chrome,Firefox]")

    return driver
