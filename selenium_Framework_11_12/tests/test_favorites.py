from core.base_test import BaseTest
from pages.main_page import MainPage
from pages.product_page import ProductPage

class FavoritesTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.main_page.accept_cookies()

    def test_add_to_favorites(self):
        initial_count = self.main_page.get_wishlist_count()
        self.main_page.navigate_to_category('Бюстгальтеры')

        self.product_page.add_to_favorites(0)
        current_count = self.main_page.get_wishlist_count()
        self.assertEqual(current_count, initial_count + 1, "Item was not added to wishlist")
