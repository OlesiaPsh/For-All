from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://b2c.passport.rt.ru"

    def find_element(self, locator, time=10):
#поиск элемента по локатору с задержкой
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Not found {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"Not found {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_relative_link(self):
        url = self.driver.current_url
        return url

    def get_relative_link_path(self):
        url = urlparse(self.driver.current_url)
        return url.path