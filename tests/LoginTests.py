from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.LoginPage import LoginPageLocators

BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_ERROR = 'Введите логин'

def test_empty_login_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR

def test_login_without_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    login_element = LoginPage.find_element(LoginPageLocators.LOGIN_FIELD)
    login_element.send_keys('test')
    LoginPage.click_login()
    error_text = LoginPage.get_error_text()
    assert error_text == 'Введите пароль', f"Ожидалась ошибка 'Введите пароль', получена: '{error_text}'"





