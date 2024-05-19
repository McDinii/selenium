import unittest
import time
from selenium import webdriver
from pages.main_page import MainPage
from pages.product_page import ProductPage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from constansts import CHROME_DRIVER_PATH


class FavoritesTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
        self.driver.get('https://hunkemoller.by')
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.main_page.accept_cookies()

    def test_add_to_favorites(self):
        self.main_page.navigate_to_category('Бюстгальтеры')
        time.sleep(3)
        initial_count = self.main_page.get_wishlist_count()
        assert initial_count == 0
        self.product_page.add_to_favorites(0)
        time.sleep(3)
        current_count = self.main_page.get_wishlist_count()
        assert current_count == initial_count + 1, "Item was not added to wishlist"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
