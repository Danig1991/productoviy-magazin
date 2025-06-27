import logging

import allure

from pages.authorization_page import AuthorizationPage
from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.fixed_navigation_bar.menu.menu import Menu
from pages.products_page import ProductsPage


@allure.epic("Тест авторизации.")
@allure.title("Авторизация на сайте покупателем.")
def test_autf_1(shopper_auth):
    # Открыть страницу авторизации (http://91.197.96.80).
    # Ввести корректные логин и пароль покупателя.
    # Нажать на кнопку 'Войти'.

    driver = shopper_auth
    products_page = ProductsPage(driver)

    logging.info("Убедиться в успешной авторизации (Найти надпись 'Продукты')")
    title_products = products_page.get_title_products()
    assert title_products == "Продукты", \
        "Ошибка: Заголовок 'Продукты' на странице не найден!"
    logging.info("Выполнен переход на страницу 'Продукты'.")


@allure.epic("Тест авторизации.")
@allure.title("Авторизация на сайте администратором.")
def test_autf_2(admin_auth):
    # Открыть страницу авторизации (http://91.197.96.80).
    # Ввести корректные логин и пароль администратора.
    # Нажать на кнопку 'Войти'.

    driver = admin_auth
    products_page = ProductsPage(driver)
    fixed_panel_icons = FixedPanelIcons(driver)
    menu = Menu(driver)

    logging.info("Убедиться в успешной авторизации (Найти надпись 'Продукты')")
    title_products = products_page.get_title_products()
    assert title_products == "Продукты", \
        "Ошибка: Заголовок 'Продукты' на странице не найден!"
    logging.info("Выполнен переход на страницу 'Продукты'.")

    logging.info("Убедиться, что авторизовались в роли администратора "
                 "(Во вкладке 'Меню' найти пункт 'Редактировать товары').")
    fixed_panel_icons.open_menu()
    item_edit_products = menu.edit_products_in_menu().text
    assert item_edit_products == "Редактировать товары", \
        "Ошибка: Пункт 'Редактировать товары' в меню не найден!"
    logging.info("В меню имеется пункт 'Редактировать товары'.")


@allure.epic("Тест авторизации.")
@allure.title("Проверка авторизации с пустыми обязательными полями.")
def test_autf_3(none_auth):
    # Открыть страницу авторизации (http://91.197.96.80).
    # Оставить поля для ввода логина и пароля пустыми.
    # Нажать на кнопку 'Войти'.

    driver = none_auth
    authorization_page = AuthorizationPage(driver)

    logging.info("Убедиться, что все еще находимся на странице авторизации.")
    title_authorization = authorization_page.get_title_authorization()
    assert title_authorization == "Авторизация", \
        "Ошибка: Заголовок 'Авторизация' на странице не найден!"
    logging.info("Все еще находимся на странице авторизации.")
