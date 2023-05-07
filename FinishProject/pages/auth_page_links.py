from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AuthPageLinks(BasePage):

    LOCATOR_VK = (By.ID, 'oidc_vk') #ссылка на вк vk.com
    LOCATOR_OK = (By.ID, 'oidc_ok')  # ссылка на одноклассники  ok.ru
    LOCATOR_MM = (By.ID, 'oidc_mail') #мой мир  mail.ru
    LOCATOR_G = (By.ID, 'oidc_google')  # ссылка гугл  google.com
    LOCATOR_YA = (By.ID, 'oidc_ya')  # ссылка на yandex   yandex.ru
    LOCATOR_POLICY_CONF = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]')
    LOCATOR_USER_AGR = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[2]')
    LOCATOR_POLICY_PAGE = (By.CLASS_NAME, 'offer-title')


    def click_to_VK(self):
        return self.find_element(self.LOCATOR_VK).click()
    def click_to_OK(self):
        return self.find_element(self.LOCATOR_OK).click()
    def click_to_MM(self):
        return self.find_element(self.LOCATOR_MM).click()
    def click_to_G(self):
        return self.find_element(self.LOCATOR_G).click()
    def click_to_YA(self):
        return self.find_element(self.LOCATOR_YA).click()

    def click_to_POLICY_CONF(self):
        return self.find_element(self.LOCATOR_POLICY_CONF).click()
    def click_to_USER_AGR(self):
        return self.find_element(self.LOCATOR_USER_AGR).click()


    def get_name_from_footer(self):
        return self.find_element(self.LOCATOR_POLICY_PAGE).text

    def go_to_cart_page(self): #нажать открыть корзину
        return self.find_element(self.LOCATOR_CART).click()