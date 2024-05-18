from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://hunkemoller.by'
        self.login_button = (By.CSS_SELECTOR, 'селектор_кнопки_вход')
        self.phone_field = (By.CSS_SELECTOR, 'селектор_поля_телефон')
        self.code_field = (By.CSS_SELECTOR, 'селектор_поля_кода')
        self.submit_button = (By.CSS_SELECTOR, 'селектор_кнопки_войти')

    def navigate(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.login_button)).click()

    def login(self, phone, code):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.phone_field)).send_keys(phone)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.code_field)).send_keys(code)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.submit_button)).click()
