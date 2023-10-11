from time import sleep

import pytest

from .pages.login_page import LoginPage
from .pages.login_page import MailPage
from .pages.dashboard_page import DashboardPage
from .data.data import *


def test_settings_security_account_deleting(driver):
    """ account_deleting в settings_security, аккаунт = enot_2022_001+XX@mail.ru """
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    mail_page = MailPage(driver)
    field_in_mail = "Delete account"

    try:
        login_page.prepare_before_settings(account_001)
        dashboard_page.click_small_man()
        dashboard_page.click_settings()
        dashboard_page.click_account_deleting()
        dashboard_page.click_delete()
        dashboard_page.insert_password(password_for_new_email)
        dashboard_page.click_continue_in_modal()

        # работа с окном mail_ru - тема "Delete account"
        mail_page.switch_to_mail_tab()
        mail_page.click_btn_back_in_mail()
        sleep(15)  # подождать чтобы пришел код
        mail_page.click_field_in_mail(field_in_mail)
        # sleep(3)
        code = mail_page.extract_code_from_mail()
        mail_page.switch_to_original_tab()

        dashboard_page.insert_confirm_code(code)
        dashboard_page.click_confirm()
        dashboard_page.click_logout()

        # Проверка, что вышли - должна быть страница логина:
        sleep(15)
        current_url = driver.current_url
        assert current_url == 'https://app.cryptomus.com/login', "Ошибка: это не страница логина!"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        driver.quit()