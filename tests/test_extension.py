import platform
import time
from get_gecko_driver import GetGeckoDriver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def test_extension():
    # Install the driver:
    # Downloads the latest GeckoDriver version
    # Adds the downloaded GeckoDriver to path
    get_driver = GetGeckoDriver()
    get_driver.install()

    options = Options()
    if platform.system() == "Windows":
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    # Use the installed GeckoDriver with Selenium
    driver = webdriver.Firefox(options=options)
    driver.get('http://google.com/')
    time.sleep(4)
    driver.quit()
