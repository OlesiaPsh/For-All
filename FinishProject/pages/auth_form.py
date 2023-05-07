from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AuthForm(BasePage):
    #локаторы переключателей способов авторизации
    LOCATOR_PHONE = (By.ID, 't-btn-tab-phone')
    LOCATOR_EMAIL = (By.ID, 't-btn-tab-mail')
    LOCATOR_LOGIN = (By.ID, 't-btn-tab-login')
    LOCATOR_ACCOUNT = (By.ID, 't-btn-tab-ls')
    # Локаторы надписи, сообщающей об ожидаемом типе данных
    LOCATOR_EMAIL_FIELD = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    LOCATOR_PHONE_FIELD = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    LOCATOR_ACCOUNT_FIELD = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    LOCATOR_PASS_FIELD = (By.ID, 'password') #поле ввода пароля

    LOCATOR_ENTER_BUTTON = (By.ID, 'kc-login')  #кнопка Войти
    LOCATOR_ENTER_DATA = (By.ID, 'username') #поле ввода почты или телефона


    def click_to_email(self):
        return self.find_element(self.LOCATOR_EMAIL).click()
    def click_to_phone(self):
        return self.find_element(self.LOCATOR_PHONE).click()
    def click_to_login(self):
        return self.find_element(self.LOCATOR_LOGIN).click()
    def click_to_account(self):
        return self.find_element(self.LOCATOR_ACCOUNT).click()


#надписи в поле ввода
    def get_name_email_field(self):
        return self.find_element(self.LOCATOR_EMAIL_FIELD).text
    def get_name_login_field(self):
        return self.find_element(self.LOCATOR_LOGIN_FIELD).text
    def get_name_phone_field(self):
        return self.find_element(self.LOCATOR_PHONE_FIELD).text
    def get_name_account_field(self):
        return self.find_element(self.LOCATOR_ACCOUNT_FIELD).text


    def send_keys_data(self,value):
        self.email_field = self.find_element(self.LOCATOR_ENTER_DATA)
        return self.email_field.send_keys(value)
    def send_keys_pass(self, value):
        self.pass_field = self.find_element(self.LOCATOR_PASS_FIELD)
        return self.pass_field.send_keys(value)

    def click_to_enter_button(self):
        return self.find_element(self.LOCATOR_ENTER_BUTTON).click()

