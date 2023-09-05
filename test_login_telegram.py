import pytest
from .pages.login_page import LoginPage


def test_login_telegram(driver):
    """ Ожид.результат: кнопка есть, кликается, появляется новое окно "Telegram Authorization"
    и ссылка вида https://oauth.telegram.org/auth?bot_id..."""
    login_page = LoginPage(driver)  # Создание объекта LoginPage
    try:
        login_page.open()
        login_page.click_login_telegram()

        # Переключаемся на новое окно
        driver.switch_to.window(driver.window_handles[-1])

        # Проверяем название и URL
        assert driver.title == "Telegram Authorization"
        assert driver.current_url == \
        "https://oauth.telegram.org/auth?bot_id=5746172286&origin=https%3A%2F%2Fapp.cryptomus.com&embed=1&request_access=write&return_to=https%3A%2F%2Fapp.cryptomus.com%2Flogin"
    except Exception as e:
        # обработка исключений
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        driver.quit()
