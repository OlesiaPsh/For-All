 #негативные тесты на заплнение полей Имя, Фамилия, формы регистрации некорректными значениями
import pytest

@pytest.mark.parametrize("name", ['Г', 'Иван1', 'Иван.', 'Mario', 'ааааааааааааааааааааааааааааааааа'])
def test_reg_page_name(browser, reg_page_fix, name):  #негативные тесты
    reg_page_fix.go_to_site()
    reg_page_fix.click_to_reg_button()

    reg_page_fix.send_keys_name(name)
    reg_page_fix.click_to_surname_field()

    assert reg_page_fix.get_name_message() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

@pytest.mark.parametrize("surname", ['Д', 'Иванов1', 'Иванов.', 'Mario', 'ааааааааааааааааааааааааааааааааа'])
def test_reg_page_surname(browser, reg_page_fix, surname):  #негативные тесты
    reg_page_fix.go_to_site()
    reg_page_fix.click_to_reg_button()

    reg_page_fix.send_keys_surname(surname)
    reg_page_fix.click_to_name_field()

    assert reg_page_fix.get_surname_message() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

