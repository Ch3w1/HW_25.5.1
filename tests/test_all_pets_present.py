import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_all_pets_are_present(open_page_my_pets):
   # Получаем количество питомцев и сохраняем в pets (2)
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
   pets = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   # Получаем количество карточек питомцев и сохраняем в cards (2)
   element = WebDriverWait(pytest.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))
   cards = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Получаем количество питомцев из данных статистики
   num = pets[0].text.split('\n')
   num = num[1].split(' ')
   num = int(num[1])

   # Получаем количество карточек питомцев
   all_my_pets = len(cards)

   # Проверяем что количество питомцев из статистики совпадает с количеством карточек питомцев
   assert num == all_my_pets
