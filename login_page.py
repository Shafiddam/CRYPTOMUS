import json
import os
import secrets
import string
from time import sleep

import pyotp
from PIL import Image
from pyzbar.pyzbar import decode
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ..data.data import *
from ..data.secret_keys import secret_keys


class LoginPage:
    class Locators:
        LOGIN_URL = 'https://app.cryptomus.com/login'
        FORGOT_PASSWORD_LINK = (By.XPATH, selector_password_link)
        FORGOT_PASSWORD_INPUT_LOGIN = (By.CSS_SELECTOR, selector_input_login)
        FORGOT_PASSWORD_INPUT_CODE = (By.CSS_SELECTOR, selector_input_code)
        SELECTOR_RESET_CONTINUE = (By.XPATH, selector_reset_continue)
        SELECTOR_RESET_CONFIRM = (By.XPATH, selector_reset_confirm)
        SELECTOR_LOGIN_CONFIRM = (By.XPATH, selector_login_confirm)
        SELECTOR_ENTER_PASSWORD = (By.CSS_SELECTOR, selector_enter_password)
        SELECTOR_RESET_CREATE = (By.XPATH, selector_reset_create)
        SELECTOR_BTN_LOGIN = (By.XPATH, selector_btn_login)
        SELECTOR_BTN_SIGNUP = (By.XPATH, selector_btn_signup)
        SELECTOR_BTN_TONKEEPER = (By.CSS_SELECTOR, selector_btn_tonkeeper)
        SELECTOR_BTN_TELEGRAM = (By.CSS_SELECTOR, selector_btn_telegram)
        SELECTOR_MODAL_TONKEEPER = (By.CSS_SELECTOR, selector_modal_tonkeeper)
        SELECTOR_QR_CODE_TONKEEPER = (By.CSS_SELECTOR, selector_qr_code_tonkeeper)
        SELECTOR_MESSAGE_TEXT = (By.XPATH, selector_message_text)
        SELECTOR_QR_MESSAGE_TEXT = (By.XPATH, selector_qr_message_text)
        SELECTOR_QR_TONKEEPER_PICT = (By.CSS_SELECTOR, selector_qr_tonkeeper_pict)
        SELECTOR_BTN_QR_CODE = (By.CSS_SELECTOR, selector_btn_qr_code)
        SELECTOR_MODAL_QR_CODE = (By.CSS_SELECTOR, selector_modal_qr)
        SELECTOR_QR_CODE_PICT = (By.CSS_SELECTOR, selector_qr_code_pict)

        # ... другие локаторы

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.secret_keys = secret_keys
        self.wait = WebDriverWait(driver, 10)

    def code2fa(self, email):
        """" генерация кода 2ФА """
        totp = pyotp.TOTP(self.secret_keys[email])
        code2fa = totp.now()
        # print("\n\nОдноразовый пароль:", code2fa)
        return code2fa

    def click_forgot_password(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.FORGOT_PASSWORD_LINK)).click()

    def open(self):
        self.driver.get(self.Locators.LOGIN_URL)

    def reset_continue(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_RESET_CONTINUE)).click()

    def click_login(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_BTN_LOGIN)).click()

    def click_signup(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_BTN_SIGNUP)).click()

    def click_login_confirm(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_LOGIN_CONFIRM)).click()

    def click_input_login(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.FORGOT_PASSWORD_INPUT_LOGIN)).click()

    def send_keys(self, data):
        self._send_keys_to_input(self.Locators.FORGOT_PASSWORD_INPUT_LOGIN, data)

    def send_keys_2fa(self, code2fa):
        self._send_keys_to_input(self.Locators.FORGOT_PASSWORD_INPUT_CODE, code2fa)

    def _send_keys_to_input(self, locator, data):
        input_element = self.wait.until(EC.visibility_of_element_located(locator))
        input_element.click()
        input_element.clear()
        input_element.send_keys(data)

    def reset_confirm(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_RESET_CONFIRM)).click()

    def send_keys_new_password(self, data):
        self._send_keys_to_input(self.Locators.SELECTOR_ENTER_PASSWORD, data)

    def send_keys_password(self, data):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_ENTER_PASSWORD)).clear()
        self._send_keys_to_input(self.Locators.SELECTOR_ENTER_PASSWORD, data)

    def reset_create(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_RESET_CREATE)).click()

    def click_login_tonkeeper(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_BTN_TONKEEPER)).click()

    def click_login_telegram(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_BTN_TELEGRAM)).click()

    def click_login_qr_code(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_BTN_QR_CODE)).click()

    def modal_tonkeeper(self):
        # поиск модалки
        return self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_MODAL_TONKEEPER))

    def modal_qr_code(self):
        # поиск модалки
        return self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_MODAL_QR_CODE))

    def qr_code_tonkeeper(self):
        # поиск QR-кода
        return self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_QR_CODE_TONKEEPER))

    def qr_code_pict(self):
        # поиск QR-кода
        return self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_QR_CODE_PICT))

    def tonkeeper_message_text(self):
        # поиск названия модалки "Log in via TonKeeper"
        return self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_MESSAGE_TEXT))

    def qr_message_text(self):
        # поиск названия модалки "Log in with QR code"
        return self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_QR_MESSAGE_TEXT))

    def qr_code_tonkeeper_screenshot(self):
        """ Создание скриншота qr-кода (вход через тонкипер) и сохранение в папку screenshot """
        qr_code_modal = self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_QR_TONKEEPER_PICT))
        # путь к папке screenshot, которая находится на одном уровне с pages
        screenshot_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'screenshot')
        # Если папка не существует, создаем ее
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)
        sleep(1)  # надо явно задать паузу, иначе скриншот не распознается
        screenshot_path = os.path.join(screenshot_folder, 'qr_code_tonkeeper.png')
        qr_code_modal.screenshot(screenshot_path)
        return screenshot_path

    @staticmethod
    def qr_code_tonkeeper_screenshot_decode(screenshot_path):
        """ Загрузка изображения и распознование (вход через тонкипер) """
        try:
            image = Image.open(screenshot_path)
        except Exception as e:
            print(f"Не удалось загрузить изображение из {screenshot_path}!")
            print(f"Ошибка: {e}")
            return

        # Распознавание QR-кода
        decoded_objects = decode(image)
        # Печать распознанных данных
        for obj in decoded_objects:
            # получается ссылка вида https://app.tonkeeper.com/ton-connect?v=2&id=0e2ee91...и далее много символов
            data = obj.data.decode('utf-8')
            return data

    def qr_code_screenshot(self):
        """ Создание скриншота qr-кода и сохранение в папку screenshot (вход по QR-коду)"""
        qr_code_modal = self.wait.until(EC.visibility_of_element_located(self.Locators.SELECTOR_QR_CODE_PICT))
        # путь к папке screenshot, которая находится на одном уровне с pages
        screenshot_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'screenshot')
        # Если папка не существует, создаем ее
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)
        sleep(1)  # надо явно задать паузу, иначе скриншот не распознается
        screenshot_path = os.path.join(screenshot_folder, 'qr_code.png')
        qr_code_modal.screenshot(screenshot_path)
        return screenshot_path

    @staticmethod
    def qr_code_screenshot_decode(screenshot_path):
        """ Загрузка изображения и распознование (вход по QR-коду)"""
        try:
            image = Image.open(screenshot_path)
        except Exception as e:
            print(f"Не удалось загрузить изображение из {screenshot_path}!")
            print(f"Ошибка: {e}")
            return

        # Распознавание QR-кода
        decoded_objects = decode(image)
        # Печать распознанных данных
        for obj in decoded_objects:
            # получается ссылка вида https://app.tonkeeper.com/ton-connect?v=2&id=0e2ee91...и далее много символов
            data = obj.data.decode('utf-8')
            return data

    def compare_url_dashboard(self):
        """ сравнение url, проверяем что вошли на дашборд """
        self.wait.until(EC.url_to_be('https://app.cryptomus.com/dashboard/'))


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
