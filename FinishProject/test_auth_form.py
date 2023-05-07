def test_email_field(browser, auth_form_fix):  #тест проверки смены способов авторизации
    auth_form_fix.go_to_site()
    auth_form_fix.click_to_email()

    assert auth_form_fix.get_name_email_field() == 'Электронная почта'

def test_phone_field(browser, auth_form_fix):#тест проверки смены способов авторизации
    auth_form_fix.go_to_site()
    auth_form_fix.click_to_phone()

    assert auth_form_fix.get_name_phone_field() == 'Мобильный телефон'

def test_login_field(browser, auth_form_fix):#тест проверки смены способов авторизации
    auth_form_fix.go_to_site()
    auth_form_fix.click_to_login()

    assert auth_form_fix.get_name_email_field() == 'Логин'

def test_account_field(browser, auth_form_fix):#тест проверки смены способов авторизации
    auth_form_fix.go_to_site()
    auth_form_fix.click_to_account()

    assert auth_form_fix.get_name_account_field() == 'Лицевой счёт'