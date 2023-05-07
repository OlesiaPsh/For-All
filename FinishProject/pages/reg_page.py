from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RegPage(BasePage):
    LOCATOR_REG_BUTTON = (By.ID, 'kc-register')
    LOCATOR_NAME_FIELD = (By.NAME, 'firstName')
    LOCATOR_SURNAME_FIELD = (By.NAME, 'lastName')
    LOCATOR_ENTER_DATA = (By.ID, 'address')
    LOCATOR_PASS = (By.ID, 'password')
    LOCATOR_PASS_CONFIRM = (By.ID, 'password-confirm')

    LOCATOR_NAME_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')  #сообщение о некорректных данных
    LOCATOR_SURNAME_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')#сообщение о некорректных данных
    LOCATOR_DATA_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/span')#сообщение о некорректных данных

    def send_keys_name(self,value):
        self.name_field = self.find_element(self.LOCATOR_NAME_FIELD)
        return self.name_field.send_keys(value)
    def send_keys_surname(self,value):
        self.surname_field = self.find_element(self.LOCATOR_SURNAME_FIELD)
        return self.surname_field.send_keys(value)


    def get_name_message(self):  #сообщение о некорректном имени
        return self.find_element(self.LOCATOR_NAME_MESSAGE).text
    def get_surname_message(self):  #сообщение о некорректной фамилии
        return self.find_element(self.LOCATOR_SURNAME_MESSAGE).text
    def click_to_surname_field(self):
        return self.find_element(self.LOCATOR_SURNAME_FIELD).click()
    def click_to_name_field(self):
        return self.find_element(self.LOCATOR_NAME_FIELD).click()

    def click_to_reg_button(self):
        return self.find_element(self.LOCATOR_REG_BUTTON).click()