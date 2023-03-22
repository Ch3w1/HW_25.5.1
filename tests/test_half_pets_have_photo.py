import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_at_lest_half_pets_have_photo(open_page_my_pets):
    # Получаем количество питомцев и сохраняем в pets (2)
    element = element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".\\.col-sm-4.left" )))
    pets = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

    # Получаем данные о количестве фотографий питомцев и сохраняем в photo
    element = element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover img")))
    photo = pytest.driver.find_elements(By.CSS_SELECTOR, ".table.table-hover img")

    num = pets[0].text.split('\n')
    num = num[1].split(' ')
    num = int(num[1])

    half = num // 2
    #Получаем половину от всех питомцев

    # Находим количество питомцев с фотографией
    number_а_photos = 0
    for i in range(len(photo)):
        if photo[i].get_attribute('src') != '':
            number_а_photos += 1

    # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
    assert number_а_photos >= half
    print(f'всего питомцев: {num}')
    print(f'количество питомцев с фото: {number_а_photos}')
    print(f'Половина от числа всех питомцев: {half}')