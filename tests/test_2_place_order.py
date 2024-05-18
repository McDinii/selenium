import unittest
from selenium import webdriver
from pages.main_page import MainPage
from pages.category_page import CategoryPage


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='путь/к/драйверу/chromedriver')
        self.main_page = MainPage(self.driver)
        self.category_page = CategoryPage(self.driver)
        self.driver.get('https://hunkemoller.by')

    def test_order_process(self):
        # Перейти в категорию нижнего белья
        self.main_page.go_to_category('селектор_кнопки_нижнее_белье')

        # Выбор товара и добавление его в корзину
        self.category_page.select_item_and_buy('селектор_товара', 'селектор_размера_С70', 'селектор_кнопки_купить')
        self.category_page.go_to_cart('селектор_иконки_корзины')

        # Тут следует добавить проверки, подтверждающие добавление товара в корзину и правильность данных
        self.assertTrue("Итоговая сумма" in self.driver.page_source)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
