def test_VK_link(browser, authpage_fix): #тест перехода по ссылке

    authpage_fix.go_to_site()  #указываем имя фикстуры
    authpage_fix.click_to_VK()
    assert 'vk.com' in authpage_fix.get_relative_link()

def test_OK_link(browser, authpage_fix):#тест перехода по ссылке
    authpage_fix.go_to_site()
    authpage_fix.click_to_OK()
    assert 'ok.ru' in authpage_fix.get_relative_link()

def test_MM_link(browser, authpage_fix):#тест перехода по ссылке
    authpage_fix.go_to_site()
    authpage_fix.click_to_MM()
    assert 'mail.ru' in authpage_fix.get_relative_link()

def test_google_link(browser, authpage_fix):#тест перехода по ссылке
    authpage_fix.go_to_site()
    authpage_fix.click_to_G()
    assert 'google.com' in authpage_fix.get_relative_link()

def test_YA_link(browser, authpage_fix):#тест перехода по ссылке
    authpage_fix.go_to_site()
    authpage_fix.click_to_YA()
    assert 'yandex.ru' in authpage_fix.get_relative_link()
