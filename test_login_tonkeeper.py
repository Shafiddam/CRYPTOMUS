import pytest

from .pages.login_page import LoginPage


def test_login_tonkeeper(driver):
    """ Ожид.результат: кнопка есть, кликается, появляется модалка "Log in via TonKeeper",
    QR-код "app.tonkeeper.com/ton-connect" найден на скриншоте """
    login_page = LoginPage(driver)  # Создание объекта LoginPage
    try:
        login_page.open()
        login_page.click_login_tonkeeper()
        modal  = login_page.modal_tonkeeper()  # поиск модального окна
        # Проверка, что модалка появилась:
        assert modal.is_displayed(), "ОШИБКА: модалки нет !!!"

        qr_code = login_page.qr_code_tonkeeper()  # поиск картинки QR-кода
        # Проверка, что картинка появилась:
        assert qr_code.is_displayed(), "ОШИБКА: QR-кода в модалке нет !!!"

        tonkeeper_message_text = login_page.tonkeeper_message_text()
        # проверка, что сообщение "Log in via TonKeeper" вывелось на плашке
        assert "Log in via TonKeeper" in tonkeeper_message_text.text, "ОШИБКА: нет названия Log in via TonKeeper !"

        screenshot_path = login_page.qr_code_tonkeeper_screenshot()

        #  загружаем и распознаем картинку
        data = login_page.qr_code_tonkeeper_screenshot_decode(screenshot_path)

        # проверка, что QR-код "app.tonkeeper.com/ton-connect" найден на скриншоте
        assert "https://app.tonkeeper.com/ton-connect" in data, "ОШИБКА: QR-код TONKEEPER не найден в модальном окне!!!"
    except Exception as e:
        # обработка исключений
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        # закрытие браузера в любом случае
        driver.quit()