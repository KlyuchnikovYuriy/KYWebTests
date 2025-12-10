from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure
import random


class RegistrationPageLocators:
    PHONE_FIELD = (By.XPATH, '//div[@data-l="t,phone"]')
    CONTRY_LIST =(By.XPATH, '//div[@data-l="t,country"]')
    CONTRY_ITEM = (By.XPATH, '//div[@class="country-select_code"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@data-l="t,submit"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@data-l="t,support"]')

class RegistrationPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Прверяем корректность загрузки старницы'):
            self.find_element(RegistrationPageLocators.PHONE_FIELD)
            self.find_element(RegistrationPageLocators.CONTRY_LIST)
            self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)
            self.find_element(RegistrationPageLocators.SUPPORT_BUTTON)

    def select_random_country(self):
        random_number = random.randint(0, 212)
        self.find_element(RegistrationPageLocators.CONTRY_LIST).click()
        country_items = self.find_element(*RegistrationPageLocators.CONTRY_ITEM)
        country_code = country_items(random_number).get_attribute('text')
        country_items(random_number).click()
        return country_code

    def get_phone_field_value(self):
        return self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute('value')

