import logging
import os
from datetime import datetime

import pytest

from pages.authorization_page import AuthorizationPage
from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.products_page import ProductsPage
from pages.shopping_cart_page import ShoppingCartPage
from utils.browser import Browser
from utils.config import AuthConfig, Url, ProductConfig

# роли для авторизации
roles = {
    "admin": {
        "login": AuthConfig.ADMIN_LOGIN,
        "password": AuthConfig.ADMIN_PASSWORD,
        "text_authorization": "\nАвторизация на сайте администратором."
    },
    "shopper": {
        "login": AuthConfig.SHOPPER_LOGIN,
        "password": AuthConfig.SHOPPER_PASSWORD,
        "text_authorization": "\nАвторизация на сайте покупателем."
    },
    "none": {
        "login": None,
        "password": None,
        "text_authorization": "\nПустые обязательные поля авторизации."
    }
}


# фикстура для авторизации
@pytest.fixture(scope="function")
def authorization(request):
    # получить роль
    role = request.param
    print(roles[role]["text_authorization"])

    # инициализация браузера
    browser = Browser(browser_type="chrome")
    browser.open(url=Url.BASE_URL)
    driver = browser.driver

    # заполнение формы авторизации
    authorization_page = AuthorizationPage(driver)
    authorization_page.enter_login(roles[role]["login"])
    authorization_page.enter_password(roles[role]["password"])
    authorization_page.click_the_login_button()

    # передача драйвера
    yield driver

    # закрытие браузера
    browser.quit()


# добавление продукта в количестве 2 шт.
@pytest.fixture(scope="function")
def add_two_products(authorization):
    driver = authorization

    ProductsPage(driver).set_product_quantity(
        product_name=ProductConfig.PRODUCT_NAME,
        target_quantity=ProductConfig.QUANTITY_2
    )


# перейти в корзину
@pytest.fixture(scope="function")
def go_to_cart(authorization):
    driver = authorization

    FixedPanelIcons(driver).click_shopping_cart()


# перейти на страницу "Оформление заказа: Данные пользователя"
@pytest.fixture(scope="function")
def go_to_checkout_user_data(authorization):
    driver = authorization

    ShoppingCartPage(driver).click_button_place_order()


# настройка записи логов
def pytest_configure():
    # отключает логи WebDriver Manager
    os.environ['WDM_LOG'] = str(0)
    # создать папку
    os.makedirs("logs", exist_ok=True)
    # имя для файла
    file_name = f"logs/log_{datetime.now().strftime('%Y-%m-%d_%H.%M.%S')}.log"

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] \t%(message)s',
        datefmt='%H:%M:%S',
        handlers=[logging.FileHandler(file_name, mode='a', encoding='utf-8')]
    )


# сохранение результатов тестов
test_results = {}


# хук для извлечения результата теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        test_results["outcome"] = report.outcome
        if report.failed:
            # извлекаем сообщение об ошибке
            error_message = str(call.excinfo.typename) + ": " + str(call.excinfo.value).split('\n')[0]
            logging.error(f"⚠️ {error_message}")


# фикстура для логирования начала и результата теста
@pytest.fixture(autouse=True)
def auto_log_test(request: pytest.FixtureRequest):
    # начало теста
    test_name = request.node.name
    logging.info(f"🚀 Запуск теста \"{test_name}\"")
    start_time = datetime.now()

    yield

    # результат теста
    outcome = test_results["outcome"]
    if outcome == "passed":
        logging.info(f"✅ Тест \"{test_name}\" завершился успехом")
    elif outcome == "failed":
        logging.error(f"❌ Тест \"{test_name}\" завершился неудачно")
    else:
        logging.info(f"Результат теста: {outcome}")

    # время теста
    end_time = datetime.now()
    duration = end_time - start_time
    logging.info(f"⌛ Продолжительность теста: {duration.total_seconds():.2f} секунд\n" +
                 f"{"=" * 35} {outcome.upper()} {"=" * 35}\n")
