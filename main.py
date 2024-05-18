from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Путь к драйверу браузера
driver_path = 'путь/к/твоему/драйверу/chromedriver'

# Инициализация драйвера
driver = webdriver.Chrome(executable_path=driver_path)

# Открытие страницы
driver.get("http://www.google.com")

# Проверка заголовка страницы
assert "Google" in driver.title

# Закрытие браузера
driver.close()
