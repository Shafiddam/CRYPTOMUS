import pytest

from .data.data import passwords
from .pages.login_page import LoginPage


def test_login_email(driver):
    """
    Вход по почте
    Аккаунт enot_2022_001@mail.ru, для подтверждения просит только 2фа
    """
    login_page = LoginPage(driver)  
    email = "enot_2022_001@mail.ru"
    password_for_email = passwords.get(email, "DefaultPasswordIfNotFound")
    try:
        login_page.open()
        login_page.send_keys(email)
        login_page.send_keys_password(password_for_email)
        login_page.click_login()
        code2fa = login_page.code2fa(email)
        login_page.send_keys_2fa(code2fa)
        login_page.click_login_confirm()
        login_page.compare()  # проверяем что вошли в дашборд
    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        driver.quit()
