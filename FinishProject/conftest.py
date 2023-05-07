import pytest
from selenium import webdriver
from pages.auth_page_links import AuthPageLinks
from pages.auth_form import AuthForm
from pages.reg_page import RegPage

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path=".\chromedriver")
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def authpage_fix(browser):
    auth_page = AuthPageLinks(browser)
    return auth_page

@pytest.fixture(scope="session")
def auth_form_fix(browser):
    auth_form = AuthForm(browser)
    return auth_form

@pytest.fixture(scope="session")
def reg_page_fix(browser):
    reg_page = RegPage(browser)
    return reg_page