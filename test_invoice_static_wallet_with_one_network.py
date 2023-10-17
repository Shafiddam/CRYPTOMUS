from time import sleep

import pytest

from .data.config import CRYPTO_TO_NETWORKS_WITH_ONE_NETWORK, CRYPTO_TO_ADDRESS_WITH_ONE_NETWORK


@pytest.mark.parametrize('currency_cripto_with_one_network, network', CRYPTO_TO_NETWORKS_WITH_ONE_NETWORK.items())
def test_invoice_static_wallet_with_one_network\
                (request, login_and_prepare_invoice_static_wallet, currency_cripto_with_one_network, network):
    """ Создаем инвойс по ссылке static_wallet на все монеты (с одной сетью). Аккаунт enot_2022_001@mail.ru
    Ожидаемые результаты: наличие ссылки; QR-код на инвойс;
    ссылка открывает пейформу, в которой есть монета и сеть;
    Recepient's wallet address и верный QR-код """

    driver, dashboard_page, first_code2fa = login_and_prepare_invoice_static_wallet
    # Получаем имя текущего теста внутри самого теста и далее используем его для сохранения и распознования скриншото
    test_name = request.node.name

    try:
        dashboard_page.insert_currency_and_select_in_static_wallet(currency_cripto_with_one_network)
        dashboard_page.create_payment()

        # Проверки наличия ссылки и QR-кода:
        success, static_wallet_invoice_share_link = dashboard_page.find_static_wallet_invoice_share_link()
        assert success, "Ошибка: на странице нет ссылки на инвойс!"

        assert_qrcode_logo = dashboard_page.find_invoice_qrcode_logo()
        assert assert_qrcode_logo, "Ошибка: на странице нет QR-кода на инвойс!"
        sleep(2)

        # работа с декодированием QR-кода ----  при создании ИНВОЙСА:
        screenshot_path = dashboard_page.invoice_static_wallet_qr_code_screenshot_name(test_name)
        #  загружаем и распознаем картинку
        data = dashboard_page.qr_code_screenshot_decode(screenshot_path)
        # проверка, что QR-код со ссылкой "https://pay.cryptomus.com/wallet/..." есть на скриншоте:
        assert static_wallet_invoice_share_link in data, "ОШИБКА: QR-код не содержит ссылку на инвойс!"

        # ---------   Открываем новую вкладку и смотрим, что это пейформа:
        dashboard_page.open_new_tab_with_link(static_wallet_invoice_share_link)

        # # находим Currency и Network на пейформе:
        dashboard_page.check_currency_network_present(currency_cripto_with_one_network, network)

        # находим Recepient's wallet address на пейформе:
        wallet_address_in_pay = dashboard_page.find_any_wallet_address_in_pay()
        expected_address = CRYPTO_TO_ADDRESS_WITH_ONE_NETWORK.get(currency_cripto_with_one_network)
        assert wallet_address_in_pay == expected_address, \
            f"Ошибка: ожидался адрес {expected_address}, выводится {wallet_address_in_pay}!"

        # ----------   работа с декодированием QR-кода на ПЕЙФОРМЕ:
        sleep(3)
        screenshot_path = dashboard_page.pay_static_wallet_qr_code_screenshot_name(test_name)
        #  загружаем и распознаем картинку
        data = dashboard_page.qr_code_screenshot_decode(screenshot_path)
        # проверка, что QR-код с адресом есть на скриншоте:
        print('\n Декодированные данные в QR-коде на пейформе = ', data)
        assert wallet_address_in_pay in data, "ОШИБКА: QR-код не содержит адрес кошелька!"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        driver.quit()