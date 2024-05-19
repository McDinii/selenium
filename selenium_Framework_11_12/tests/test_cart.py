from core.base_test import BaseTest
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

class ShoppingCartTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.main_page.accept_cookies()

    def test_price_calculation(self):
        self.main_page.navigate_to_category('Бюстгальтеры')
        initial_total = self.cart_page.get_cart_total()

        price1 = self.product_page.select_and_buy_product(0, 'C80')
        price2 = self.product_page.select_and_buy_product(1, 'C80')

        if price1 is None or price2 is None:
            self.fail("Не удалось выбрать и купить один или оба товара.")

        expected_total_cart = initial_total + price1 + price2

        self.cart_page.go_to_shopping_cart()
        actual_total = self.cart_page.get_cart_total()
        self.assertEqual(expected_total_cart, actual_total, f"Ожидалось {expected_total_cart}, но в корзине {actual_total}")
