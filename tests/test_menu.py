import logging

import allure

from pages.authorization_page import AuthorizationPage
from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.fixed_navigation_bar.menu.menu import Menu
from pages.products_page import ProductsPage
from pages.shopping_cart_page import ShoppingCartPage


@allure.epic("Тест меню.")
@allure.title("Вкладка 'Меню' должна содержать пункты: 'Магазин', 'Корзинка', 'Выход'.")
def test_menu_1(shopper_auth):
    driver = shopper_auth

    # Нажать на кнопку 'Меню'.
    FixedPanelIcons(driver).open_menu()

    logging.info("Убедиться в наличии пунктов: 'Магазин', 'Корзинка', 'Выход'.")
    shop_in_menu = Menu(driver).shop_in_menu()
    shopping_cart_in_menu = Menu(driver).shopping_cart_in_menu()
    exit_button_in_menu = Menu(driver).exit_button_in_menu()

    assert shop_in_menu.is_displayed(), "Ошибка: Пункт 'Магазин' не найден или не отображается!"
    assert shopping_cart_in_menu.is_displayed(), "Ошибка: Пункт 'Корзинка' не найден или не отображается!"
    assert exit_button_in_menu.is_displayed(), "Ошибка: Кнопка 'Выход' не найдена или не отображается!"

    logging.info("Пункты: 'Магазин', 'Корзинка', 'Выход' присутствуют в меню.")


@allure.epic("Тест меню.")
@allure.title("Пункт 'Магазин' служит для перевода на страницу с каталогом товаров.")
def test_menu_2(shopper_auth):
    driver = shopper_auth

    # Нажать на кнопку 'Меню'.
    FixedPanelIcons(driver).open_menu()
    # Во вкладке 'Меню' найти и нажать на пункт 'Магазин'.
    Menu(driver).click_shop_in_menu()

    logging.info("Убедиться, что находимся на странице 'Продукты'.")
    title_products = ProductsPage(driver).get_title_products()
    assert title_products == "Продукты", \
        "Ошибка: Заголовок 'Продукты' на странице не найден!"
    logging.info("Выполнен корректный переход на страницу 'Продукты'.")


@allure.epic("Тест меню.")
@allure.title("Пункт 'Корзинка' служит для перевода на страницу с товарами, добавленными в корзину.")
def test_menu_3(shopper_auth):
    driver = shopper_auth

    # Нажать на кнопку 'Меню'.
    FixedPanelIcons(driver).open_menu()
    # Во вкладке 'Меню' найти и нажать на пункт 'Корзинка'.
    Menu(driver).click_shopping_cart_in_menu()

    logging.info("Убедиться, что находимся на странице 'Корзинка'.")
    title_shopping_cart = ShoppingCartPage(driver).get_title_shopping_cart()
    assert title_shopping_cart == "Корзинка", \
        "Ошибка: Заголовок 'Корзинка' на странице не найден!"
    logging.info("Выполнен корректный переход на страницу 'Корзинка'.")


@allure.epic("Тест меню.")
@allure.title("Кнопка 'Выход' служит для завершения сессии пользователя.")
def test_menu_4(shopper_auth):
    driver = shopper_auth

    # Нажать на кнопку 'Меню'.
    FixedPanelIcons(driver).open_menu()
    # Во вкладке 'Меню' найти и нажать на кнопку 'Выход'.
    Menu(driver).click_exit_button_in_menu()

    logging.info("Убедиться, что находимся на странице авторизации.")
    title_authorization = AuthorizationPage(driver).get_title_authorization()
    assert title_authorization == "Авторизация", \
        "Ошибка: Заголовок 'Авторизация' на странице не найден!"
    logging.info("Завершение сессии пользователя, переход на страницу авторизации.")
