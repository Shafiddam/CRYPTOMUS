import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .data.data import passwords
from .pages.login_page import LoginPage


def test_login_phone(driver):
    """ Вход по телефону, аккаунт +79058308055, есть 2ФА."""
    login_page = LoginPage(driver)  # Создание объекта LoginPage
    # Получите пароль из словаря
    phone = "+79058308055"
    password_for_phone = passwords.get(phone, "DefaultPasswordIfNotFound")
    try:
        login_page.open()
        login_page.send_keys(phone)
        login_page.send_keys_password(password_for_phone)
        login_page.click_login()
        code2fa = login_page.code2fa(phone)
        login_page.send_keys_2fa(code2fa)
        login_page.click_login_confirm()
        # Ожидание перехода на новую страницу (ожидаем, пока URL не будет равен указанному)
        # то есть проверяем, что мы вошли в ЛК
        WebDriverWait(driver, 10).until(EC.url_to_be('https://app.cryptomus.com/dashboard/'))
    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        driver.quit()
