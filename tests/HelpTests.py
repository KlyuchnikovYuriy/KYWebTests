import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelperHelper, HelpPageLocators
from pages.AdvertisementCabinetHelp import AdvertisementCabinetHelpHelper

BASE_URL = 'https://ok.ru/help'


@allure.suite('Проверка формы помощь')
@allure.title('Проверка кнопок помощи')
def test_help_tests(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelperHelper(browser)
    HelpPage.scrollToItem(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelpHelper(browser)