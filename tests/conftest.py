import pytest

from configurations.action_with_product import PRODUCT_NAME, QUANTITY_2
from configurations.login_password import (
    SHOPPER_LOGIN,
    SHOPPER_PASSWORD,
    ADMIN_PASSWORD,
    ADMIN_LOGIN
)
from configurations.url import BASE_URL
from pages.authorization_page import AuthorizationPage
from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.products_page import ProductsPage
from pages.shopping_cart_page import ShoppingCartPage
from utils.browser import Browser

# роли для авторизации
roles = {
    "admin": {
        "login": ADMIN_LOGIN,
        "password": ADMIN_PASSWORD,
        "text_authorization": "\nАвторизация на сайте администратором."
    },
    "shopper": {
        "login": SHOPPER_LOGIN,
        "password": SHOPPER_PASSWORD,
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
    browser.open(url=BASE_URL)
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

    products_page = ProductsPage(driver)
    products_page.set_product_quantity(product_name=PRODUCT_NAME, target_quantity=QUANTITY_2)


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
