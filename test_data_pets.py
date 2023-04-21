import time
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_data_pets():

   # Вводим email
    element_email = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
    element_email.send_keys('neugodoff@gmail.com')
    #pytest.driver.find_element(By.ID, 'email').send_keys('neugodoff@gmail.com')
   # Вводим пароль
    element_pass = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'pass')))
    element_pass.send_keys('neogoddd1')
    #pytest.driver.find_element(By.ID, 'pass').send_keys('neogoddd1')
   # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'html > body > div > div > form > div:nth-of-type(3) > button'))).click()
    #pytest.driver.find_element(By.CSS_SELECTOR, 'html > body > div > div > form > div:nth-of-type(3) > button').click()
    time.sleep(2)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#navbarNav > ul > li > a'))).click()
    #pytest.driver.find_element(By.CSS_SELECTOR, 'div#navbarNav > ul > li > a').click()

    time.sleep(2)

   # Проверяем, что мы оказались на странице пользователя
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h2'))).text == "OlesiaPsh"
    #assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == "OlesiaPsh"

    data_pets = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')))
    #data_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    for i in range(len(data_pets)):
        data = data_pets[i].text.split(' ')
        assert data[0] != ''
        assert data[1] != ''
        assert data[2] != ''

    #data = data_pets.text.split('\n')


        print(data)


    print(type(data_pets))
    #for i in range(len(data_pets)):
     #   for j in range(1, 4):
      #      print(data_pets[i].get_attribute('td[j]'))


