import time
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver

def test_all_pets():

   # Вводим email
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.ID, 'email').send_keys('neugodoff@gmail.com')
   # Вводим пароль
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.ID, 'pass').send_keys('neogoddd1')
   # Нажимаем на кнопку входа в аккаунт
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.CSS_SELECTOR, 'html > body > div > div > form > div:nth-of-type(3) > button').click()
    time.sleep(5)
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.CSS_SELECTOR, 'div#navbarNav > ul > li > a').click()
    
    time.sleep(5)

   # Проверяем, что мы оказались на главной странице пользователя
    pytest.driver.implicitly_wait(10)
    user = pytest.driver.find_element(By.TAG_NAME, 'h2').text
    assert  user == "OlesiaPsh"


    pytest.driver.implicitly_wait(10)
    pets = pytest.driver.find_elements(By.XPATH, '// *[ @ id = "all_my_pets"] / table / tbody / tr')

    pytest.driver.implicitly_wait(10)
    quant_pets = pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]')
    print(quant_pets.text.split('\n')[1].split(':')[-1])
    print(len(pets))

    assert int(quant_pets.text.split('\n')[1].split(':')[-1]) == len(pets)



