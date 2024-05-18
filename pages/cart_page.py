from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_shopping_cart(self):
        cart_icon = self.driver.find_element(By.CSS_SELECTOR, "icon_for_cart_css_selector")
        cart_icon.click()

    def get_cart_total(self):
        # Wait for the cart total to update
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, ".minicart-total").text.strip() != "0.00"
        )
        total_price_element = self.driver.find_element(By.CSS_SELECTOR, ".minicart-total")
        total_price = total_price_element.text.strip('BYN').strip()
        return float(total_price) if total_price else 0.0
