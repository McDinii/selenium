from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_favorites(self, product_index):
        heart_icon = self.driver.find_element(By.CSS_SELECTOR, "a.link-wishlist.icons-heart-lightgray")
        ActionChains(self.driver).move_to_element(heart_icon).click(heart_icon).perform()


    def go_to_favorites(self):
        self.driver.find_element(By.CSS_SELECTOR, 'selector_for_favorites_page').click()

    def verify_product_in_favorites(self):
        # Проверяем наличие товара в избранном
        return "expected_text_or_element" in self.driver.page_source

    def select_and_buy_product(self, product_index, size_text):
        try:
            # Находим все карточки товаров
            products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card.product.app-card"))
            )
            product = products[product_index]

            # Прокручиваем до карточки товара
            self.driver.execute_script("arguments[0].scrollIntoView(true);", product)

            # Находим выпадающий список размеров
            size_dropdown = product.find_element(By.CSS_SELECTOR, "select.custom-select.select-attr")

            # Проверяем наличие нужного размера
            sizes = size_dropdown.find_elements(By.TAG_NAME, "option")
            size_found = False
            for size in sizes:
                if size.text.strip() == size_text:
                    size_found = True
                    break

            if not size_found:
                raise NoSuchElementException(f"Размер {size_text} не найден в списке доступных размеров.")

            # Кликаем на выпадающий список и выбираем нужный размер
            size_dropdown.click()
            for size in sizes:
                if size.text.strip() == size_text:
                    self.driver.execute_script("arguments[0].click();", size)
                    break

            # Ждем, пока кнопка "Купить" станет активной
            WebDriverWait(product, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-hkm-dark.px-2.link-add-to-cart:not(.app-disabled)"))
            )

            # Нажимаем на кнопку "Купить"
            buy_button = product.find_element(By.CSS_SELECTOR, "button.btn.btn-hkm-dark.px-2.link-add-to-cart")
            buy_button.click()

            # Получаем цену товара из карточки
            price_element = product.find_element(By.CSS_SELECTOR, "meta[itemprop='price']")
            price = price_element.get_attribute("content")
            return float(price)
        except (NoSuchElementException, ElementClickInterceptedException, TimeoutException) as e:
            print(f"Ошибка при выборе и покупке товара: {str(e)}")
            return None