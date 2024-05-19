from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from constansts import CHROME_DRIVER_PATH

class BrowserManager:
    @staticmethod
    def get_driver():
        options = Options()
        driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)
        return driver
