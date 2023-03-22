import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_there_is_a_name_age_and_gender(open_page_my_pets):
   # Получаем данные питомцев и сохраняем в переменную my_pets_stat
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))
   my_pets_stat = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   '''Из my_pets_stat, оставляем имя, возраст, и породу. Остальное меняем на пустую строку и разделяем по пробелу. 
   Находим количество элементов в получившемся списке и сравниваем их с ожидаемым результатом'''
   for i in range(len(my_pets_stat)):
      pets = my_pets_stat[i].text.replace('\n', '').replace('×', '')
      split_pets = pets.split(' ')
      result = len(split_pets)
      assert result == 3