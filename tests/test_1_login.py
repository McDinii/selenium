import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from constansts import CHROME_DRIVER_PATH

class TestLogin(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)
        self.login_page = LoginPage(self.driver)

    def test_login(self):
        self.login_page.navigate()
        self.login_page.login('+375 29 335 46 77', '43835')
        # Проверка, что пользователь авторизован (можно проверить наличие какого-либо элемента личного кабинета)
        self.assertTrue("личная информация" in self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
