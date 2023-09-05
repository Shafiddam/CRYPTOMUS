import pytest

from .pages.login_page import LoginPage


def test_login_qr_code(driver):
    """ Ожид.результат: кнопка есть, кликается, появляется модалка "Log in with QR code" """
    login_page = LoginPage(driver)  # Создание объекта LoginPage
    try:
        login_page.open()
        login_page.click_login_qr_code()
        modal = login_page.modal_qr_code()  # поиск модального окна
        # Проверка, что модалка появилась:
        assert modal.is_displayed(), "ОШИБКА: модалки нет !!!"

        qr_code = login_page.qr_code_pict()  # поиск картинки QR-кода
        assert qr_code.is_displayed(), "ОШИБКА: QR-кода в модалке нет !!!"

        qr_message_text = login_page.qr_message_text()
        assert "Log in with QR code" in qr_message_text.text, "ОШИБКА: нет названия Log in with QR code !"

        screenshot_path = login_page.qr_code_screenshot()

        #  загружаем и распознаем картинку
        data = login_page.qr_code_screenshot_decode(screenshot_path)
        # проверка, что QR-код "https://app.cryptomus.com/dashboard?token=" найден на скриншоте
        assert "https://app.cryptomus.com/dashboard?token=" in data, "ОШИБКА: QR-код не распознан!"
    except Exception as e:
        # обработка исключений
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        # закрытие браузера в любом случае
        driver.quit()
