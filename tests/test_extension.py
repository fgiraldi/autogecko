import time
from get_gecko_driver import GetGeckoDriver
from selenium import webdriver


def test_extension():
    # Install the driver:
    # Downloads the latest GeckoDriver version
    # Adds the downloaded GeckoDriver to path
    get_driver = GetGeckoDriver()
    get_driver.install()

    # Use the installed GeckoDriver with Selenium
    driver = webdriver.Firefox()
    driver.get("https://google.com")
    time.sleep(4)
    driver.quit()
