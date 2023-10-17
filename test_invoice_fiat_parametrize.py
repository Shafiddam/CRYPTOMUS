from time import sleep

import pytest
from .data.currency_list import fiat_list, cripto_list


@pytest.mark.parametrize('currency_fiat', fiat_list)
@pytest.mark.parametrize('currency_cripto', cripto_list)
def test_invoice_fiat_parametrize(request, login_and_prepare_invoice_fiat, currency_fiat, currency_cripto):
    """ Создаем инвойс по ссылке ФИАТ на 25000.
    Аккаунт enot_2022_001@mail.ru - должна быть кнопка оплаты через фиат "Pay via fiat"
    Ожидаемые результаты:
    - в инвойсе: наличие ссылки; QR-код на инвойс; ссылка открывает пейформу
    - в пейформе: сумма и фиат;
    - есть 3 кнопки: "WalletConnect" (по дефолту некликабельная) и "Pay via fiat" (именно в этом аккаунте) и "Pay"
    !!! НЕТ проверки правильности суммы в КРИПТЕ и нет проверок оплаты
    То есть тут проверки получить пейформу на 2500 фиатных монет + наличие-возможноть кликнуть на кнопку оплаты
    """

    driver, dashboard_page, first_code2fa, amount_to_send = login_and_prepare_invoice_fiat

    # Получаем имя текущего теста внутри самого теста и далее используем его для сохранения и распознования скриншото
    test_name = request.node.name

    try:
        dashboard_page.insert_currency_and_select(currency_fiat)
        dashboard_page.create_payment()

        # Проверки наличия ссылки и QR-кода:
        success, invoice_share_link = dashboard_page.find_invoice_share_link()
        assert success, "Ошибка: на странице нет ссылки на инвойс!"

        assert_qrcode_logo = dashboard_page.find_invoice_qrcode_logo()
        assert assert_qrcode_logo, "Ошибка: на странице нет QR-кода на инвойс!"

        # работа с декодированием QR-кода
        sleep(2)
        screenshot_path = dashboard_page.invoice_qr_code_screenshot_name(test_name)
        #  загружаем и распознаем картинку
        data = dashboard_page.qr_code_screenshot_decode(screenshot_path)
        # проверка, что QR-код со ссылкой "https://pay.cryptomus.com/pay/..." есть на скриншоте:
        assert invoice_share_link in data, "ОШИБКА: QR-код не содержит ссылку на инвойс!"

        # --------  открываем новую вкладку, смотрим, что это пейформа и делаем проверки:
        dashboard_page.open_new_tab_with_link(invoice_share_link)

        # --------  Проверяем кнопки:
        # 1) валет-конект НЕкликабельная 2) pay НЕкликабельная, 3) pay via fiat НЕкликабельная
        button_wallet_connect_in_pay = dashboard_page.find_wallet_connect_in_pay_not_clickable()
        assert button_wallet_connect_in_pay is not None, "Ошибка: нет кнопки wallet_connect!"
        assert not button_wallet_connect_in_pay.is_enabled(), "Ошибка: кнопка wallet_connect кликабельна!"

        button_pay_in_pay = dashboard_page.find_button_pay_in_pay_not_clickable()
        assert button_pay_in_pay is not None, "Ошибка: нет кнопки Pay!"
        assert not button_pay_in_pay.is_enabled(), "Ошибка: кнопка Pay кликабельна!"

        button_pay_via_fiat_in_pay = dashboard_page.find_pay_via_fiat_in_pay_not_clickable()
        assert button_pay_via_fiat_in_pay is not None, "Ошибка: нет кнопки Pay via fiat!"
        assert not button_pay_via_fiat_in_pay.is_enabled(), "Ошибка: кнопка Pay via fiat кликабельна!"

        # Проверка наличия суммы и названия монеты в ФИАТЕ:
        result = dashboard_page.check_fiat_in_pay_present(amount_to_send, currency_fiat)
        assert result, "Ошибка: не удалось найти требуемые amount или currency на странице!"

        # Для каждой монеты из cripto_list
        for cripto in cripto_list:
            # ---------  Выбираем монету и сеть:
            dashboard_page.click_select_currency_in_pay()
            dashboard_page.insert_currency_and_select_in_pay(cripto)

            # --------  СНОВА проверяем кнопки (выбрали монету и сеть):
            # 1) валет-конект НЕкликабельная, 2) PAY кликабельная, 3) pay via fiat кликабельная:
            button_wallet_connect_in_pay = dashboard_page.find_wallet_connect_in_pay()
            assert button_wallet_connect_in_pay is None, "Ошибка: кнопка wallet_connect кликабельна!"

            button_wallet_connect_in_pay = dashboard_page.find_wallet_connect_in_pay_not_clickable()
            assert button_wallet_connect_in_pay is not None, "Ошибка: нет кнопки wallet_connect!"

            button_pay_in_pay = dashboard_page.find_button_pay_in_pay()
            assert button_pay_in_pay, "Ошибка: кнопка PAY НЕкликабельна или ее нет на странице!"

            button_pay_via_fiat_in_pay = dashboard_page.find_pay_via_fiat_in_pay()
            assert button_pay_via_fiat_in_pay, "Ошибка: кнопка PAY НЕкликабельна или ее нет на странице!"

            # Проверка наличия суммы и названия монеты в КРИПТЕ:
            result = dashboard_page.check_any_amount_currency_in_pay(cripto)
            assert result, f"Ошибка: не удалось найти требуемые сумму и {cripto} на странице!"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        driver.quit()
