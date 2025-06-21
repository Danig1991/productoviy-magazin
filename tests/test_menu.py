import logging

import pytest

from pages.authorization_page import AuthorizationPage
from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.fixed_navigation_bar.menu.menu import Menu
from pages.products_page import ProductsPage
from pages.shopping_cart_page import ShoppingCartPage
from utils.double import Double


@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_menu_1(authorization):
    logging.info("Вход в роли пользователя")
    driver = authorization

    fixed_panel_icons = FixedPanelIcons(driver)
    menu = Menu(driver)

    logging.info("Нажать на кнопку \"Меню\".")
    fixed_panel_icons.open_menu()

    logging.info("Убедиться в наличии пунктов: \"Магазин\", \"Корзинка\", \"Выход\".")
    shop_in_menu = menu.shop_in_menu()
    shopping_cart_in_menu = menu.shopping_cart_in_menu()
    exit_button_in_menu = menu.exit_button_in_menu()

    assert shop_in_menu.is_displayed(), "Ошибка: Пункт \"Магазин\" не найден или не отображается!"
    assert shopping_cart_in_menu.is_displayed(), "Ошибка: Пункт \"Корзинка\" не найден или не отображается!"
    assert exit_button_in_menu.is_displayed(), "Ошибка: Кнопка \"Выход\" не найдена или не отображается!"

    Double.print_and_log("Пункты: \"Магазин\", \"Корзинка\", \"Выход\" присутствуют в меню.")


@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_menu_2(authorization):
    logging.info("Вход в роли пользователя")
    driver = authorization

    fixed_panel_icons = FixedPanelIcons(driver)
    menu = Menu(driver)
    products_page = ProductsPage(driver)

    logging.info("Нажать на кнопку \"Меню\".")
    fixed_panel_icons.open_menu()

    logging.info("Во вкладке \"Меню\" найти и нажать на пункт \"Магазин\".")
    menu.click_shop_in_menu()

    logging.info("Убедиться, что находимся на странице \"Продукты\".")
    title_products = products_page.get_title_products()
    assert title_products == "Продукты", \
        "Ошибка: Заголовок \"Продукты\" на странице не найден!"
    Double.print_and_log("Выполнен корректный переход на страницу \"Продукты\".")


@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_menu_3(authorization):
    logging.info("Вход в роли пользователя")
    driver = authorization

    fixed_panel_icons = FixedPanelIcons(driver)
    menu = Menu(driver)
    shopping_cart_page = ShoppingCartPage(driver)

    logging.info("Нажать на кнопку \"Меню\".")
    fixed_panel_icons.open_menu()

    logging.info("Во вкладке \"Меню\" найти и нажать на пункт \"Корзинка\".")
    menu.click_shopping_cart_in_menu()

    logging.info("Убедиться, что находимся на странице \"Корзинка\".")
    title_shopping_cart = shopping_cart_page.get_title_shopping_cart()
    assert title_shopping_cart == "Корзинка", \
        "Ошибка: Заголовок \"Корзинка\" на странице не найден!"
    Double.print_and_log("Выполнен корректный переход на страницу \"Корзинка\".")


@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_menu_4(authorization):
    logging.info("Вход в роли пользователя")
    driver = authorization

    fixed_panel_icons = FixedPanelIcons(driver)
    menu = Menu(driver)
    authorization_page = AuthorizationPage(driver)

    logging.info("Нажать на кнопку \"Меню\".")
    fixed_panel_icons.open_menu()

    logging.info("Во вкладке \"Меню\" найти и нажать на кнопку \"Выход\".")
    menu.click_exit_button_in_menu()

    logging.info("Убедиться, что находимся на странице авторизации.")
    title_authorization = authorization_page.title_authorization()
    assert title_authorization == "Авторизация", \
        "Ошибка: Заголовок \"Авторизация\" на странице не найден!"
    Double.print_and_log("Завершение сессии пользователя, переход на страницу авторизации.")
