import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import valid_email, valid_password

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('/tests_drivers/chromedriver.exe')

    # Переходим на страницу авторизации
    pytest.driver.get('https://petfriends.skillfactory.ru/login')

    # Вводим email
    email_field = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    email_field.clear()
    email_field.send_keys(valid_email)

    # Вводим пароль
    password_field = pytest.driver.find_element_by_id('pass')
    password_field.clear()
    password_field.send_keys(valid_password)

    # Нажимаем на кнопку входа в аккаунт
    login_button = pytest.driver.find_element_by_css_selector('button[type="submit"]')
    login_button.click()

    # Переходим на страницу со списком питомцев
    pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')

    yield

    pytest.driver.quit()
