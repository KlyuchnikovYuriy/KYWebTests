import allure
from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper


BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_ERROR = 'Введите логин'


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустой форме авторизации')
def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при отсутствии пароля')
def test_login_without_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    login_element = LoginPage.find_element(LoginPageLocators.LOGIN_FIELD)
    login_element.send_keys('test')
    LoginPage.click_login()
    error_text = LoginPage.get_error_text()
    assert error_text == 'Введите пароль', f"Ожидалась ошибка 'Введите пароль', получена: '{error_text}'"
