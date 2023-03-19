from api import PetFriends
from settings import valid_email, valid_password, invalid_email, auth_key_invalid
import json
import requests
import os


pf = PetFriends()

def test_get_api_key_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result

def test_get_pet_list_valid_key(filter=''):
    _,auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_pet_list(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/cat1.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_pet_list(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_pet_list(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_pet_list(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_pet_list(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


#Дополнительные тесты

def test_create_pet_simple_valid_data(name='Артемон', animal_type='пудель', age=36):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_photo_of_pet_with_valid_data(pet_photo='images/dog.jpg'):
    """Проверяем что можно добавить фото существующему питомцу"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_pet_list(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.add_foto_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert "pet_photo" in result

#

def test_create_pet_simple_invalid_name(name=',,,,', animal_type='пудель', age='36'): #тест завершается с кодом 200
    """Проверяем что можно добавить питомца с некорректным именем"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


def test_create_pet_simple_invalid_type(name='Антошка', animal_type=789, age=5): #тест завершается с кодом 200
    """Проверяем что можно добавить питомца с некорректными типом"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


def test_create_pet_simple_invalid_age(name='Jopa', animal_type='пудель', age=''): #тест завершается с кодом 200
    """Проверяем что можно добавить питомца с некорректным возрастом"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


def test_add_photo_of_pet_with_invalid_key(pet_photo='images/dog.jpg'):# PASS
    """Проверяем что можно добавить фото существующему питомцу используя неверный ключ"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_pet_list(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.add_foto_of_pet(auth_key_invalid, my_pets['pets'][0]['id'], pet_photo)
        # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403


def test_add_photo_of_pet_with_invalid_pet_id(pet_photo='images/dog.jpg'): #тест завершается с кодом 500
    """Проверяем что можно добавить фото к несуществующему питомцу"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_pet_list(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        invaid_pet_id = '1234'
        status, result = pf.add_foto_of_pet(auth_key, invaid_pet_id, pet_photo)
        # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400

def test_get_api_key_invalid_user(email=invalid_email, password=valid_password): #PASS
    """Проверяем возможность получения ключа c неверным email"""
    status, result = pf.get_api_key(email, password)

    assert status == 403


def test_get_pet_list_invalid_key(filter=''): #PASS
    """Проверяем возможность получения спика питомцев c неверным ключом"""
    _,auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_pet_list(auth_key_invalid, filter)

    assert status == 403


def test_successful_update_self_pet_info_invalid_key(name='Мурзик', animal_type='Котэ', age=5):#PASS
    """Проверяем возможность обновления информации о питомце c неверным ключом"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_pet_list(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key_invalid, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 403

