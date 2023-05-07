

def test_footer_link(browser, authpage_fix):

    authpage_fix.go_to_site()  #указываем имя фикстуры
    authpage_fix.click_to_POLICY_CONF()

    assert authpage_fix.get_relative_link_path() == '/sso-static/agreement/agreement.html'
