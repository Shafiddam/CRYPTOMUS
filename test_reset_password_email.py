import pytest

from .data.data import *
from .pages.login_page import LoginPage, PasswordManager


def test_reset_password_email(driver):
    """
    Проверка сброса пароля при авторизации.
    Аккаунт enot_2022_016@mail.ru, для подтверждения просит только 2фа (без мыла)
    """
    login_page = LoginPage(driver, link_login)  
    manager = PasswordManager()  
    email_account = 'enot_2022_016@mail.ru'  
    
    try:
        login_page.open()
        login_page.click_forgot_password()
        login_page.send_keys(email_account)
        login_page.reset_continue()
        login_page.click_input_login()
        code2fa = login_page.code2fa(email_account)
        login_page.send_keys_2fa(code2fa)
        login_page.reset_confirm()

        # Генерация, сохранение и запись пароля:
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
