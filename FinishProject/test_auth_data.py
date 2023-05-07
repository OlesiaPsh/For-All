#позитивные тесты на зааполнение формы авторизации корректными данными

def test_auth_data_email(browser, auth_form_fix):
    auth_form_fix.go_to_site()
    auth_form_fix.click_to_email()
    auth_form_fix.send_keys_data('email')
    auth_form_fix.send_keys_pass('E_W)ktsp+VyyN3A')
    auth_form_fix.click_to_enter_button()

    assert auth_form_fix.get_relative_link_path() == '/account_b2c/page'

def test_auth_data_phone(browser, auth_form_fix):
    auth_form_fix.go_to_site()
    auth_form_fix.click_to_phone()
    auth_form_fix.send_keys_data('phone')
    auth_form_fix.send_keys_pass('2GDwFMf(%zYZNZH')
    auth_form_fix.click_to_enter_button()

    assert auth_form_fix.get_relative_link_path() == '/account_b2c/page'

def test_auth_data_login(browser, auth_form_fix):
    auth_form_fix.go_to_site()
    auth_form_fix.click_to_login()
    auth_form_fix.send_keys_data('логин')
    auth_form_fix.send_keys_pass('пароль')
    auth_form_fix.click_to_enter_button()

    assert auth_form_fix.get_relative_link_path() == '/account_b2c/page'

def test_auth_data_account(browser, auth_form_fix):
    auth_form_fix.go_to_site()
    auth_form_fix.click_to_account()
    auth_form_fix.send_keys_data('лицевой счет')
    auth_form_fix.send_keys_pass('пароль')
    auth_form_fix.click_to_enter_button()

    assert auth_form_fix.get_relative_link_path() == '/account_b2c/page'