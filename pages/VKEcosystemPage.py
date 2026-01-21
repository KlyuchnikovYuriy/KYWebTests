from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure


class VKEcosystemPageLocators:
    TITLE_LABEL = (By.XPATH, '//h1[@class="title-h2"]')


class VKEcosystemPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Прверяем корректность загрузки старницы'):
            self.attach_screenshot()
        self.find_element(VKEcosystemPageLocators.TITLE_LABEL)
