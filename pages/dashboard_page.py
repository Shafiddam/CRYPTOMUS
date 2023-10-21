import json
import os
import secrets
import string
from time import sleep
from datetime import datetime
import re

import pyautogui
import pyotp
import pytest
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image, ImageEnhance, ImageFilter
from pyzbar.pyzbar import decode
import cv2

from base_page import BasePage
from data.data import *
from data.secret_keys import secret_keys


class DashboardPage(BasePage):
    class Locators:
        # region
        DASHBOARD_URL = 'https://app.cryptomus.com/dashboard/'
        SELECTOR_BTN_COOKIE_CONFIRM = (By.CSS_SELECTOR, selector_btn_cookie_confirm)
        SELECTOR_BTN_PERSONAL_WITHDRAWAL = (By.XPATH, selector_btn_personal_withdrawal)
        SELECT_NETWORK_IN_PAY_BUTTON = (By.XPATH, select_network_in_pay_button)
        SELECT_NETWORK_NEED_IN_PAY = (By.XPATH, select_network_need_in_pay)
        BTN_PERSONAL_WITHDRAWAL_SELECT_WALLET = (By.XPATH, btn_personal_withdrawal_select_wallet)
        INPUT_SUBJECT_IN_MODAL_TICKET = (By.XPATH, input_subject_in_modal_ticket)
        INPUT_MESSAGE_IN_MODAL_TICKET = (By.XPATH, input_message_in_modal_ticket)
        INPUT_SEARCH_FIND_CURRENCY = (By.CSS_SELECTOR, input_search_find_currency)
        INPUT_FIND_CURRENCY = (By.XPATH, input_find_currency)
        INPUT_SEARCH_FIND_CURRENCY_IN_SHOW_MORE = (By.CSS_SELECTOR, input_search_find_currency_in_show_more)
        INPUT_NAME_OF_RECURRING_PAYMENT = (By.CSS_SELECTOR, input_name_of_recurring_payment)
        INPUT_SEARCH_FIND_CURRENCY_IN_PAY = (By.XPATH, input_search_find_currency_in_pay)
        SELECT_FIRST_CURRENCY = (By.ID, select_first_currency)
        SUBJECT_IN_TICKET = (By.CSS_SELECTOR, subject_in_ticket)
        MESSAGE_IN_TICKET = (By.XPATH, message_in_ticket)
        WRITE_MESSAGE_IN_TICKET = (By.XPATH, write_message_in_ticket)
        BTN_SEND_MESSAGE_IN_TICKET = (By.XPATH, btn_send_message_in_ticket)
        BTN_RESUME_MESSAGE_IN_TICKET = (By.XPATH, btn_resume_message_in_ticket)
        MODAL_NEW_TICKET = (By.CSS_SELECTOR, modal_new_ticket)
        SELECTOR_CURRENCY_TEXT__NAME = (By.XPATH, selector_currency_text__name)
        SELECTOR_CURRENCY_TEXT__NAME_USD = (By.XPATH, selector_currency_text__name_usd)
        USDT_IN_STATIC_WALLET = (By.XPATH, usdt_in_static_wallet)
        CURRENCY_TEXT_NAME_USDT = (By.XPATH, currency_text_name_usdt)
        INPUT_WALLET_ADDRESS = (By.NAME, input_wallet_address)
        INPUT_ADDRESS = (By.XPATH, input_address)
        AMOUNT_TO_AUTO_WITHDRAWAL = (By.XPATH, amount_to_auto_withdrawal)
        INSERT_BLOCKCHAIN_NAME = (By.XPATH, insert_blockchain_name)
        INSERT_HASH_TEXT = (By.XPATH, insert_hash_text)
        INSERT_COIN_NAME = (By.XPATH, insert_coin_name)
        BTN_SELECT_NETWORK = (By.XPATH, btn_select_network)
        INVOICE_SELECT_NETWORK = (By.XPATH, invoice_select_network)
        BTN_SELECT_NETWORK_POLYGON = (By.XPATH, btn_select_network_polygon)
        BTN_CREATE_PAYMENT = (By.XPATH, btn_create_payment)
        ERROR_INVALID_CODE_MESSAGE = (By.XPATH, error_invalid_code_message)
        SNACKBAR_MESSAGE_IN_PAY_LOCATOR = (By.CSS_SELECTOR, snackbar_message_in_pay_locator)
        SNACKBAR_CREATE_TICKET = (By.XPATH, snackbar_create_ticket)
        SNACKBAR_CLOSE_TICKET = (By.XPATH, snackbar_close_ticket)
        INVOICE_SHARE_LINK = (By.XPATH, selector_invoice_share_link)
        STATIC_WALLET_INVOICE_SHARE_LINK = (By.XPATH, static_wallet_invoice_share_link)
        RECURRING_PAYMENT_INVOICE_SHARE_LINK = (By.XPATH, recurring_payment_invoice_share_link)
        INVOICE_QRCODE_LOGO = (By.ID, invoice_qrcode_logo)
        PAY_STATIC_WALLET_QR_CODE = (By.CSS_SELECTOR, pay_static_wallet_qr_code)
        INVOICE_STATIC_WALLET_QRCODE_LOGO = (By.ID, invoice_static_wallet_qrcode_logo)
        INPUT_AMOUNT_TO_SEND = (By.NAME, input_amount_to_send)
        INPUT_AMOUNT_IN_SPOT = (By.XPATH, input_in_spot)
        INPUT_AMOUNT_IN_SPOT_TO_SELL = (By.XPATH, input_in_spot_to_sell)
        INPUT_IN_SPOT_LIMIT_TO_BUY = (By.XPATH, input_in_spot_limit_to_buy)
        INPUT_IN_SPOT_LIMIT_TO_SELL = (By.XPATH, input_in_spot_limit_to_sell)
        INPUT_IN_SPOT_LIMIT_MARKET_PRICE = (By.XPATH, input_in_spot_limit_market_price)
        INPUT_IN_SPOT_LIMIT_MARKET_PRICE_IN_SELL = (By.XPATH, input_in_spot_limit_market_price_in_sell)
        INPUT_AMOUNT_SET_LIMIT_PRICE = (By.CSS_SELECTOR, input_amount_set_limit_price)
        BTN_WITHDRAW = (By.XPATH, btn_withdraw)
        INPUT_CODE_2FA = (By.NAME, input_code_2fa)
        BTN_CONFIRM = (By.XPATH, btn_confirm)
        BTN_LOGOUT = (By.XPATH, btn_logout)
        CLOSE_MODAL_BIND_GOOGLE_SUCCESS = (By.XPATH, close_modal_bind_google_success)
        CLOSE_MODAL_GOT_IT = (By.XPATH, close_modal_got_it)
        MERCHANT_NAME_01 = (By.XPATH, merchant_name_01)
        BTN_MASS_PAYOUT = (By.XPATH, btn_mass_payout)
        AUTO_WITHDRAWAL_URL = 'https://app.cryptomus.com/dashboard/settings/personal/auto-withdrawal'
        BTN_PERSONAL_TRANSFER = (By.XPATH, btn_personal_transfer)
        BTN_BUSINESS_TRANSFER = (By.XPATH, btn_business_transfer)
        BTN_P2P_TRANSFER = (By.XPATH, btn_p2p_transfer)
        BTN_TRANSFER_CONFIRM = (By.XPATH, btn_transfer_confirm)
        BTN_PERSONAL_WALLET = (By.XPATH, btn_personal_wallet)
        BTN_BUSINESS_WALLET = (By.XPATH, btn_business_wallet)
        BTN_P2P_WALLET = (By.XPATH, btn_p2p_wallet)
        USDT_SENT = (By.XPATH, usdt_sent)
        BIND_GOOGLE_SUCCESS = (By.CSS_SELECTOR, bind_google_success)
        USDT_RECEIVED = (By.XPATH, usdt_received)
        BTN_DISABLE_PIN_CODE = (By.XPATH, btn_disable_pin_code)
        AMOUNT_USDT = (By.XPATH, amount_usdt)
        BTN_CREATE_MERCHANT = (By.XPATH, btn_create_merchant)
        BTN_CONFIRM_CREATE_MERCHANT = (By.XPATH, btn_confirm_create_merchant)
        BTN_SEND_ADD_COIN = (By.XPATH, btn_send_add_coin)
        BTN_CLOSE_MODAL_CREATE_MERCHANT = (By.CSS_SELECTOR, btn_close_modal_create_merchant)
        OUT_NEW_FEATURE = (By.CSS_SELECTOR, out_new_feature)
        SMALL_MAN = (By.CSS_SELECTOR, small_man)
        SELECT_SETTINGS = (By.XPATH , select_settings)
        PROMO_CODE = (By.XPATH , promo_code)
        BTN_KYC = (By.XPATH , btn_kyc)
        BTN_VERIFICATION = (By.XPATH , btn_verification)
        PROMO_CODE_ACTIVATE = (By.XPATH , promo_code_activate)
        SELECT_CURRENCY = (By.XPATH , select_currency)
        ADD_COIN = (By.CSS_SELECTOR , add_coin)
        AUTO_WITHDRAWAL = (By.XPATH , auto_withdrawal)
        ACCOUNT_DELETING = (By.XPATH , account_deleting)
        BTN_ADD_ADDRESS = (By.XPATH , btn_add_address)
        BTN_DELETE = (By.XPATH , btn_delete)
        BTN_CHANGE_EMAIL_IN_SECURITY = (By.XPATH , btn_change_email_in_security)
        BTN_CHANGE_PASSWORD_IN_SECURITY = (By.XPATH , btn_change_password_in_security)
        BTN_ADD_PHONE_NUMBER_IN_SECURITY = (By.XPATH , btn_add_phone_number_in_security)
        BTN_CONTINUE_IN_ADD_PHONE = (By.XPATH , btn_continue_in_add_phone)
        BTN_ENABLE_IN_SECURITY = (By.XPATH , btn_enable_in_security)
        BTN_PLUS_MERCHANT = (By.CSS_SELECTOR, btn_plus_merchant)
        BTN_CREATE_IN_MODAL_TICKET = (By.XPATH, btn_create_in_modal_ticket)
        BTN_CLOSE_TICKET = (By.CSS_SELECTOR, btn_close_ticket)
        BTN_YES_IN_CLOSE_TICKET = (By.XPATH, btn_yes_in_close_ticket)
        INPUT_MERCHANT_NAME = (By.CSS_SELECTOR, input_merchant_name)
        INPUT_EMAIL = (By.CSS_SELECTOR, input_email)
        BTN_RM_MERCHANT_CONFIRM_YES = (By.XPATH, btn_rm_merchant_confirm_yes)
        RM_MERCHANT_NOTISTACK_SNACKBAR = (By.XPATH, rm_merchant_notistack_snackbar)
        INVALID_CODE = (By.XPATH, invalid_code)
        SNACKBAR_TEMPORARILY_FROZEN = (By.XPATH, snackbar_temporarily_frozen)
        SNACKBAR_ADD_COIN = (By.XPATH, snackbar_add_coin)
        SNACKBAR_SEND_EMAIL = (By.XPATH, snackbar_send_email)
        SNACKBAR_PINCODE_ENABLED = (By.XPATH, snackbar_pincode_enabled)
        SNACKBAR_PINCODE_DISABLED = (By.XPATH, snackbar_pincode_disabled)
        ERROR_NOTISTACK_SNACKBAR = (By.XPATH, error_notistack_snackbar)
        MERCHANT__NAME = (By.XPATH, merchant__name)
        BTN_PAYMENT_BY_LINK = (By.XPATH, btn_payment_by_link)
        SELECT_TYPE_PAYMENT = (By.XPATH, select_type_payment)
        TYPE_PAYMENT_STATIC_WALLET = (By.XPATH, type_payment_static_wallet)
        TYPE_PAYMENT_RECURRING_PAYMENT = (By.XPATH, type_payment_recurring_payment)
        INVOICE_AMOUNT_IN_PAY = (By.XPATH, invoice_amount_in_pay)
        INVOICE_CURRENCY_IN_PAY = (By.XPATH, invoice_currency_in_pay)
        INVOICE_NETWORK_IN_PAY = (By.XPATH, invoice_network_in_pay)
        INVOICE_WALLET_ADDRESS_IN_PAY = (By.XPATH, invoice_wallet_address_in_pay)
        INVOICE_ANY_WALLET_ADDRESS_IN_PAY = (By.XPATH, invoice_any_wallet_address_in_pay)
        WALLET_CONNECT_IN_PAY = (By.XPATH, wallet_connect_in_pay)
        PAY_VIA_FIAT = (By.XPATH, pay_via_fiat)
        BTN_PAY_IN_PAY = (By.XPATH, btn_pay_in_pay)
        BTN_TICKET = (By.CSS_SELECTOR, btn_ticket)
        BTN_NEW_TICKET = (By.XPATH, btn_new_ticket)
        BTN_SELECTOR_CURRENCY = (By.CSS_SELECTOR, btn_selector_currency)
        BTN_SELECT_CURRENCY_IN_PAY = (By.CSS_SELECTOR, btn_select_currency_in_pay)
        BTN_SELECT_CURRENCY_INVOICE = (By.XPATH, btn_select_currency_invoice)
        DROPDOWN_LIST_NETWORK = (By.CSS_SELECTOR, dropdown_list_network)
        DROPDOWN_LIST_NETWORK_FIAT = (By.XPATH, dropdown_list_network_fiat)
        SELECT_CURRENCY_IN_STATIC_WALLET = (By.XPATH, select_currency_in_static_wallet)
        BTN_RECEIVE = (By.XPATH, btn_receive)
        BTN_PERSONAL_CONVERT = (By.XPATH, btn_personal_convert)
        BTN_CONVERT_SPOT = (By.XPATH, btn_convert_spot)
        BTN_DOWNLOAD_TRANSACTION = (By.CSS_SELECTOR, btn_download_transaction)
        BTN_SPOT_LIMIT = (By.XPATH, btn_spot_limit)
        BTN_BUY_IN_CONVERT_SPOT_LIMIT = (By.CSS_SELECTOR, btn_buy_in_convert_spot_limit)
        BTN_CONVERT_SPOT_MARKET_BUY = (By.CSS_SELECTOR, btn_convert_spot_market_buy)
        BTN_CONVERT_SPOT_MARKET_SELL = (By.CSS_SELECTOR, btn_convert_spot_market_sell)
        BTN_CONVERT_LIMIT = (By.XPATH, btn_convert_limit)
        CLOSE_MODAL_BALANCES_OF_PERSONAL_WALLETS = (By.CSS_SELECTOR, close_modal_balances_of_personal_wallets)
        CLOSE_MODAL = (By.CSS_SELECTOR, close_modal)
        BTN_GENERATE_NEW_ADDRESS = (By.CSS_SELECTOR, btn_generate_new_address)
        BTN_GENERATE_NEW_ADDRESS_IN_MODAL = (By.XPATH, btn_generate_new_address_in_modal)
        BTN_ORDER_HISTORY = (By.XPATH, btn_order_history)
        EXPAND_IN_ORDER_HISTORY = (By.CSS_SELECTOR, expand_in_order_history)
        BTN_SELECT_CRYPTO_WALLET = (By.XPATH, btn_select_crypto_wallet)
        WALLET_ADDRESS_IN_RECEIVE = (By.XPATH, wallet_address_in_receive)
        SELECT_CURRENCY_IN_CONVERT_MARKET = (By.XPATH, select_currency_in_convert_market)
        SELECTOR_MANUAL_CONVERT_CURRENCY = (By.XPATH, selector_manual_convert_currency)
        SELECTOR_CONVERT_LIMIT_CURRENCY_TO = (By.CSS_SELECTOR, selector_convert_limit_currency_to)
        SELECTOR_CONVERT_LIMIT_EXPIRES_IN = (By.CSS_SELECTOR, selector_convert_limit_expires_in)
        SECRET_KEY_FIELD = (By.XPATH, secret_key_field)
        INSERT_CODE2FA_GENERATE_IN_MODAL = (By.XPATH, insert_code2fa_generate_in_modal)
        INSERT_EMAIL_CODE_IN_MODAL = (By.XPATH, insert_email_code_in_modal)
        NEW_EMAIL_CODE_IN_CHANGE_EMAIL = (By.CSS_SELECTOR, new_email_code_in_change_email)
        CURRENT_EMAIL_CODE_IN_CHANGE_EMAIL = (By.CSS_SELECTOR, current_email_code_in_change_email)
        INSERT_NEW_EMAIL_IN_CHANGE_EMAIL = (By.XPATH, insert_new_email_in_change_email)
        INSERT_NEW_PHONE_NUMBER = (By.XPATH, insert_new_phone_number)
        INSERT_OLD_PASSWORD = (By.XPATH, insert_old_password)
        INSERT_NEW_PASSWORD = (By.XPATH, insert_new_password)
        INSERT_PASSWORD = (By.XPATH, insert_password)
        INSERT_PROMOCODE = (By.XPATH, insert_promocode)
        CONFIRM_NEW_PASSWORD = (By.XPATH, confirm_new_password)
        INSERT_CONFIRM_CODE = (By.XPATH, insert_confirm_code)
        SELECTOR_ONE_HOUR = (By.XPATH, selector_one_hour)
        COIN_IN_ADD_ADDRESS = (By.XPATH, coin_in_add_address)
        BTN_CONVERT_IN_CONVERT_MARKET = (By.XPATH, btn_convert_in_convert_market)
        BTN_CONVERT_IN_CONVERT_LIMIT = (By.XPATH, btn_convert_in_convert_limit)
        BTN_SHOW_MORE = (By.XPATH, btn_show_more)
        BTN_ADD_PIN_CODE_IN_SECURITY = (By.CSS_SELECTOR, btn_add_pin_code_in_security)
        INPUT1_ADD_PIN_CODE_IN_SECURITY = (By.CSS_SELECTOR, input1_add_pin_code_in_security)
        INPUT2_ADD_PIN_CODE_IN_SECURITY = (By.CSS_SELECTOR, input2_add_pin_code_in_security)
        INPUT3_ADD_PIN_CODE_IN_SECURITY = (By.CSS_SELECTOR, input3_add_pin_code_in_security)
        INPUT4_ADD_PIN_CODE_IN_SECURITY = (By.CSS_SELECTOR, input4_add_pin_code_in_security)
        # endregion

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.driver = driver
        self.secret_keys = secret_keys
        self.wait = WebDriverWait(driver, 10)

    def click_create_merchant(self):
        self.wait.until(EC.presence_of_element_located(self.Locators.BTN_CREATE_MERCHANT)).click()

    def select_merchant(self, name):
        dynamic_locator = (By.XPATH, merchant__name_template.format(name))
        self.wait.until(EC.presence_of_element_located(dynamic_locator)).click()
        # self.wait.until(EC.presence_of_element_located(self.Locators.MERCHANT__NAME)).click()

    def click_payment_by_link(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_PAYMENT_BY_LINK)).click()

    def click_receive(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_RECEIVE)).click()

    def click_btn_convert(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_PERSONAL_CONVERT)).click()

    def click_btn_spot(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CONVERT_SPOT)).click()

    def click_btn_download_transaction(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_DOWNLOAD_TRANSACTION)).click()

    def click_btn_spot_limit(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_SPOT_LIMIT)).click()

    def click_btn_buy_in_convert_spot_limit(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_BUY_IN_CONVERT_SPOT_LIMIT)).click()

    def click_btn_buy(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CONVERT_SPOT_MARKET_BUY)).click()

    def click_btn_sell(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CONVERT_SPOT_MARKET_SELL)).click()

    def click_btn_convert_limit(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CONVERT_LIMIT)).click()

    def click_add_pin_code(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_ADD_PIN_CODE_IN_SECURITY))
        # Прокручиваем страницу к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def insert_pin_code(self):
        """ вводим 1111 """
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT1_ADD_PIN_CODE_IN_SECURITY)).send_keys('1')
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT2_ADD_PIN_CODE_IN_SECURITY)).send_keys('1')
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT3_ADD_PIN_CODE_IN_SECURITY)).send_keys('1')
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT4_ADD_PIN_CODE_IN_SECURITY)).send_keys('1')

    def click_close_modal_balances_of_personal_wallets(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.CLOSE_MODAL_BALANCES_OF_PERSONAL_WALLETS)).click()

    def click_close_modal(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.CLOSE_MODAL)).click()
        sleep(2)

    def click_button_generate_new_address(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_GENERATE_NEW_ADDRESS)).click()

    def check_button_generate_new_address(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_GENERATE_NEW_ADDRESS))
            return False
        except TimeoutException:
            return None

    def click_btn_order_history(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_ORDER_HISTORY)).click()

    def click_expand_in_order_history(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.EXPAND_IN_ORDER_HISTORY)).click()

    def click_button_generate_new_address_in_modal(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_GENERATE_NEW_ADDRESS_IN_MODAL)).click()

    def click_select_crypto_wallet(self):
        self.wait.until(EC.presence_of_element_located(self.Locators.BTN_SELECT_CRYPTO_WALLET)).click()

    def click_selector_currency(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_SELECTOR_CURRENCY))
        # Прокручиваем страницу к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_show_more(self):
        element = self.wait.until(EC.presence_of_element_located(self.Locators.BTN_SHOW_MORE))
        # Прокручиваем страницу к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_selector_manual_convert_currency(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_MANUAL_CONVERT_CURRENCY))
        # Прокручиваем страницу к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_selector_convert_limit_currency_to(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_CONVERT_LIMIT_CURRENCY_TO))
        # Прокручиваем страницу к элементу
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_selector_convert_limit_expires_in(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_CONVERT_LIMIT_EXPIRES_IN))
        # Прокручиваем страницу к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def code2fa_generate_in_modal(self):
        """ Генерация кода 2ФА в модалке включения 2ФА """
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.SECRET_KEY_FIELD))
        secret_key = element.text
        totp = pyotp.TOTP(secret_key)
        code2fa = totp.now()
        return code2fa

    def insert_code2fa_generate_in_modal(self, code2fa):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INSERT_CODE2FA_GENERATE_IN_MODAL))
        element.click()
        element.send_keys(code2fa)

    def insert_code2fa_placeholder_enter_code(self, code2fa):
        locator = (By.XPATH, '//input[@placeholder="Enter code"]')
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()
        element.send_keys(code2fa)

    def insert_email_code_in_modal(self, code):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INSERT_EMAIL_CODE_IN_MODAL))
        element.click()
        element.send_keys(code)

    def insert_new_email_code_in_change_email(self, code):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.NEW_EMAIL_CODE_IN_CHANGE_EMAIL))
        element.click()
        element.clear()
        element.send_keys(code)

    def insert_current_email_code_in_change_email(self, code):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.CURRENT_EMAIL_CODE_IN_CHANGE_EMAIL))
        element.click()
        element.clear()
        element.send_keys(code)

    def insert_new_email_in_change_email(self, new_email):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INSERT_NEW_EMAIL_IN_CHANGE_EMAIL))
        element.click()
        element.send_keys(new_email)

    def insert_new_phone_number(self, new_phone_number):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INSERT_NEW_PHONE_NUMBER))
        element.click()
        element.send_keys(new_phone_number)

    def insert_old_password(self, password):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INSERT_OLD_PASSWORD))
        element.click()
        element.send_keys(password)

    def insert_new_password(self, password):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INSERT_NEW_PASSWORD))
        element.click()
        element.send_keys(password)

    def insert_password(self, password):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INSERT_PASSWORD))
        element.click()
        element.send_keys(password)

    def insert_promocode(self, code):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INSERT_PROMOCODE))
        element.click()
        element.clear()
        element.send_keys(code)

    def confirm_new_password(self, password):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.CONFIRM_NEW_PASSWORD))
        element.click()
        element.send_keys(password)

    def insert_confirm_code(self, confirm_code):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INSERT_CONFIRM_CODE))
        element.click()
        element.send_keys(confirm_code)

    def select_expires_in_1_hour(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_ONE_HOUR))
        element.click()

    def select_coin_in_add_address(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.COIN_IN_ADD_ADDRESS)).click()

    def click_btn_convert_in_convert_market(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CONVERT_IN_CONVERT_MARKET))
        # Прокручиваем страницу к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_btn_convert_in_convert_limit(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CONVERT_IN_CONVERT_LIMIT))
        # Прокручиваем страницу к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_select_currency_in_pay(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_SELECT_CURRENCY_IN_PAY)).click()

    def click_invoice_select_currency(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_SELECT_CURRENCY_INVOICE))
        # Прокручиваем страницу к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_select_currency_in_static_wallet(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECT_CURRENCY_IN_STATIC_WALLET)).click()

    def click_select_type_payment_static_wallet(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.SELECT_TYPE_PAYMENT))
        # Прокручиваем страницу к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.TYPE_PAYMENT_STATIC_WALLET))
        # Прокручиваем страницу к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_select_type_payment_recurring_payment(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.SELECT_TYPE_PAYMENT))
        # Прокручиваем страницу к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.TYPE_PAYMENT_RECURRING_PAYMENT))
        # Прокручиваем страницу к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def rm_merchant(self, merchant_name):
        """ remove merchant """
        try:
            delete_button_locator = (By.CSS_SELECTOR, ".active.merchant__item button.btn__delete")
            self.wait.until(EC.presence_of_element_located(delete_button_locator)).click()

            return True
        except TimeoutException:
            return None

    def rm_merchant_confirm_yes(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_RM_MERCHANT_CONFIRM_YES)).click()

    def find_notistack_snackbar(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.Locators.RM_MERCHANT_NOTISTACK_SNACKBAR))
        except TimeoutException:
            return False

    def find_text_in_kyc_verification(self, status):
        locator = (By.XPATH, f"//div[contains(@class, 'Verification_status') and text()='{status}']")
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            return False

    def check_btn_is_disabled(self):
        locator = (By.XPATH, "//button[contains(@class, 'btn secondary') and @disabled]")
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            return False

    def find_invalid_code(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.Locators.INVALID_CODE))
        except TimeoutException:
            return False

    def find_snackbar_temporarily_frozen(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.Locators.SNACKBAR_TEMPORARILY_FROZEN))
        except TimeoutException:
            return False

    def find_snackbar_add_coin(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.Locators.SNACKBAR_ADD_COIN))
        except TimeoutException:
            return False

    def find_currency_network_on_site(self, currency, network):
        network_lower = f'{network}'.lower()  # на сайте все в нижнем регистре
        locator = (By.XPATH, f"//span[@class='info__currency-code' and text()='{currency}']"
                             f"/following-sibling::span[@class='info__network-code' and text()='{network_lower}']")
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            return False

    def click_delete_in_add_address(self, currency, network):
        network_lower = f'{network}'.lower()  # на сайте все в нижнем регистре
        locator = (By.XPATH, f"//div[contains(@class, 'item__info') and .//span[@class='info__currency-code' and "
                             f"text()='{currency}'] and .//span[@class='info__network-code' and "
                             f"text()='{network_lower}']]//following-sibling::div[contains(@class, "
                             f"'item__actions')]//button//span[text()='Delete']")
        try:
            self.wait.until(EC.visibility_of_element_located(locator)).click()
            sleep(1)
        except TimeoutException:
            return False

    def find_address_on_site(self, address):
        locator = (By.XPATH, f"//span[@class='details__value' and text()='{address}']")
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            return False

    def find_error_description(self, error_description):
        locator = (By.XPATH, f"//span[@class='error__description' and text()='{error_description}']")
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            return False

    def find_snackbar_send_email(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.Locators.SNACKBAR_SEND_EMAIL))
        except TimeoutException:
            return False

    def find_snackbar_pincode_enabled(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.Locators.SNACKBAR_PINCODE_ENABLED))
        except TimeoutException:
            return False

    def find_snackbar_pincode_disabled(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.Locators.SNACKBAR_PINCODE_DISABLED))
        except TimeoutException:
            return False

    def find_error_notistack_snackbar(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.Locators.ERROR_NOTISTACK_SNACKBAR))
            return True
        except TimeoutException:
            return False

    def is_error_snackbar_present(self):
        error_snackbar_locator = (By.CSS_SELECTOR, '.SnackbarContent-root.SnackbarItem-variantError')
        try:
            self.wait.until(EC.presence_of_element_located(error_snackbar_locator))
            return True
        except TimeoutException:
            return False

    def check_error_snackbar_in_convert_my(self):
        # Проверка на появление ошибки "We can't create an order now. Please, try again later." (справа вверху):
        # Этого элемента не должно быть. Если есть, то тест упадет "assert not True"
        try:
            element = self.wait.until(EC.presence_of_element_located(self.Locators.ERROR_NOTISTACK_SNACKBAR))
        except TimeoutException:
            return False
        assert not element, "Внутренняя ошибка 'We can't create an order now. Please, try again later'"

        error_snackbar_locator = (By.CSS_SELECTOR, '.SnackbarContent-root.SnackbarItem-variantError')
        try:
            element2 = self.wait.until(EC.presence_of_element_located(error_snackbar_locator))
        except TimeoutException:
            return False
        assert not element2, "Ошибка: появилась плашка с ошибкой!"

    def check_error_snackbar_in_convert(self):
        snackbars = [
            (self.Locators.ERROR_NOTISTACK_SNACKBAR,
             "Внутренняя ошибка 'We can't create an order now. Please, try again later'"),
            (
            (By.CSS_SELECTOR, '.SnackbarContent-root.SnackbarItem-variantError'), "Ошибка: появилась плашка с ошибкой!")
        ]
        for snackbar, error_message in snackbars:
            try:
                self.wait.until(EC.presence_of_element_located(snackbar))
                assert False, error_message
            except TimeoutException:
                continue

    def insert_merchant_name(self, merchant_name):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_MERCHANT_NAME))
        element.click()
        element.send_keys(merchant_name)

    def insert_email_and_send(self, email):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_EMAIL))
        element.click()
        element.send_keys(email)
        btn = self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_SEND))
        btn.click()

    def click_confirm_create_merchant(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CONFIRM_CREATE_MERCHANT)).click()

    def click_pay_in_pay(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_PAY_IN_PAY)).click()

    def click_btn_ticket(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_TICKET)).click()

    def click_btn_new_ticket(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_NEW_TICKET)).click()

    def click_close_modal_create_merchant(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CLOSE_MODAL_CREATE_MERCHANT)).click()

    def click_out_new_feature(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.OUT_NEW_FEATURE)).click()

    def click_small_man(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SMALL_MAN)).click()

    def click_settings(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECT_SETTINGS)).click()

    def click_promo_code(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.PROMO_CODE)).click()

    def click_btn_kyc(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_KYC)).click()

    def click_btn_verification(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_VERIFICATION)).click()

    def click_activate(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.PROMO_CODE_ACTIVATE)).click()

    def click_currency(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECT_CURRENCY)).click()

    def click_add_coin(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.ADD_COIN)).click()

    def click_send(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_SEND_ADD_COIN)).click()

    def click_delete(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_DELETE)).click()

    def click_auto_withdrawal(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.AUTO_WITHDRAWAL)).click()

    def click_account_deleting(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.ACCOUNT_DELETING)).click()

    def click_add_address(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_ADD_ADDRESS)).click()

    def click_change_email(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CHANGE_EMAIL_IN_SECURITY)).click()

    def click_change_password(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CHANGE_PASSWORD_IN_SECURITY)).click()

    def click_add_phone_number(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_ADD_PHONE_NUMBER_IN_SECURITY)).click()

    def click_continue_in_modal(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CONTINUE_IN_ADD_PHONE)).click()

    def click_btn_enable_in_security(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_ENABLE_IN_SECURITY)).click()
            return True
        except TimeoutException:
            return False

    def find_merchant_name(self, merchant_name):
        try:
            merchant_locator = (By.XPATH, f"//*[contains(text(), '{merchant_name}')]")
            element = self.wait.until(EC.visibility_of_element_located(merchant_locator))
            return element
        except TimeoutException:
            return None

    def find_error_message_incorrect_promocode(self, message):
        try:
            locator = (By.XPATH, f"//span[@class='error__description' and text() = '{message}']")
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            return None

    def click_btn_plus_merchant(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_PLUS_MERCHANT)).click()

    def confirm_cookies(self):
        """ модалка принятия кукис """
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_BTN_COOKIE_CONFIRM)).click()
        sleep(1)

    def open(self):
        self.driver.get(self.Locators.DASHBOARD_URL)

    def _send_keys_to_input(self, locator, data):
        input_element = self.wait.until(EC.visibility_of_element_located(locator))
        input_element.click()
        input_element.clear()
        input_element.send_keys(data)

    def compare_url_dashboard(self):
        """
        Сравнение url, проверяем что вошли на дашборд
        """
        self.wait.until(EC.url_to_be('https://app.cryptomus.com/dashboard/')),

    def withdrawal_click(self):
        """ Поиск кнопки withdrawal и клик """
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_BTN_PERSONAL_WITHDRAWAL)).click()

    def select_crypto_click(self):
        """ Поиск кнопки выбора crypto_wallet и клик """
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_PERSONAL_WITHDRAWAL_SELECT_WALLET)).click()

    def select_network_in_pay(self, network):
        """ Выбираем сеть в пейформе """
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECT_NETWORK_IN_PAY_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECT_NETWORK_NEED_IN_PAY)).click()

    def insert_usdt(self):
        """ находим поиск и вставляем USDT """
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY)).send_keys('USDT')
        sleep(2)
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECT_FIRST_CURRENCY)).click()
        sleep(2)

    def filling_modal_create_ticket(self, subject, message):
        """ заполняем модалку создания тикета """
        subject_element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SUBJECT_IN_MODAL_TICKET))
        subject_element.click()
        subject_element.send_keys(subject)

        message_element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_MESSAGE_IN_MODAL_TICKET))
        message_element.click()
        message_element.send_keys(message)

        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CREATE_IN_MODAL_TICKET)).click()

    def find_subject_in_ticket(self):
        """ ищем тему """
        try:
            subject_element = self.wait.until(EC.visibility_of_element_located(self.Locators.SUBJECT_IN_TICKET))
            return subject_element.text
        except TimeoutException:
            raise Exception("Не удалось найти тему в течение ожидания!")

    def find_message_in_ticket(self):
        """ ищем message in ticket """
        try:
            subject_element = self.wait.until(EC.visibility_of_element_located(self.Locators.MESSAGE_IN_TICKET))
            return subject_element.text
        except TimeoutException:
            raise Exception("Не удалось найти message в течение ожидания!")

    def write_message_in_ticket(self, message):
        """ write_message in ticket и жмем кнопку Send """
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.Locators.WRITE_MESSAGE_IN_TICKET))
            element.click()
            element.send_keys(message)
            sleep(2)
            # Попытаться найти кнопку SEND, если не удалось, искать кнопку RESUME
            try:
                btn_send = self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_SEND_MESSAGE_IN_TICKET))
                btn_send.click()
            except TimeoutException:
                btn_resume = self.wait.until(
                    EC.visibility_of_element_located(self.Locators.BTN_RESUME_MESSAGE_IN_TICKET))
                btn_resume.click()
            return True
        except TimeoutException:
            raise Exception("Не удалось найти поле ввода или кнопку в течение ожидания!")

    def find_modal_new_ticket(self):
        """ ищем modal """
        try:
            self.wait.until(EC.visibility_of_element_located(self.Locators.MODAL_NEW_TICKET))
            return True
        except TimeoutException:
            raise Exception("Не удалось найти modal_new_ticket в течение ожидания!")

    def select_and_click_on_ticket(self, subject):
        """ ищем тему и кликаем """
        locator = (By.XPATH,
                   f"//div[@class='Tickets_table_column__bbD8V' and contains(text(), '{subject}')]")

        try:
            self.wait.until(EC.visibility_of_element_located(locator)).click()
            return True
        except TimeoutException:
            raise Exception("Не удалось найти тему в течение ожидания!")

    def find_btn_close_ticket(self):
        """ ищем btn_close_ticket """
        try:
            self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CLOSE_TICKET))
            return True
        except TimeoutException:
            raise Exception("Не удалось найти кнопку закрытия в течение ожидания!")

    def close_ticket(self):
        """ ищем btn_close_ticket и кликаем """
        try:
            self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CLOSE_TICKET)).click()
            self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_YES_IN_CLOSE_TICKET)).click()
            return True
        except TimeoutException:
            raise Exception("Не удалось найти кнопку закрытия в течение ожидания!")

    def insert_usdt_and_select(self):
        """ находим поиск и вставляем USDT """
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY)).send_keys('USDT')
        sleep(1)
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_CURRENCY_TEXT__NAME)).click()
        sleep(1)

    def insert_currency_and_select(self, currency):
        """ находим поиск и вставляем объявленный ранее currency """
        currency_text__name_locator = \
            (By.XPATH, f"//*[contains(@class,'SelectorCurrency_text__name')][text()='{currency}']")
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY))
        element.click()
        element.send_keys(currency)
        sleep(2)
        self.wait.until(EC.visibility_of_element_located(currency_text__name_locator)).click()
        sleep(2)

    def insert_currency_and_select_in_manual_convert(self, currency):
        """ находим поиск и вставляем объявленный ранее currency """
        currency_text__name_locator = \
            (By.XPATH, f"//*[contains(@class,'SelectorManualConvert_item__title__EQMJ4')][text()='{currency}']")
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY))
        element.click()
        element.send_keys(currency)
        self.wait.until(EC.visibility_of_element_located(currency_text__name_locator)).click()

    def insert_currency_and_select_in_currency(self, currency):
        """ находим поиск и вставляем объявленный ранее currency """
        currency_text__name_locator = \
            (By.XPATH, f"//div[contains(@class,'GetCurrencyModal_wrapper__Mi7yF')]/p[text()='{currency}']")
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_FIND_CURRENCY))
        element.click()
        element.send_keys(currency)
        self.wait.until(EC.visibility_of_element_located(currency_text__name_locator)).click()

    def insert_currency_and_get_balance_in_show_more(self, currency):
        """ находим поиск и вставляем объявленный ранее currency """
        currency_text_locator = (By.CSS_SELECTOR, "div.WalletBalancesModal_modal__wrapper__GNzSJ span.name__top")
        balance_locator = (By.CSS_SELECTOR, "div.WalletBalancesModal_modal__wrapper__GNzSJ span.balance__total")
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY_IN_SHOW_MORE))
        element.click()
        element.clear()
        element.send_keys(currency)
        try:
            sleep(2)
            currency_element = self.wait.until(EC.visibility_of_element_located(currency_text_locator))
            balance_element = self.wait.until(EC.visibility_of_element_located(balance_locator))
            # Получаем текст из элемента
            currency_text = currency_element.text
            balance_text = balance_element.text
            print(f"Currency: {currency_text}")
            print(f"Balance: {balance_text}")

            # Преобразуйте текст в float (если нужно)
            try:
                balance_amount = float(balance_text)
            except ValueError:
                raise Exception(f"Unable to convert '{balance_text}' to a float")
            return balance_amount
        except TimeoutException:
            return False

    def get_balance_crypta_from(self, crypta, amount_min):
        self.click_show_more()
        currency_amount = self.insert_currency_and_get_balance_in_show_more(crypta)
        if not currency_amount:
            pytest.fail(f"Не удалось извлечь количество {crypta}!")
        if currency_amount < amount_min:
            pytest.skip(f"Сумма {crypta} меньше {amount_min}. Минимум для конверта {amount_min} {crypta}!")
        self.click_close_modal_balances_of_personal_wallets()
        return currency_amount

    def get_amount_to_set_limit_price(self):
        amount_locator = (By.XPATH,
                "//h2[text()='Set limit price']/following-sibling::p[contains(@class, 'Form_hint__vTXvN')]")
        try:
            amount_element = self.wait.until(EC.visibility_of_element_located(amount_locator))
            match = re.search(r'(\d+\.\d+)', amount_element.text)
            if match:
                amount_value = float(match.group(1))
                print(amount_value)
                return amount_value
            else:
                pytest.fail(f"Не удалось найти числовое значение в строке '{amount_element.text}'")
        except TimeoutException:
            pytest.fail(f"Не удалось извлечь количество!")
        except ValueError:
            pytest.fail(f"Не удалось преобразовать значение '{amount_element.text}' в float!")

    def get_balance_crypta_to(self, crypta):
        self.click_show_more()
        sleep(2)
        balance_crypta_to = self.insert_currency_and_get_balance_in_show_more(crypta)
        # if not balance_crypta_to:
        #     pytest.fail(f"Не удалось извлечь количество {crypta}!")
        if balance_crypta_to is None:
            pytest.fail(f"Не удалось извлечь количество {crypta}!")
        self.click_close_modal_balances_of_personal_wallets()
        return balance_crypta_to

    def get_amount1_receive_in_site(self):
        amount_receive_locator = (By.XPATH, '//div[p[text()="You will receive"]]/p[2]')
        try:
            amount_receive_element = self.wait.until(EC.visibility_of_element_located(amount_receive_locator))
            match = re.search(r'(\d+\.\d+)', amount_receive_element.text)
            if match:
                amount_value = float(match.group(1))
                return amount_value
            else:
                pytest.fail(f"Не удалось найти числовое значение в строке '{amount_receive_element.text}'")
        except TimeoutException:
            pytest.fail(f"Не удалось извлечь количество!")
        except ValueError:
            pytest.fail(f"Не удалось преобразовать значение '{amount_receive_element.text}' в float!")

    def get_amount2_receive_in_site(self):
        amount_receive_locator = (By.CSS_SELECTOR, '.amount-input.convert:not(.withBtn) input[name="amount"]')
        try:
            # amount_receive_element = self.wait.until(EC.visibility_of_element_located(amount_receive_locator))
            amount_receive_element = self.wait.until(EC.presence_of_element_located(amount_receive_locator))
            amount_value = amount_receive_element.get_attribute('value')
            return float(amount_value)
        except TimeoutException:
            pytest.fail(f"Не удалось извлечь количество!")
        except ValueError:
            pytest.fail(f"Не удалось преобразовать значение '{amount_value}' в float!")

    def get_amount2_in_convert_limit(self):
        amount_receive_locator = (By.CSS_SELECTOR, 'div:nth-child(4) > div.Form_input__6\+OIz > '
                                'div.Form_amount_input__qhiaF > div > div > div > span > div > input')
        try:
            amount_receive_element = self.wait.until(EC.presence_of_element_located(amount_receive_locator))
            amount_value = amount_receive_element.get_attribute('value')
            return float(amount_value)
        except TimeoutException:
            pytest.fail(f"Не удалось извлечь количество!")
        except ValueError:
            pytest.fail(f"Не удалось преобразовать значение '{amount_value}' в float!")

    def insert_currency_and_select_in_pay(self, crypta):
        """ В ПЕЙФОРМЕ: находим инпут и вставляем объявленный ранее currency """
        currency_text__name_locator = (By.XPATH, f"//*[@class='css-102gxhc'][text()='{crypta}']")
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY_IN_PAY))
        element.click()
        element.send_keys(crypta)
        sleep(1)
        self.wait.until(EC.visibility_of_element_located(currency_text__name_locator)).click()
        sleep(1)

    def insert_currency_and_select_in_receive(self, currency):
        """ В RECEIVE находим поиск и вставляем объявленный ранее currency """
        name_locator = (By.XPATH,
            f"//li[contains(@class, 'Dropdown_item__sCHed') and .//span[@class='name__top' and text()='{currency}']]")
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY))
        element.click()
        element.send_keys(currency)
        sleep(1)
        self.wait.until(EC.visibility_of_element_located(name_locator)).click()
        sleep(1)

    def select_network_in_receive(self, network):
        """ В RECEIVE выбираем объявленный ранее currency """
        name_locator = (By.XPATH, f"//li//span[@class='css-1h92ycn' and text()='{network}']")
        self.wait.until(EC.visibility_of_element_located(name_locator)).click()
        sleep(1)

    def insert_usdt_and_select_in_static_wallet(self):
        """ находим поиск и вставляем USDT при создании статик-валлета """
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY)).send_keys('USDT')
        sleep(1)
        self.wait.until(EC.visibility_of_element_located(self.Locators.USDT_IN_STATIC_WALLET)).click()
        sleep(1)

    def insert_currency_and_select_in_static_wallet(self, currency):
        """ находим поиск и вставляем CURRENCY при создании статик-валлета """
        locator = (By.XPATH, f"//span[@class='item__name'][text()='{currency}']")
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_SELECT_CURRENCY_INVOICE)).click()
        sleep(2)
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        element.send_keys(currency)
        sleep(1)
        self.wait.until(EC.visibility_of_element_located(locator)).click()
        sleep(1)

    def insert_currency_and_select_in_add_address(self, currency):
        """ находим поиск и вставляем 'currency' в модалке добавления адреса в автовыводе """
        currency_text__name_locator = \
            (By.XPATH, f"//span[@class='text__name'][text()='{currency}']")
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY)).send_keys(currency)
        sleep(1)
        self.wait.until(EC.visibility_of_element_located(currency_text__name_locator)).click()
        sleep(1)

    def insert_currency_and_select_in_invoice(self, currency):
        """ находим поиск и вставляем объявленный ранее currency """
        currency_text__name_locator = \
            (By.XPATH, f"//span[@class='item__name'][text()='{currency}']")
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY)).send_keys(currency)
        sleep(1)
        self.wait.until(EC.visibility_of_element_located(currency_text__name_locator)).click()
        sleep(1)

    def insert_currency_and_select_in_recurring_payment(self, currency):
        """ В recurring_payment: находим поиск и вставляем объявленный ранее currency """
        currency_locator = (By.XPATH, f"//span[@class='SelectorCurrency_text__name__OG5iX'][text()='{currency}']")
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_SEARCH_FIND_CURRENCY))
        element.click()
        element.send_keys(currency)
        sleep(1)
        self.wait.until(EC.visibility_of_element_located(currency_locator)).click()
        sleep(1)

    def insert_name_of_recurring_payment(self, name):
        """ находим инпут и вставляем имя рекурентки """
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_NAME_OF_RECURRING_PAYMENT))
        element.click()
        element.send_keys(name)
        sleep(1)

    def insert_usdt_trust_wallet(self):
        """ вводим адрес usdt_trust_wallet (переводим с 1-го аккаунта на внешний кошелек) """
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_WALLET_ADDRESS)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_WALLET_ADDRESS)).send_keys(
            usdt_trust_wallet)

    def insert_usdt_address(self):
        """ вводим адрес usdt_polygon аккаунта enot_2022_015@mail.ru"""
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_WALLET_ADDRESS)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_WALLET_ADDRESS)).send_keys(
            usdt_polygon_015)

    def insert_address(self, address):
        """ вводим адрес в поле с плейсхолдером Address """
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_ADDRESS)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_ADDRESS)).send_keys(address)

    def insert_amount_to_auto_withdrawal(self, amount):
        """ вводим сумму в поле с плейсхолдером Auto-withdrawal amount """
        self.wait.until(EC.visibility_of_element_located(self.Locators.AMOUNT_TO_AUTO_WITHDRAWAL)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.AMOUNT_TO_AUTO_WITHDRAWAL)).send_keys(amount)

    def insert_blockchain_name(self, blockchain_name):
        """ вводим blockchain_name """
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INSERT_BLOCKCHAIN_NAME))
        element.click()
        element.send_keys(blockchain_name)

    def insert_hash(self, hash_text):
        """ вводим  """
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INSERT_HASH_TEXT))
        element.click()
        element.send_keys(hash_text)

    def insert_coin_name(self, coin_name):
        """ вводим  """
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INSERT_COIN_NAME))
        element.click()
        element.send_keys(coin_name)

    def scroll_500(self):
        """ Прокрутка страницы на 500 пикселей вниз"""
        self.driver.execute_script("window.scrollBy(0, 500);")

    def scroll_500_up(self):
        """ Прокрутка страницы на 500 пикселей UP """
        self.driver.execute_script("window.scrollBy(0, -500);")

    def select_network(self):
        """ выбираем сеть в ТРАНСФЕРАХ, ВЫВОДАХ (клик на кнопку меню)"""
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_SELECT_NETWORK)).click()

    def click_select_network(self):
        """ выбираем сеть в ТРАНСФЕРАХ, ВЫВОДАХ (клик на кнопку меню)"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_SELECT_NETWORK)).click()
            return True
        except TimeoutException:
            return None

    def click_selected_network(self, network):
        """ клик на уже выбранную ранее сеть """
        network_locator = (By.XPATH, f"//li//span[@class='css-1h92ycn' and text()='{network}']")
        try:
            self.wait.until(EC.visibility_of_element_located(network_locator)).click()
            return True
        except TimeoutException:
            self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_SELECT_NETWORK)).click()
            return None

    def click_selected_network_in_add_address(self, network):
        """ клик на уже выбранную ранее сеть при добавлении адреса в автовыводе """
        network_locator_1 = (By.XPATH, "//div[@class='title__text']//span[text()='Select network']")
        network_locator_2 = (By.XPATH, f"//li//span[@class='text__name' and text()='{network}']")
        try:
            self.wait.until(EC.visibility_of_element_located(network_locator_1)).click()
            sleep(2)
            self.wait.until(EC.visibility_of_element_located(network_locator_2)).click()
            return True
        except TimeoutException:
            return None

    def click_frequency_of_withdrawals(self, value):
        button_locator = (By.XPATH, f"//button[@value='{value}']")
        self.wait.until(EC.visibility_of_element_located(button_locator)).click()

    def invoice_select_network(self):
        """ выбираем сеть В ИНВОЙСАХ (клик на кнопку меню)"""
        element = self.wait.until(EC.presence_of_element_located(self.Locators.INVOICE_SELECT_NETWORK))
        # Прокручиваем страницу к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def select_network_polygon(self):
        """ выбираем сеть Polygon """
        self.wait.until(EC.presence_of_element_located(self.Locators.BTN_SELECT_NETWORK_POLYGON)).click()

    def create_payment(self):
        """ клик на кнопку create_payment """
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CREATE_PAYMENT)).click()

    def check_button_create_payment(self):
        """ Проверка кликабельности кнопки Сreate_payment """
        try:
            self.wait.until(EC.element_to_be_clickable(self.Locators.BTN_CREATE_PAYMENT))
            return True
        except TimeoutException:
            return False

    def check_error_invalid_code_message(self):
        """ Проверка вывода сообщения "Invalid code" """
        try:
            self.wait.until(EC.visibility_of_element_located(self.Locators.ERROR_INVALID_CODE_MESSAGE))
            return True
        except TimeoutException:
            return False

    def check_snackbar_message_in_pay(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.SNACKBAR_MESSAGE_IN_PAY_LOCATOR))
        assert element, "Ошибка: нет сообщения об ошибке 'You cannot accept the recurring payment you created'!"
        assert element.text == 'You cannot accept the recurring payment you created', \
            "Ошибка: выводится не 'You cannot accept the recurring payment you created'!"

    def check_snackbar_after_change_password(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.Locators.SNACKBAR_MESSAGE_IN_PAY_LOCATOR))
            assert element.text == 'Withdrawals are temporarily blocked, the reason is a password change', \
                "Ошибка: выводится не 'Withdrawals are temporarily blocked, the reason is a password change'!"
        except TimeoutException:
            assert False, "Ошибка: нет сообщения о заморозке вывода после смены пароля!"

    def check_snackbar_create_ticket(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.SNACKBAR_CREATE_TICKET))
        assert element.text == 'Ticket sent', "Ошибка: выводится не 'Ticket sent'!"

    def check_snackbar_close_ticket(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.SNACKBAR_CLOSE_TICKET))
        assert element.text == 'Ticket closed', "Ошибка: не выводится 'Ticket closed'!"

    def check_usdt_polygon_present(self):
        usdt_locator = "//div[contains(@class, 'payment-details-wallet__subheading')]//span[text()='USDT']"
        polygon_locator = \
            "//div[contains(@class, 'payment-details-wallet__subheading')]//span[text()='Network · POLYGON   ']"

        usdt_element = self.wait.until(EC.presence_of_element_located((By.XPATH, usdt_locator)))
        polygon_element = self.wait.until(EC.presence_of_element_located((By.XPATH, polygon_locator)))

        assert usdt_element is not None, "USDT not found on the page!"
        assert polygon_element is not None, "POLYGON not found on the page!"

    def check_currency_network_present(self, currency, network):
        currency_locator = f"//div[contains(@class, 'payment-details-wallet__subheading')]//span[text()='{currency}']"
        network_locator = \
            f"//div[contains(@class, 'payment-details-wallet__subheading')]//span[text()='Network · {network}   ']"

        crypto_element = self.wait.until(EC.presence_of_element_located((By.XPATH, currency_locator)))
        network_element = self.wait.until(EC.presence_of_element_located((By.XPATH, network_locator)))

        assert crypto_element is not None, f"{currency} not found on the page!"
        assert network_element is not None, f"{network} not found on the page!"

    def check_amount_currency_name(self, amount, currency, name):
        """ Проверка наличия amount , currency, name на пейформе """
        amount_locator = f"//span[contains(@class, 'payment-details__amount') and text()='{amount}']"
        currency_locator = f"//span[contains(@class, 'payment-details__amount') and text()='{currency}']"
        name_locator = f"//div[contains(@class, 'payment-details__subheading')]//span[contains(text(), '{name}')]"

        amount_element = self.wait.until(EC.presence_of_element_located((By.XPATH, amount_locator)))
        currency_element = self.wait.until(EC.presence_of_element_located((By.XPATH, currency_locator)))
        name_element = self.wait.until(EC.presence_of_element_located((By.XPATH, name_locator)))

        assert amount_element, f"{amount} not found on the page!"
        assert currency_element, f"{currency} not found on the page!"
        assert name_element, f"{name} not found on the page!"

    def find_balance_value_rub(self):
        """ поиск  """
        locator = "//span[@class='balance__value']//div[contains(text(), '₽')]"
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    def find_balance_value_currency(self, currency):
        """Поиск символа валюты на странице."""
        symbol = currency_symbols.get(currency)  # Получаем символ валюты из словаря
        if not symbol:
            raise ValueError(f"Unsupported currency code: {currency}")
        # Создаем локатор с помощью полученного символа
        locator = f"//span[@class='balance__value']//div[contains(text(), '{symbol}')]"
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    def find_TransactionHeaderItem_amountSubTitle(self, currency):
        """ поиск валюты в транзакциях """
        symbol = currency_symbols.get(currency)  # Получаем символ валюты из словаря
        if not symbol:
            raise ValueError(f"Unsupported currency code: {currency}")
        locator = f"//p[contains(@class,'TransactionHeaderItem_amountSubTitle') and contains(text(), '{symbol}')]"
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    def find_balance_total_price(self, currency):
        """ поиск валюты в транзакциях """
        symbol = currency_symbols.get(currency)  # Получаем символ валюты из словаря
        if not symbol:
            raise ValueError(f"Unsupported currency code: {currency}")
        locator = f"//span[contains(@class,'balance__total-price') and contains(text(), '{symbol}')]"
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    def find_invoice_share_link(self):
        """ поиск ссылки на инвойс и извлечение ссылки """
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.Locators.INVOICE_SHARE_LINK))
            # Прокручиваем страницу к элементу
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            invoice_share_link = element.text
            return True, invoice_share_link
        except TimeoutException:
            return False, None

    def find_wallet_address_in_receive(self):
        """ поиск Share wallet address при получении  """
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.Locators.WALLET_ADDRESS_IN_RECEIVE))
            # Прокручиваем страницу к элементу
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            wallet_address = element.text
            return True, wallet_address
        except TimeoutException:
            return False, None

    def find_pay_recepient_address(self):
        """ поиск адреса """
        locator = "//span[@class='address__text']"
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            return element.text
        except TimeoutException:
            return False

    def find_commission_in_manual_convert(self):
        """ поиск Commission в мануал-конверте и значения (0 BTC) """
        div_element = '//div[contains(@class, "WalletManualConvertCrypto_data__WkV8p")]//p[text()="Commission"]'

        try:
            commission_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, div_element)))
            value_element = commission_text.find_element(By.XPATH, "following-sibling::p")

            return commission_text, value_element.text
        except TimeoutException:
            return False

    def find_static_wallet_invoice_share_link(self):
        """ СТАТИК ВАЛЕТ: поиск ссылки на инвойс и извлечение ссылки """
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.Locators.STATIC_WALLET_INVOICE_SHARE_LINK))
            # Прокручиваем страницу к элементу
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            invoice_share_link = element.text
            return True, invoice_share_link
        except TimeoutException:
            return False, None

    def find_recurring_payment_invoice_share_link(self):
        """ RECURRING_PAYMENT: поиск ссылки на инвойс и извлечение ссылки """
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.Locators.RECURRING_PAYMENT_INVOICE_SHARE_LINK))
            # Прокручиваем страницу к элементу
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            invoice_share_link = element.text
            return True, invoice_share_link
        except TimeoutException:
            return False, None

    def find_invoice_qrcode_logo(self):
        """ поиск QR-кода на инвойс """
        try:
            self.wait.until(EC.visibility_of_element_located(self.Locators.INVOICE_QRCODE_LOGO))
            return True
        except TimeoutException:
            return False

    def find_pay_qrcode_address(self):
        """ поиск QR-кода на адрес в пейформе """
        locator = '.info__qr-wrapper'
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException:
            return False

    def find_amount_network_in_pay(self):
        """ поиск amount, currency и network в пейформе """
        try:
            self.wait.until(EC.visibility_of_element_located(self.Locators.INVOICE_AMOUNT_IN_PAY))
            self.wait.until(EC.visibility_of_element_located(self.Locators.INVOICE_CURRENCY_IN_PAY))
            self.wait.until(EC.visibility_of_element_located(self.Locators.INVOICE_NETWORK_IN_PAY))
            return True
        except TimeoutException:
            return False

    def check_fiat_amount_crypto_amount_network_in_pay_present(self):
        """ поиск fiat amount, currency amount и network в пейформе """
        usdt_locator = "//div[contains(@class, 'payment-details__amount')]//span[text()='USDT']"
        usd_locator = "//div[contains(@class, 'subheading__currency')]//span[text()='USD']"
        polygon_locator = \
        "//div[contains(@class, 'subheading__currency')]/following-sibling::span[contains(text(), 'Network · POLYGON')]"

        usdt_element = self.wait.until(EC.presence_of_element_located((By.XPATH, usdt_locator)))
        usd_element = self.wait.until(EC.presence_of_element_located((By.XPATH, usd_locator)))
        polygon_element = self.wait.until(EC.presence_of_element_located((By.XPATH, polygon_locator)))

        assert usdt_element is not None, "USDT not found on the page!"
        assert usd_element is not None, "USD not found on the page!"
        assert polygon_element is not None, "POLYGON not found on the page!"

    def check_fiat_crypto_in_pay_present(self, crypta, fiat):
        """ поиск fiat amount, currency amount и network в пейформе """
        crypta_locator = f"//div[contains(@class, 'payment-details__amount')]//span[text()='{crypta}']"
        fiat_locator = f"//div[contains(@class, 'subheading__currency')]//span[text()='{fiat}']"

        crypta_element = self.wait.until(EC.presence_of_element_located((By.XPATH, crypta_locator)))
        fiat_element = self.wait.until(EC.presence_of_element_located((By.XPATH, fiat_locator)))

        assert crypta_element is not None, f"{crypta} not found on the page!"
        assert fiat_element is not None, f"{fiat} not found on the page!"

    def check_fiat_in_pay_present(self, amount, currency):
        """ поиск amount и currency в пейформе """
        amount_locator = f"//div[@class='subheading__currency']/span[text()='{amount}']"
        currency_locator = f"//div[@class='subheading__currency']/span[text()='{currency}']"
        try:
            amount_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, amount_locator)))
            currency_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, currency_locator)))
            assert amount_element, f"{amount} not found on the page!"
            assert currency_element, f"{currency} not found on the page!"
            return True
        except TimeoutException:
            print('TimeoutException occurred')
            return False

    def check_fiat_crypto_network_in_pay_present(self, crypta, fiat, network):
        """ поиск fiat amount, currency amount и network в пейформе """
        crypta_locator = f"//div[contains(@class, 'payment-details__amount')]//span[text()='{crypta}']"
        fiat_locator = f"//div[contains(@class, 'subheading__currency')]//span[text()='{fiat}']"
        network_locator = f"//div[contains(@class, 'subheading__currency')]/following-sibling::span[contains(text()," \
                          f" 'Network · {network}')]"

        crypta_element = self.wait.until(EC.presence_of_element_located((By.XPATH, crypta_locator)))
        fiat_element = self.wait.until(EC.presence_of_element_located((By.XPATH, fiat_locator)))
        network_element = self.wait.until(EC.presence_of_element_located((By.XPATH, network_locator)))

        assert crypta_element is not None, f"{crypta} not found on the page!"
        assert fiat_element is not None, f"{fiat} not found on the page!"
        assert network_element is not None, f"{network} not found on the page!"

    def check_convert_fiat_usd_crypto_usdt_in_pay_from_binance(self, amount_to_send):
        """ проверка правильности выставления суммы в крипте. Открываем курс USDT/USD на БИНАНС в новой вкладке."""
        link = 'https://www.binance.com/en/price/tether'
        self.driver.execute_script("window.open('');")  # открываем новую вкладку
        self.driver.switch_to.window(self.driver.window_handles[-1])  # переключаемся на новую вкладку
        self.driver.get(link)

        # надо принять куки:
        btn_accept_cookies_binance = "//button[@id='onetrust-accept-btn-handler']"
        self.wait.until(EC.presence_of_element_located((By.XPATH, btn_accept_cookies_binance))).click()

        # ищем курс:
        sleep(3)
        locator = "//div[@data-bn-type='text' and contains(@class, 'css-') " \
                  "and contains(text(), 'USD') and contains(text(), '$')]"
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        text_value = element.text  # забираем число

        # сумма из текста
        match = re.search(r"\$ (\d+\.\d+) per", text_value)
        if match:
            amount = float(match.group(1))
        else:
            # обработка ошибки, если не найдено соответствие
            print("Не удалось найти число в строке.")
            return None

        # Возвращаемся на первую вкладку (на сайт):
        self.driver.switch_to.window(self.driver.window_handles[0])
        return float(amount_to_send) / amount

    def check_convert_fiat_usd_crypto_trx_in_pay_from_binance(self, amount_to_send):
        """ проверка правильности выставления суммы в крипте. Открываем курс на БИНАНС в новой вкладке."""
        link = 'https://www.binance.com/en/price/tron'
        self.driver.execute_script("window.open('');")  # открываем новую вкладку
        self.driver.switch_to.window(self.driver.window_handles[-1])  # переключаемся на новую вкладку
        self.driver.get(link)

        # надо принять куки:
        btn_accept_cookies_binance = "//button[@id='onetrust-accept-btn-handler']"
        self.wait.until(EC.presence_of_element_located((By.XPATH, btn_accept_cookies_binance))).click()

        # ищем курс:
        sleep(3)
        locator = "//div[@data-bn-type='text' and contains(@class, 'css-') " \
                  "and contains(text(), 'USD') and contains(text(), '$')]"
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        text_value = element.text  # забираем число
        print('\n',text_value)

        # сумма из текста
        match = re.search(r"\$ (\d+\.\d+) per", text_value)
        if match:
            amount = float(match.group(1))
        else:
            # обработка ошибки, если не найдено соответствие
            print("Не удалось найти число в строке.")
            return None

        # Возвращаемся на первую вкладку (на сайт):
        self.driver.switch_to.window(self.driver.window_handles[0])
        return float(amount_to_send) / amount

    def get_site_value(self):
        """ Получение суммы в крипте с сайта """
        site_value_locator = "//span[@class='payment-details__amount']"
        site_value_element = self.wait.until(EC.presence_of_element_located((By.XPATH, site_value_locator)))
        site_value = float(site_value_element.text)
        return site_value

    def get_site_value_recurring(self):
        """ Получение суммы в крипте с сайта В РЕКУРЕНТКАХ """
        site_value_locator = "//div[contains(@class, 'payment-details__subheading')]/span[1]"
        site_value_element = self.wait.until(EC.presence_of_element_located((By.XPATH, site_value_locator)))
        site_value = float(site_value_element.text)
        return site_value

    def find_amount_in_pay(self):
        """ поиск amount в пейформе """
        try:
            self.wait.until(EC.visibility_of_element_located(self.Locators.INVOICE_AMOUNT_IN_PAY))
            self.wait.until(EC.visibility_of_element_located(self.Locators.INVOICE_CURRENCY_IN_PAY))
            return True
        except TimeoutException:
            return False

    def check_amount_currency_in_pay(self, amount, currency):
        """ поиск amount и currency в пейформе """
        amount_locator = f"//span[@class='payment-details__amount'][text()='{amount}']"
        currency_locator = f"//span[@class='payment-details__amount'][text()='{currency}']"
        try:
            amount_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, amount_locator)))
            currency_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, currency_locator)))
            assert amount_element, f"{amount} not found on the page!"
            assert currency_element, f"{currency} not found on the page!"
            return True
        except TimeoutException:
            print('TimeoutException occurred')
            return False

    def check_any_amount_currency_in_pay(self, currency):
        """ поиск любой суммы(так как они меняются в цикле и currency в пейформе """
        amount_locator = "//span[@class='payment-details__amount']"
        currency_locator = f"//span[@class='payment-details__amount'][text()='{currency}']"
        try:
            amount_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, amount_locator)))
            currency_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, currency_locator)))
            assert amount_element, "Сумма не найдена на странице!"
            assert currency_element, f"{currency} not found on the page!"
            return True
        except TimeoutException:
            print('TimeoutException occurred')
            return False

    # def check_amount_fiat_in_pay(self, amount, currency):
    #     """ поиск amount и currency в пейформе """
    #     amount_locator = f"//div[@class='subheading__currency']/span[text()='{amount}']"
    #     currency_locator = f"//div[@class='subheading__currency']/span[text()='{currency}']"
    #     try:
    #         amount_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, amount_locator)))
    #         currency_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, currency_locator)))
    #         assert amount_element, f"{amount} not found on the page!"
    #         assert currency_element, f"{currency} not found on the page!"
    #         return True
    #     except TimeoutException:
    #         print('TimeoutException occurred')
    #         return False

    def check_link_and_button(self):
        # Локатор для ссылки, в которой содержится кнопка
        link_locator = "//a[contains(@href, 'https://app.cryptomus.com/dashboard/get')]"
        button_locator = ".btn.primary"

        # Проверка, что ссылка правильная
        link_element = self.wait.until(EC.presence_of_element_located((By.XPATH, link_locator)))
        assert link_element.get_attribute("href") == "https://app.cryptomus.com/dashboard/get", "Неверная ссылка!"

        # Проверка кликабельности кнопки
        try:
            button_element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_locator)))
            assert button_element, "Кнопка не кликабельна!"
        except TimeoutException:
            assert False, "Кнопка не найдена или не кликабельна!"
        return button_element

    def check_text_enough_funds_in_pay(self):
        heading_text_locator = ".status-hint__heading-text"
        status_hint_locator = "//p[@class='status-hint__description']" \
                              "[text()='Top up your Cryptomus balance to confirm a recurring payment.']"

        try:
            # self.wait.until(EC.presence_of_element_located((By.XPATH, heading_text_locator)))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, heading_text_locator)))
            heading_text_visible = True
        except TimeoutException:
            heading_text_visible = False

        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, status_hint_locator)))
            status_hint_visible = True
        except TimeoutException:
            status_hint_visible = False

        return heading_text_visible, status_hint_visible

    def find_4_network_in_pay_fiat(self):
        """ поиск 4 сетей в пейформе ФИАТ """
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.Locators.DROPDOWN_LIST_NETWORK_FIAT))
            element.click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='tron (TRC-20)']")))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='eth (ERC-20)']")))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='polygon (ERC-20)']")))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='bsc (BEP-20)']")))
            element.click()
            return True
        except TimeoutException:
            return False

    def find_4_network_in_pay(self):
        """ поиск 4 сетей в пейформе """
        try:
            self.wait.until(EC.visibility_of_element_located(self.Locators.DROPDOWN_LIST_NETWORK)).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='tron (TRC-20)']")))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='eth (ERC-20)']")))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='polygon (ERC-20)']")))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='bsc (BEP-20)']")))
            return True
        except TimeoutException:
            return False

    def find_wallet_address_in_pay(self):
        """ поиск wallet_address в пейформе """
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.Locators.INVOICE_WALLET_ADDRESS_IN_PAY))
            wallet_address_in_pay = element.text
            return wallet_address_in_pay
        except TimeoutException:
            return None

    def find_any_wallet_address_in_pay(self):
        """ поиск ЛЮБОГО wallet_address в пейформе """
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.Locators.INVOICE_ANY_WALLET_ADDRESS_IN_PAY))
            wallet_address_in_pay = element.text
            return wallet_address_in_pay
        except TimeoutException:
            return None

    def find_wallet_connect_in_pay(self):
        """ поиск КЛИКАБЕЛЬНОЙ кнопки "wallet_connect" в пейформе """
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.Locators.WALLET_CONNECT_IN_PAY))
            return element
        except TimeoutException:
            return None

    def find_wallet_connect_in_pay_not_clickable(self):
        """ поиск НЕ кликабельной кнопки "wallet_connect" в пейформе """
        try:
            element = self.wait.until(EC.presence_of_element_located(self.Locators.WALLET_CONNECT_IN_PAY))
            return element
        except TimeoutException:
            return None

    def find_pay_via_fiat_in_pay(self):
        """ поиск КЛИКАБЕЛЬНОЙ pay_via_fiat в пейформе """
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.Locators.PAY_VIA_FIAT))
            return element
        except TimeoutException:
            return None

    def find_pay_via_fiat_in_pay_not_clickable(self):
        """ поиск НЕкликабельной кнопки "pay_via_fiat" в пейформе """
        try:
            element = self.wait.until(EC.presence_of_element_located(self.Locators.PAY_VIA_FIAT))
            return element
        except TimeoutException:
            return None

    def find_button_pay_in_pay(self):
        """ поиск кнопки КЛИКАБЕЛЬНОЙ Pay в пейформе и проверка ее кликабельности """
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.Locators.BTN_PAY_IN_PAY))
            return element
        except TimeoutException:
            return None

    def find_button_pay_in_pay_not_clickable(self):
        """ поиск НЕкликабельной кнопки "button_pay_in_pay" в пейформе """
        try:
            element = self.wait.until(EC.presence_of_element_located(self.Locators.BTN_PAY_IN_PAY))
            return element
        except TimeoutException:
            return None

    def invoice_qr_code_screenshot(self):
        """ Создание скриншота qr-кода и сохранение в папку screenshot """
        qr_code_logo = self.wait.until(EC.visibility_of_element_located(self.Locators.INVOICE_QRCODE_LOGO))
        # путь к папке screenshot, которая находится на одном уровне с pages
        screenshot_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'screenshot')
        # Если папка не существует, создаем ее
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)
        sleep(1)  # надо явно задать паузу, иначе скриншот не распознается
        screenshot_path = os.path.join(screenshot_folder, 'invoice_qr_code.png')
        qr_code_logo.screenshot(screenshot_path)
        return screenshot_path

    def invoice_qr_code_screenshot_name(self, test_name):
        """ Создание скриншота qr-кода в ИНВОЙСЕ и сохранение в папку screenshot с именем теста """
        qr_code_logo = self.wait.until(
            EC.visibility_of_element_located(self.Locators.INVOICE_QRCODE_LOGO))
        # путь к папке screenshot, которая находится на одном уровне с pages
        screenshot_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'screenshot')
        # Если папка не существует, создаем ее
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)
        sleep(1)  # надо явно задать паузу, иначе скриншот не распознается
        screenshot_name = f"{test_name}_invoice_qr_code.png"
        screenshot_path = os.path.join(screenshot_folder, screenshot_name)
        qr_code_logo.screenshot(screenshot_path)
        return screenshot_path

    def pay_qr_code_screenshot_name(self, test_name):
        """ Создание скриншота qr-кода в ПЕЙФОРМЕ и сохранение в папку screenshot с именем теста """
        locator = ".info__qr-wrapper"
        qr_code_address = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        # путь к папке screenshot, которая находится на одном уровне с pages
        screenshot_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'screenshot')
        # Если папка не существует, создаем ее
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)
        sleep(1)  # надо явно задать паузу, иначе скриншот не распознается
        screenshot_name = f"{test_name}_pay_qr_code.png"
        screenshot_path = os.path.join(screenshot_folder, screenshot_name)
        qr_code_address.screenshot(screenshot_path)
        return screenshot_path

    def invoice_static_wallet_qr_code_screenshot_name(self, name_prefix):
        """ Создание скриншота qr-кода в ИНВОЙСЕ статик-валет и сохранение в папку screenshot """
        qr_code_logo = self.wait.until(
            EC.visibility_of_element_located(self.Locators.INVOICE_QRCODE_LOGO))
        # путь к папке screenshot, которая находится на одном уровне с pages
        screenshot_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'screenshot')
        # Если папка не существует, создаем ее
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)
        sleep(1)  # надо явно задать паузу, иначе скриншот не распознается
        screenshot_name = f"{name_prefix}_pay_static_wallet_qr_code.png"
        screenshot_path = os.path.join(screenshot_folder, screenshot_name)
        qr_code_logo.screenshot(screenshot_path)
        return screenshot_path

    def pay_static_wallet_qr_code_screenshot_name(self, name_prefix):
        """ Создание скриншота qr-кода в ПЕЙФОРМЕ статик-валет и сохранение в папку screenshot """
        qr_code_logo = self.wait.until(
            EC.visibility_of_element_located(self.Locators.PAY_STATIC_WALLET_QR_CODE))
        # путь к папке screenshot, которая находится на одном уровне с pages
        screenshot_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'screenshot')
        # Если папка не существует, создаем ее
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)
        sleep(1)  # надо явно задать паузу, иначе скриншот не распознается
        screenshot_name = f"{name_prefix}_pay_static_wallet_qr_code.png"
        screenshot_path = os.path.join(screenshot_folder, screenshot_name)
        qr_code_logo.screenshot(screenshot_path)
        return screenshot_path

    @staticmethod
    def qr_code_screenshot_decode(screenshot_path):
        """ Загрузка изображения и распознование (вход по QR-коду)"""
        try:
            image = Image.open(screenshot_path)
            # ниже строки по ДОРАБОТКЕ картинки, можно убрать
            # image = image.convert("L")  # преобразование в оттенки серого
            # image = ImageEnhance.Contrast(image).enhance(2)  # увеличение контраста
            # image = image.filter(ImageFilter.MedianFilter(size=3))  # уменьшение шума
            # image = image.resize((int(image.width * 1.5), int(image.height * 1.5)),
            #                      Image.ANTIALIAS)  # увеличение размера изображения
        except Exception as e:
            print(f"Не удалось загрузить изображение из {screenshot_path}!")
            print(f"Ошибка: {e}")
            return
        # Распознавание QR-кода
        decoded_objects = decode(image)
        # Печать распознанных данных
        for obj in decoded_objects:
            # получается текст: адрес кошелька, ссылка на инвойс, ссылка на тонкипер или телеграм ...
            data = obj.data.decode('utf-8')
            return data

    @staticmethod
    def qr_code_screenshot_decode2(screenshot_path):
        """ Второй метод по декоду картинки, на основе библиотеки CV2 """

        image = cv2.imread(screenshot_path)
        if image is None:
            print("Ошибка загрузки изображения.")
            return

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        detector = cv2.QRCodeDetector()
        val, pts, qr_code = detector.detectAndDecode(image)
        if val:
            return val

    def insert_amount_to_send_0_52(self):
        """ вводим "0.52" (с учетом комиссии) в поле ввода суммы """
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_AMOUNT_TO_SEND)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_AMOUNT_TO_SEND)).send_keys('0.52')

    def insert_amount_to_send(self, amount):
        """ Вводим заданную сумму в поле ввода """
        input_element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_AMOUNT_TO_SEND))
        # Прокручиваем страницу к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", input_element)
        input_element.click()
        input_element.clear()
        input_element.send_keys(amount)

    def insert_amount_in_spot_to_buy(self, amount):
        """ Вводим заданную сумму в поле ввода """
        input_element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_AMOUNT_IN_SPOT))
        input_element.send_keys(amount)

    def insert_amount_in_spot_to_sell(self, amount):
        """ Вводим заданную сумму в поле ввода in_spot_to_sell """
        input_element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_AMOUNT_IN_SPOT_TO_SELL))
        input_element.send_keys(amount)

    def insert_amount_in_spot_limit_to_buy(self, amount):
        """ Вводим заданную сумму в поле ввода """
        input_element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_IN_SPOT_LIMIT_TO_BUY))
        input_element.click()
        input_element.send_keys(amount)

    def insert_amount_in_spot_limit_to_sell(self, amount):
        """ Вводим заданную сумму в поле ввода """
        input_element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_IN_SPOT_LIMIT_TO_SELL))
        input_element.click()
        input_element.send_keys(amount)

    def get_market_price_from_binance(self, crypta_from, crypta_to):
        self.driver.execute_script("window.open('');")  # открываем новую вкладку
        self.driver.switch_to.window(self.driver.window_handles[-1])  # переключаемся на новую вкладку
        url = f"https://www.binance.com/ru/trade/{crypta_from}_{crypta_to}?theme=dark&type=spot"
        price_locator = (By.XPATH, "//div[@class='showPrice']")
        self.driver.get(url)
        try:
            btn_accept_cookies_binance = "//button[@id='onetrust-accept-btn-handler']"
            self.wait.until(EC.element_to_be_clickable((By.XPATH, btn_accept_cookies_binance))).click()
        except TimeoutException:
            pass  # Если кнопка не найдена, просто продолжаем
        try:
            market_price = self.wait.until(EC.visibility_of_element_located(price_locator))
            price = market_price.text
        except TimeoutException:
            price = None  # или какое-то другое действие в случае ошибки
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])  # возвращаемся в первоначальное окно
        return price

    def insert_market_price(self, amount):
        """ Вводим заданную сумму в поле ввода """
        input_element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_IN_SPOT_LIMIT_MARKET_PRICE))
        input_element.click()
        input_element.send_keys(amount)

    def insert_market_price_in_sell(self, amount):
        """ Вводим заданную сумму в поле ввода """
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_IN_SPOT_LIMIT_MARKET_PRICE_IN_SELL))
        element.click()
        element.send_keys(amount)

    def insert_amount_set_limit_price(self, amount):
        """ Вводим заданную сумму в поле ввода set_limit_price """
        input_element = self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_AMOUNT_SET_LIMIT_PRICE))
        input_element.click()
        input_element.clear()
        input_element.send_keys(amount)

    def insert_amount_to_send_0_5(self):
        """ вводим "0.5" в поле ввода суммы """
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_AMOUNT_TO_SEND)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_AMOUNT_TO_SEND)).send_keys('0.5')

    def scroll_1000(self):
        """ Прокрутка страницы на 1000 пикселей вниз"""
        self.driver.execute_script("window.scrollBy(0, 1000);")

    def scroll_page(self, amount):
        """ Прокрутка страницы на "amount" пикселей вниз (или вверх, если ввести -) """
        self.driver.execute_script(f"window.scrollBy(0, {amount});")

    def scroll_to_top(self):
        """ Прокрутка страницы на самый верх """
        self.driver.execute_script("window.scrollTo(0, 0);")

    def click_withdraw(self):
        """ Поиск кнопки withdrawal и клик """
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_WITHDRAW)).click()

    def click_btn_transfer_confirm(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_TRANSFER_CONFIRM)).click()

    def insert_2fa(self, code2fa):
        """ Вводим код 2ФА """
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_CODE_2FA)).click()
        self.wait.until(EC.visibility_of_element_located(self.Locators.INPUT_CODE_2FA)).send_keys(code2fa)

    def click_confirm(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_CONFIRM)).click()

    def click_logout(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_LOGOUT)).click()

    def click_close_modal_bind_google_success(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.CLOSE_MODAL_BIND_GOOGLE_SUCCESS)).click()

    def click_got_it(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.CLOSE_MODAL_GOT_IT)).click()

    def click_personal_wallet(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_PERSONAL_WALLET)).click()

    def click_business_wallet(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_BUSINESS_WALLET)).click()

    def click_p2p_wallet(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_P2P_WALLET)).click()

    def find_usdt_sent(self):
        """ Поиск usdt_sent """
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.USDT_SENT))
        return element

    def find_text_convert(self, find_text_convert):
        """ Поиск find_text_convert """
        locator = (By.XPATH,
                   f"//p[starts-with(@class, 'TransactionHeaderItem_titleText')]/span[text()='{find_text_convert}']")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element

    def find_bind_google_success(self):
        """ Поиск модалки об успехе подключения 2ФА """
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.BIND_GOOGLE_SUCCESS))
        return element

    def find_amount_convert_in_transaction(self, find_amount_convert_in_transaction):
        """ Поиск find_amount_convert_in_transaction """
        locator = (By.XPATH, f"//p[starts-with(@class, "
                        f"'TransactionHeaderItem_amountTitle')][text()='{find_amount_convert_in_transaction}']")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element

    def find_method_amount_convert_status_in_order_history(self, metod, find_amount_convert_in_transaction, status):
        """ Поиск method_amount_convert_status_in_order_history """
        locator = (By.XPATH, f"//div[contains(@class, 'WalletManualConvertHistoryTableRow_row__header__') and "
                             f".//p[contains(@class, 'WalletManualConvertHistoryTableRow_row_value__VDwmw') and text()='{metod}'] and "
                             f".//p[contains(@class, 'from_cell') and text()='{find_amount_convert_in_transaction}'] and "
                             f".//span[contains(@class, 'WalletManualConvertHistoryTableRow_done__PbiHF') and text()='{status}']]")
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except NoSuchElementException:
            pytest.fail("Ошибка: не найдено - не все условия выполнены (метод, сумма, статус)!")

    def click_expand_in_found_order(self, metod, find_amount_convert_in_transaction, status):
        locator = (By.XPATH,
                   f"//div[contains(@class, 'WalletManualConvertHistoryTableRow_row__header__') and "
                   f".//p[contains(@class, 'WalletManualConvertHistoryTableRow_row_value__VDwmw') and text()='{metod}'] and "
                   f".//p[contains(@class, 'from_cell') and text()='{find_amount_convert_in_transaction}'] and "
                   f".//span[contains(@class, 'WalletManualConvertHistoryTableRow_done__PbiHF') and text()='{status}']]"
                   f"//div[contains(@class, 'WalletManualConvertHistoryTableRow_title__icon__eYKZS')]")
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            pytest.fail("Ошибка: не найдено - не все условия выполнены (метод, сумма, статус)!")

    def click_expand_in_found_order_active(self, metod, find_amount_convert_in_transaction, status):
        locator = (By.XPATH,
                   f"//div[contains(@class, 'WalletManualConvertHistoryTableRow_row__header__') and "
                   f".//p[contains(@class, 'WalletManualConvertHistoryTableRow_row_value__VDwmw') and text()='{metod}'] and "
                   f".//p[contains(@class, 'from_cell') and text()='{find_amount_convert_in_transaction}'] and "
                   f".//span[contains(@class, 'WalletManualConvertHistoryTableRow_active') and text()='{status}']]"
                   f"//div[contains(@class, 'WalletManualConvertHistoryTableRow_title__icon__eYKZS')]")
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            pytest.fail("Ошибка: не найдено - не все условия выполнены (метод, сумма, статус)!")

    def find_settlement_date_in_order_history(self):
        """ Поиск settlement_date_in_order_history """
        current_date = datetime.now()  # получаем текущие дату-время, пример: 2023-09-26 18:52:10.427038
        formatted_date = current_date.strftime('%d.%m.%Y')  # 26.09.2023 (так в order_history выводится)
        locator = (By.XPATH, f"//p[contains(@class, 'WalletManualConvertHistoryTableRow_footer__item__value__') "
                             f" and text()='{formatted_date}']")
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            print("Не удалось найти текущую дату в Оrder_history в течение ожидания!")
            return False

    def find_1_usdt(self):
        """ Поиск 1_usdt """
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.AMOUNT_USDT))
        return element

    def find_usdt_received(self):
        """ Поиск usdt_sent """
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.USDT_RECEIVED))
        return element

    def find_btn_disable_pin_code(self):
        """ Поиск кнопки btn_disable в pin_code """
        try:
            element  = self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_DISABLE_PIN_CODE))
            # Прокручиваем страницу к элементу
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return element
        except TimeoutException:
            return False

    def transfer_to_p2p(self):
        # кликаем на "transfer_to"
        self.wait.until(EC.visibility_of_element_located((By.XPATH,
                        "//span[@class='css-1hugxjs'][text()='personal wallet']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,
                        "//span[@class='css-1hugxjs'][text()='P2P trade wallet']"))).click()
        sleep(1)

    def transfer_to_p2p_from_personal(self):
        # кликаем на "transfer_to"
        self.wait.until(EC.visibility_of_element_located((By.XPATH,
                        "//span[@class='css-1hugxjs'][text()='business wallet']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,
                        "//span[@class='css-1hugxjs'][text()='P2P trade wallet']"))).click()
        sleep(1)

    def transfer_to_business(self):
        # кликаем на "transfer_to"
        self.wait.until(EC.visibility_of_element_located((By.XPATH,
                        "//span[@class='css-1hugxjs'][text()='personal wallet']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH,
                        "//span[@class='css-1hugxjs'][text()='business wallet']"))).click()
        sleep(1)

    def get_unique_subject_for_ticket(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        unique_message = f"Message from autotest - {current_datetime}"
        return unique_message

    def get_transaction_record(self):
        """ Получение текущей даты, ее преобразование в формат как на фронте в транзакциях, поиск на странице """
        current_date = datetime.now()
        start_time = datetime.now()
        transaction_time = datetime.now()
        formatted_date = transaction_time.strftime("%d %B").lstrip("0")  # убираем ведущий ноль
        formatted_time = transaction_time.strftime("%H:%M")
        date_obj = datetime.strftime(current_date, "%d %B")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{date_obj}')]")))
        self.wait.until(EC.visibility_of_element_located
                        ((By.CSS_SELECTOR, ".TransactionItemNew_transactionItem__EqRL8"))).click()
        sleep(5)  # подождем, чтобы появилась запись на сайте
        print(f'\n{formatted_date} {formatted_time}')
        try:
            transaction_record = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, f"//p[contains(@class, 'TransactionExtraInfoItem') "
                        f"and contains(text(), '{formatted_date}') and contains(text(), '{formatted_time}')]")))
        except TimeoutException:
            print("Не удалось найти запись транзакции в течение ожидания!")
            transaction_record = None

        record_time_text = transaction_record.text if transaction_record else None
        record_time = self.extract_datetime_from_element\
            (record_time_text,'%Y %d %B %H:%M') if record_time_text else None

        return transaction_record, record_time, start_time

    def get_transaction_time(self):
        """ Получение текущей даты, ее преобразование в формат как на фронте в транзакциях, поиск на странице """
        current_date = datetime.now()
        start_time = datetime.now()
        transaction_time = datetime.now()
        print(current_date)
        formatted_date = transaction_time.strftime("%d %B").lstrip("0")  # убираем ведущий ноль
        formatted_time = transaction_time.strftime("%H:%M")
        date_obj = datetime.strftime(current_date, "%d %B")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{date_obj}')]")))

        print(f'\n{formatted_date} {formatted_time} - {date_obj}')

        try:
            transaction_record = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, f"//p[contains(@class, 'TransactionExtraInfoItem') "
                        f"and contains(text(), '{formatted_date}')]")))
        except TimeoutException:
            print("Не удалось найти запись транзакции в течение ожидания!")
            transaction_record = None

        record_time_text = transaction_record.text if transaction_record else None
        record_time = self.extract_datetime_from_element\
            (record_time_text,'%Y %d %B %H:%M') if record_time_text else None

        return transaction_record, record_time, start_time

    @staticmethod
    def extract_datetime_from_element(element_text, date_format):
        current_year = datetime.now().year
        # разбиваем текст элемента на дату и время, учитывая запятую
        date_str, time_str = element_text.split(", ")
        # формируем строку даты и времени с учетом текущего года
        record_datetime_str = f"{current_year} {date_str} {time_str}"
        return datetime.strptime(record_datetime_str, date_format)

    def open_auto_withdrawal(self):
        """ открытие страницы автовывода: """
        self.driver.get(self.Locators.AUTO_WITHDRAWAL_URL)

    def checkbox_off_on(self, code2fa):
        # находим чек-бокс включения автовывода:
        checkbox = self.wait.until(EC.presence_of_element_located
                        ((By.CSS_SELECTOR, ".PrivateSwitchBase-input.MuiSwitch-input.css-1m9pwf3")))
        # Включаем автовывод. Сначала проверка чек-бокс на checked.
        # Если нет checked, то надо кликнуть на элемент и таким образом включить его:
        if not checkbox.get_attribute('checked'):
            checkbox.click()  # Если чек-бокс не отмечен, кликаем на него
            self.insert_2fa(code2fa)  # вводим 2FA
            self.click_confirm()

    def click_trx_address(self):
        # находим строку с TRX, раскрываем ее(клик) и там должен быть адрес TK1bWEiuFoeL9ZsJnWpj6vcxBfLHnDXYGg:
        self.wait.until(EC.visibility_of_element_located((By.XPATH,
                        "//span[@class='info__currency-code'][text()='TRX']"))).click()
        # self.driver.find_element(By.XPATH, "//span[@class='info__currency-code'][text()='TRX']").click()

    def find_trx_address(self):
        """ поиск адреса TK1bWEiuFoeL9ZsJnWpj6vcxBfLHnDXYGg """
        address = self.wait.until(EC.visibility_of_element_located((By.XPATH,
                        "//span[@class='details__value'][text()='TK1bWEiuFoeL9ZsJnWpj6vcxBfLHnDXYGg']")))
        return address

    def click_to_dashboard(self):
        # кликаем на "To dashboard"
        self.wait.until(EC.visibility_of_element_located((By.XPATH,
                        "//span[@class='link__text'][text()='To dashboard']"))).click()

    def click_to_logout(self):
        # кликаем на "Logout"
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                        'div > div.dropdown-profile > div > button'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Logout']"))).click()

    def date_time(self):
        """ метод поиска даты-времени и записи о транзакции: """
        # Получаем текущую дату:
        current_date = datetime.now()
        # Сохраните текущее время после совершения транзакции
        transaction_time = datetime.now()
        formatted_date = transaction_time.strftime("%d %B")
        # Форматирование объекта datetime в желаемый формат строку вида "16 August"
        date_obj = datetime.strftime(current_date, "%d %B")
        self.wait.until(EC.visibility_of_element_located
                       ((By.XPATH, f"//*[contains(text(), '{date_obj}')]")))
        self.wait.until(EC.visibility_of_element_located
                        ((By.CSS_SELECTOR, ".TransactionItemNew_transactionItem__EqRL8"))).click()
        sleep(5)  # подождем, чтобы появилась запись на сайте
        transaction_record = self.wait.until(EC.visibility_of_element_located
                        ((By.XPATH, f"//*[contains(text(), '{formatted_date}')]")))

        return date_obj, transaction_record

    def find_element_1(self):
        # находим "TRX Received":
        element_1 = self.wait.until(EC.visibility_of_element_located((By.XPATH,
                        "//p[@class='TransactionHeaderItem_titleText__PI2MO'][text()='TRX Received']")))
        return element_1

    def find_element_2(self):
        # находим адрес получения TK1bWEiuFoeL9ZsJnWpj6vcxBfLHnDXYGg:
        element_2 = self.wait.until(EC.visibility_of_element_located((By.XPATH,
                    "//p[@class='TransactionExtraInfoItem_value__Wyq6r'][text()='TK1bWEiuFoeL9ZsJnWpj6vcxBfLHnDXYGg']")))
        return element_2

    def find_element_3(self):
        # находим сумму "1 TRX":
        element_3 = self.wait.until(EC.visibility_of_element_located((By.XPATH,
                     "//p[@class='TransactionHeaderItem_amountTitle__P8Y7D'][text()='1 TRX']")))
        return element_3

    def btn_personal_transfer(self):
        # делаем трансфер с персонал
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_PERSONAL_TRANSFER)).click()

    def btn_business_transfer(self):
        # делаем трансфер с бизнес
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_BUSINESS_TRANSFER)).click()
        sleep(1)

    def btn_p2p_transfer(self):
        # делаем трансфер с p2p
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_P2P_TRANSFER)).click()
        sleep(1)




    # region MASS PAYOUT
    # ----------------------------- MASS PAYOUT METHODS ----------------------------------------------

    def merchant_01_click(self):
        """ выбираем мерчанта 01 и кликаем """
        self.wait.until(EC.visibility_of_element_located(self.Locators.MERCHANT_NAME_01)).click()

    def btn_mass_payout_click(self):
        """ кликаем """
        # Прокрутка страницы вверх на 500 пикселей:
        self.driver.execute_script("window.scrollBy(0, -500);")
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_MASS_PAYOUT)).click()

    def delete_old_file(self):
        """ удалим старый файл и клик на аплоад нового """
        try:
            btn_delete = self.driver.find_element(By.XPATH, "//span[@class='button-text large'][text()='Delete']")
            btn_delete.click()
            sleep(3)
        except NoSuchElementException:
            pass
        self.driver.find_element(By.XPATH, "//span[@class='button-text large'][text()='Upload']").click(); sleep(3)

    @staticmethod
    def insert_file_xlsx():
        """ вставка файла из ОС """
        # вводим путь к файлу
        sleep(3) # модуль ввода очень нестабилен поэтому ждем
        pyautogui.write(r"c:\Tests\Tests\data\mass_payout.xlsx", interval=0.1)
        sleep(3)
        # нажимаем Enter, чтобы закрыть диалоговое окно
        pyautogui.press('enter')
        sleep(3)

    def click_start(self):
        """ клик на кнопку "Старт": """
        self.driver.find_element(By.XPATH, "//span[@class='button-text large'][text()='Start mass payout']").click()
        sleep(3)

    # endregion




class PasswordManager:

    def __init__(self):
        self.passwords_dict = {}

    @staticmethod
    def generate_password(length=10):
        """
        генерация нового пароля из 10 символов (обязательно одна заглавная и одна цифра)
        """
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        # Check if the password contains at least one uppercase letter and one digit
        while not any(char.isupper() for char in password) or not any(char.isdigit() for char in password):
            password = ''.join(secrets.choice(alphabet) for _ in range(length))
        print("Пароль:", password)
        return password

    @staticmethod
    def save_password_to_env(password):
        """ Сохраняем пароль в переменной окружения """
        os.environ["AUTOMATION_PASSWORD"] = password

    @staticmethod
    def get_saved_password():
        """ получить сохраненный пароль из переменной окружения """
        return os.environ.get("AUTOMATION_PASSWORD", "")

    def save_password(self, login, password):
        """ Сохраняет пароль в словаре """
        self.passwords_dict[login] = password

    def save_to_json(self, filename='passwords.json'):
        """ Сохраняет словарь паролей в JSON-файл """
        # Получаем директорию, в которой находится данный скрипт
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        # Возвращаемся на уровень вверх (из pages в Work)
        parent_dir = os.path.dirname(current_script_dir)
        # Создайте путь к папке data
        data_dir = os.path.join(parent_dir, 'data')
        # Если папка data не существует, создайте её
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        # Создайте полный путь к файлу внутри папки data
        full_path = os.path.join(data_dir, filename)
        with open(full_path, 'w') as file:
            json.dump(self.passwords_dict, file)

    def load_from_json(self, filename='passwords.json'):
        """ Загружает словарь паролей из JSON-файла """
        try:
            with open(filename, 'r') as file:
                self.passwords_dict = json.load(file)
        except FileNotFoundError:
            # Файл не найден, можно обработать ошибку или просто пропустить
            pass
