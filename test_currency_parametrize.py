from time import sleep

import pytest

from .pages.login_page import LoginPage
from .pages.login_page import MailPage
from .pages.dashboard_page import DashboardPage
from .data.data import *


currency_list = ['JPY','TMT','AMD','PHP','UZS','USD','PLN','ISK','GBP','DKK','NOK',
    'RUB','CZK','CHF','EUR','KZT','CAD','UAH','TRY','SEK','IDR','INR','VND',
    'CNY','KRW','MYR','THB',]
@pytest.mark.parametrize('currency', currency_list)
def test_currency_parametrize(login_and_prepare_settings, currency):
    """ смена валют в ЛК и их правильное отображение, аккаунт = enot_2022_001@mail.ru """

    driver, dashboard_page, first_code2fa = login_and_prepare_settings

    try:
        dashboard_page.click_small_man()
        dashboard_page.click_currency()
        dashboard_page.insert_currency_and_select_in_currency(currency)
        sleep(2)

        # Проверки Персонал-валет:
        # Available balance
        element = dashboard_page.find_balance_value_currency(currency)
        assert element, "Ошибка: нет отображения {currency} в Available balance!"
        # Transaction
        element = dashboard_page.find_TransactionHeaderItem_amountSubTitle(currency)
        assert element, "Ошибка: нет отображения {currency} в транзакциях!"
        # balance__total-price
        element = dashboard_page.find_balance_total_price(currency)
        assert element, "Ошибка: нет отображения {currency} в балансах кошельков!"

        # Проверки Бизнес-валет:
        dashboard_page.click_business_wallet()
        # Available balance
        element = dashboard_page.find_balance_value_currency(currency)
        assert element, "Ошибка: нет отображения {currency} в Available balance!"
        # Transaction
        element = dashboard_page.find_TransactionHeaderItem_amountSubTitle(currency)
        assert element, "Ошибка: нет отображения {currency} в транзакциях!"
        # balance__total-price
        element = dashboard_page.find_balance_total_price(currency)
        assert element, "Ошибка: нет отображения {currency} в балансах кошельков!"

        # Проверки p2p-валет:
        dashboard_page.click_p2p_wallet()
        # Available balance
        element = dashboard_page.find_balance_value_currency(currency)
        assert element, "Ошибка: нет отображения {currency} в Available balance!"
        # Transaction
        element = dashboard_page.find_TransactionHeaderItem_amountSubTitle(currency)
        assert element, "Ошибка: нет отображения {currency} в транзакциях!"
        # balance__total-price
        element = dashboard_page.find_balance_total_price(currency)
        assert element, "Ошибка: нет отображения {currency} в балансах кошельков!"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        driver.quit()