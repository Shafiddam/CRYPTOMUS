from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options  # для запуска браузера в безоконном режиме; на английском
from selenium.webdriver.chrome.service import Service
from .pages.login_page import LoginPage
from .pages.dashboard_page import DashboardPage
from .data.data import *
import os
# from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--lang=en-US")  # Установите желаемый язык, например, en-US для английского
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--log-level=DEBUG")
    service = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # driver = webdriver.Chrome(ChromeDriverManager(version="118.0.5993.70").install())
    #driver.maximize_window()  
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver, link_prod='https://app.cryptomus.com/login'):
    page = LoginPage(driver, link_prod)
    yield page


# @pytest.fixture
# def login_and_prepare():
#     chrome_options = Options()
#     chrome_options.add_argument("--lang=en-US")  # Установите желаемый язык, например, en-US для английского
#     chrome_options.add_argument("--headless")
#     #service = Service(os.environ.get("CHROMEWEBDRIVER"))
#     #driver = webdriver.Chrome(service=service, options=chrome_options)
#     driver = webdriver.Chrome(options=chrome_options)
#     #chromedriver_path = os.environ.get("CHROMEWEBDRIVER")
#     #driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
#     #driver.maximize_window()  
#     login_page = LoginPage(driver)
#     dashboard_page = DashboardPage(driver)
#     email = "enot_2022_001@mail.ru"
#     password_for_email = passwords.get(email, "DefaultPasswordIfNotFound")
#     login_page.login_with_2fa(email, password_for_email)
#     dashboard_page.confirm_cookies()
#     yield driver, dashboard_page
#     driver.quit()


# @pytest.fixture
# def login_and_prepare_settings():
#     chrome_options = Options()
#     chrome_options.add_argument("--lang=en-US")  # Установите желаемый язык, например, en-US для английского
#     chrome_options.add_argument("--headless")
#     #service = Service(os.environ.get("CHROMEWEBDRIVER"))
#     #driver = webdriver.Chrome(service=service, options=chrome_options)
#     driver = webdriver.Chrome(options=chrome_options)
#     #chromedriver_path = os.environ.get("CHROMEWEBDRIVER")
#     #driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
#     #driver.maximize_window()  
#     login_page = LoginPage(driver)
#     dashboard_page = DashboardPage(driver)
#     email = "enot_2022_001@mail.ru"
#     password_for_email = passwords.get(email, "DefaultPasswordIfNotFound")
#     first_code2fa = login_page.login_with_2fa(email, password_for_email)
#     dashboard_page.confirm_cookies()
#     yield driver, dashboard_page, first_code2fa
#     driver.quit()


# @pytest.fixture(scope="module")
# def login_and_prepare_enot_2022_015_mail_ru():
#     chrome_options = Options()
#     chrome_options.add_argument("--lang=en-US")  # Установите желаемый язык, например, en-US для английского
#     chrome_options.add_argument("--headless")
#     #service = Service(os.environ.get("CHROMEWEBDRIVER"))
#     #driver = webdriver.Chrome(service=service, options=chrome_options)
#     driver = webdriver.Chrome(options=chrome_options)
#     #chromedriver_path = os.environ.get("CHROMEWEBDRIVER")
#     #driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
#     #driver.maximize_window()  
#     login_page = LoginPage(driver)
#     dashboard_page = DashboardPage(driver)
#     email = "enot_2022_015@mail.ru"
#     password_for_email = passwords.get(email, "DefaultPasswordIfNotFound")
#     login_page.login_with_2fa(email, password_for_email)
#     dashboard_page.confirm_cookies()
#     yield driver, dashboard_page
#     driver.quit()


def pytest_exception_interact(node, call, report):
    """ хук для обработки падений в тестах: функция, которая будет вызвана pytest'ом автоматически в момент,
    когда во время выполнения теста возникает исключение. Это позволяет добавить дополнительную логику обработки
    таких ситуаций, например, для создания скриншотов (метод take_screenshot ниже)"""
    if "driver" in node.funcargs:
        web_driver = node.funcargs['driver']
        take_screenshot(web_driver, node.nodeid.replace("/", "_").replace(":", "_") + ".png")


def take_screenshot(driver, screenshot_name, screenshots_folder="screenshots"):
    if not os.path.exists(screenshots_folder):
        os.makedirs(screenshots_folder)
    screenshot_path = os.path.join(screenshots_folder, screenshot_name)
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved as {screenshot_path}")


# @pytest.fixture
# def login_and_prepare_enot_2022_018_mail_ru():
#     chrome_options = Options()
#     chrome_options.add_argument("--lang=en-US")  # Установите желаемый язык, например, en-US для английского
#     chrome_options.add_argument("--headless")
#     #service = Service(os.environ.get("CHROMEWEBDRIVER"))
#     #driver = webdriver.Chrome(service=service, options=chrome_options)
#     driver = webdriver.Chrome(options=chrome_options)
#     #chromedriver_path = os.environ.get("CHROMEWEBDRIVER")
#     #driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
#     #driver.maximize_window()  
#     login_page = LoginPage(driver)
#     dashboard_page = DashboardPage(driver)
#     email = "enot_2022_018@mail.ru"
#     password_for_email = passwords.get(email, "DefaultPasswordIfNotFound")
#     login_page.login_with_2fa(email, password_for_email)
#     dashboard_page.confirm_cookies()
#     yield driver, dashboard_page
#     driver.quit()
