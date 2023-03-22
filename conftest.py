import pytest
from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('F:/Selenium/chromedriver_win32/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()

@pytest.fixture()
def open_page_my_pets():
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
   #Поиск по ID и ввод email
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
   # Поиск по ID и ввод password
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
   pytest.driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
   # Поиск по CSS и нажатие кнопки вход
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='button']")))
   pytest.driver.find_element(By.CSS_SELECTOR,"button[type='button']").click()
   # Поиск по CSS и открытия меню
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
   pytest.driver.find_element(By.LINK_TEXT, "Мои питомцы").click()
   #Поиск по тексту и нажания на мои питомцы
