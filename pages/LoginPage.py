from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, "field_password")
    LOGIN_BUTTON_ONE = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_BUTTON_TWO = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_BUTTON_QR_ONE = (By.XPATH, '//*[@data-l="t,get_qr"]')
    LOGIN_BUTTON_QR_TWO = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_DO_NOT_IN = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTRATION_BUTTON = (By.XPATH, '//*[@data-l="t,register"]')
    LOGIN_BUTTON_VK = (By.XPATH, '//*[@data-l="t,vkc"]')
    LOGIN_BUTTON_EMAIL = (By.XPATH, '//*[@data-l="t,mailru"]')
    LOGIN_BUTTON_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')


class LoginPageHelper(BasePage):
    pass