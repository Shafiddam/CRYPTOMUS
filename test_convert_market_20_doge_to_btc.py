import pytest
from time import sleep


def test_convert_market_20_doge_to_btc(login_and_prepare):
    """ Аккаунт enot_2022_001@mail.ru. Конвертируем 20 DOGE в BTC.
    Нюанс: сначала кликаем на кнопку ShowMore, ищем DOGE и вытаскиваем текст(сумму) из элемента.
    И дальше если значение больше 20, то делаем try, иначе просто выводим что "минимум для конверта 20 DOGE"
    Ожидаемые результаты:  """

    driver, dashboard_page = login_and_prepare  # фикстура для авторизации, прописана в conftest.py
    crypta_from = 'DOGE'
    crypta_to = 'BTC'
    amount_fail = '0'
    amount_min = 20

    try:
        # проверка на минимум amount_min (если меньше, то тест пропускается skip)
        dashboard_page.get_balance_crypta_from(crypta_from, amount_min)

        dashboard_page.click_btn_convert()
        dashboard_page.insert_amount_to_send(amount_min)
        dashboard_page.click_selector_currency()
        dashboard_page.insert_currency_and_select(crypta_from)
        dashboard_page.click_selector_manual_convert_currency()
        dashboard_page.insert_currency_and_select_in_manual_convert(crypta_to)
        text, amount = dashboard_page.find_commission_in_manual_convert()
        assert text, "Ошибка: отсутствует слово 'Commission'!"
        assert amount == f"{amount_fail} {crypta_to}", f'Ошибка: должно выводиться "{amount_fail} {crypta_to}"'
        dashboard_page.click_btn_convert_in_convert_market()

        # Проверка на появление ошибки "We can't create an order now. Please, try again later." (справа вверху):
        # Этого элемента не должно быть. Если есть, то тест упадет "assert not True"
        element = dashboard_page.find_error_notistack_snackbar()
        assert not element, "Внутренняя ошибка 'We can't create an order now. Please, try again later'"
        assert not dashboard_page.is_error_snackbar_present(), "Ошибка: появилась плашка с ошибкой!"

        # Проверки на суммы с бинанс:

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        driver.quit()