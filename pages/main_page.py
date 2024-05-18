from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
    def accept_cookies(self):
        try:
            # Wait for the cookie acceptance button to be clickable and then click it
            accept_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success[onclick='acceptCookiesBlock()']"))
            )
            accept_button.click()
        except Exception as e:
            print("Cookie acceptance button not found or not clickable.", str(e))
    def navigate_to_category(self, category_name):
        if category_name == 'Бюстгальтеры':
            category_path = "#mainmenu2 > span"
        link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, category_path))
        )
        link.click()

    def get_wishlist_count(self):
        # Return the current number of items in the wishlist or 0 if none
        try:
            count_element = self.driver.find_element(By.CSS_SELECTOR, ".item-count-wish")
            return int(count_element.text)
        except:
            return 0