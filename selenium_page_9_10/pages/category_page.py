from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CategoryPage:
    def __init__(self, driver):
        self.driver = driver

    def select_item_and_buy(self, item_selector, size_selector, buy_button_selector):
        self.driver.find_element(By.CSS_SELECTOR, item_selector).click()
        self.driver.find_element(By.CSS_SELECTOR, size_selector).click()
        self.driver.find_element(By.CSS_SELECTOR, buy_button_selector).click()

    def go_to_cart(self, cart_button_selector):
        self.driver.find_element(By.CSS_SELECTOR, cart_button_selector).click()
