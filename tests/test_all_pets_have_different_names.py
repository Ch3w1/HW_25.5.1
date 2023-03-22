import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_all_my_pets_have_different_names(open_page_my_pets):
    # Получаем данные питомцев и сохраняем в переменную my_pets_stat
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".table.table-hover tbody tr")))
    my_pets_stat = pytest.driver.find_elements(By.CSS_SELECTOR,".table.table-hover tbody tr")

    pets_names = []
    for i in range(len(my_pets_stat)):
        pets = my_pets_stat[i].text.replace('\n', '').replace('*', '')
        split_pets = pets.split(' ')
        pets_names.append(split_pets[0])

    r = 0
    for i in range(len(pets_names)):
        if pets_names.count(pets_names[i])>1:
            r += 1
    assert r == 0
    print(r)
    print(pets_names)