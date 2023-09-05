import pytest

from .data.data import *
from .pages.login_page import LoginPage, PasswordManager


def test_reset_password_phone(driver):
    """
    Cброс пароля при авторизации.
    Аккаунт +79058308055, для подтверждения просит 2фа
    """
    login_page = LoginPage(driver, link_login)  # Создание объекта LoginPage
    manager = PasswordManager()  # Создаем экземпляр PasswordManager
    email_account = '+79058308055'  # Определение переменной для генеррации 2ФА
    try:
        login_page.open()
        login_page.click_forgot_password()
        login_page.send_keys(email_account)
        login_page.reset_continue()
        login_page.click_input_login()
        code2fa = login_page.code2fa(email_account)
        login_page.send_keys_2fa(code2fa)
        login_page.reset_confirm()

        # Генерировать, сохранять и записывать пароли
        new_password = manager.generate_password(10)
        manager.save_password(email_account, new_password)
        manager.save_to_json()
        # manager.save_password_to_env(new_password) # это второй вариант - сохранение в окружении
        login_page.send_keys_new_password(new_password)
        login_page.reset_create()
    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        driver.quit()
