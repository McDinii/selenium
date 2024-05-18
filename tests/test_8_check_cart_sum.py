import time
import unittest
from selenium import webdriver
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from constansts import CHROME_DRIVER_PATH


class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        # Add necessary Chrome options if needed
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)
        self.driver.get('https://hunkemoller.by')
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.main_page.accept_cookies()

    def test_price_calculation(self):
        self.main_page.navigate_to_category('Бюстгальтеры')

        # Получаем начальную стоимость корзины
        initial_total = self.cart_page.get_cart_total()

        # Покупаем два товара и получаем их цены
        price1 = self.product_page.select_and_buy_product(0, 'C80')  # Размер C80
        price2 = self.product_page.select_and_buy_product(1, 'C80')  # Размер C80

        # Проверяем, что оба товара успешно добавлены
        if price1 is None or price2 is None:
            self.fail("Не удалось выбрать и купить один или оба товара.")

        # Ожидаемая общая стоимость в корзине
        expected_total_cart = initial_total + price1 + price2

        self.cart_page.go_to_shopping_cart()
        actual_total = self.cart_page.get_cart_total()
        self.assertEqual(expected_total_cart, actual_total, f"Ожидалось {expected_total_cart}, но в корзине {actual_total}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
