
def test_pets_list():
    # Явное ожидание загрузки таблицы питомцев
    pets_table = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table-hover")))

    # Получаем список всех строк таблицы
    pets_rows = pets_table.find_elements_by_tag_name('tr')

    # Проверяем, что присутствуют все питомцы
    assert len(pets_rows) == 9

    # Создаем словарь, где ключами являются имена питомцев,
    # а значениями - списки соответствующих строк таблицы
    pets_dict = {}
    for row in pets_rows[1:]:
        pet_name = row.find_element_by_css_selector("a[class='text-info']").text
        if pet_name not in pets_dict:
            pets_dict[pet_name] = [row]
        else:
            pets_dict[pet_name].append(row)

    # Проверяем, что у всех питомцев есть фото, имя, возраст и порода,
    # а также разные имена и отсутствие повторяющихся питомцев
    for pet_name, pet_rows in pets_dict.items():
        assert len(pet_rows) == 1
        pet_row = pet_rows[0]
        assert pet_row.find_element_by_tag_name('img').get_attribute('src') != ''
        assert pet_row.find_element_by_css_selector('td:nth-child(2)').text != ''
        assert pet_row.find_element_by_css_selector('td:nth-child(3)').text != ''
        assert pet_row.find_element_by_css_selector('td:nth-child(4)').text != ''
    assert len(pets_dict) == len(pets_rows) - 1
    
# Неявные ожидания всех элементов (фото, имя питомца, его возраст)
pet_images = pytest.driver.find_elements_by_css_selector('.table-hover td img')
# Находим все изображения на странице
for image in pet_images:
    assert image.get_attribute('src') != '' # Проверяем, что у каждого изображения есть src

pet_names = pytest.driver.find_elements_by_css_selector('.table-hover td:nth-child(2)')
# Находим все элементы с именами питомцев
for name in pet_names:
    assert name.text != ''
    # Проверяем, что у каждого имени есть текст

pet_ages = pytest.driver.find_elements_by_css_selector('.table-hover td:nth-child(3)')
# Находим все элементы с возрастами питомцев
for age in pet_ages:
    assert age.text != '' # Проверяем, что у каждого возраста есть текст
    
    
    import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Определяем параметры входа в аккаунт
valid_email = 'valid_email@mail.com'
valid_password = 'valid_password'

# Запускаем браузер и переходим на страницу авторизации
driver = webdriver.Chrome()
driver.get('https://petfriends.skillfactory.ru/login')

# Вводим email
email_field = driver.find_element(By.ID, 'email')
email_field.clear()
email_field.send_keys(valid_email)

# Вводим пароль
password_field = driver.find_element(By.ID, 'pass')
password_field.clear()
password_field.send_keys(valid_password)

# Нажимаем на кнопку входа в аккаунт
login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
login_button.click()

# Явное ожидание загрузки страницы со списком питомцев
pets_page_loaded = WebDriverWait(driver, 10).until(EC.url_to_be('https://petfriends.skillfactory.ru/my_pets'))

# Проверяем, что страница загрузилась корректно
assert pets_page_loaded

# Явное ожидание появления таблицы питомцев
pets_table_visible = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".table-hover")))

# Проверяем, что таблица питомцев появилась на странице
assert pets_table_visible

# Явное ожидание появления кнопки добавления нового питомца
new_pet_button_visible = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/my_pets/new']")))

# Проверяем, что кнопка добавления нового питомца появилась на странице
assert new_pet_button_visible

# Явное ожидание загрузки списка пород питомцев
breeds_loaded = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#create_pet select[name='species'] option")))

# Проверяем, что список пород питомцев загрузился корректно
assert len(breeds_loaded.find_elements(By.TAG_NAME, "option")) > 0

# Явное ожидание загрузки списка владельцев питомцев
owners_loaded = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#create_pet select[name='owner'] option")))

# Проверяем, что список владельцев питомцев загрузился корректно
assert len(owners_loaded.find_elements(By.TAG_NAME, "option")) > 0

# Закрываем браузер
driver.quit()


    
    
