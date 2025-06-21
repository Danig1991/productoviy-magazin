import logging

import pytest

from pages.authorization_page import AuthorizationPage
from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.fixed_navigation_bar.menu.menu import Menu
from pages.products_page import ProductsPage
from utils.double import Double


@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_autf_1(authorization):
    logging.info("Вход в роли пользователя")
    logging.info("Открыть страницу авторизации (http://91.197.96.80).")
    logging.info("Ввести корректные логин и пароль покупателя.")
    logging.info("Нажать на кнопку \"Войти\".")
    driver = authorization

    logging.info("Убедиться в успешной авторизации (Найти надпись \"Продукты\")")
    title_products = ProductsPage(driver).get_title_products()
    assert title_products == "Продукты", \
        "Ошибка: Заголовок \"Продукты\" на странице не найден!"
    Double.print_and_log("Выполнен переход на страницу \"Продукты\".")


@pytest.mark.parametrize("authorization", ["admin"], indirect=True)
def test_autf_2(authorization):
    logging.info("Вход в роли администратора")
    logging.info("Открыть страницу авторизации (http://91.197.96.80).")
    logging.info("Ввести корректные логин и пароль администратора.")
    logging.info("Нажать на кнопку \"Войти\".")
    driver = authorization

    logging.info("Убедиться в успешной авторизации (Найти надпись \"Продукты\")")
    title_products = ProductsPage(driver).get_title_products()
    assert title_products == "Продукты", \
        "Ошибка: Заголовок \"Продукты\" на странице не найден!"
    print("Выполнен переход на страницу \"Продукты\".")

    logging.info("Убедиться, что авторизовались в роли администратора "
                 "(Во вкладке \"Меню\" найти пункт \"Редактировать товары\").")
    FixedPanelIcons(driver).open_menu()

    item_edit_products = Menu(driver).edit_products_in_menu().text
    assert item_edit_products == "Редактировать товары", \
        "Ошибка: Пункт \"Редактировать товары\" в меню не найден!"
    Double.print_and_log("В меню имеется пункт \"Редактировать товары\".")


@pytest.mark.parametrize("authorization", ["none"], indirect=True)
def test_autf_3(authorization):
    logging.info("Вход не выполнен")
    logging.info("Открыть страницу авторизации (http://91.197.96.80).")
    logging.info("Оставить поля для ввода логина и пароля пустыми.")
    logging.info("Нажать на кнопку \"Войти\".")
    driver = authorization

    logging.info("Убедиться, что все еще находимся на странице авторизации.")
    title_authorization = AuthorizationPage(driver).title_authorization()
    assert title_authorization == "Авторизация", \
        "Ошибка: Заголовок \"Авторизация\" на странице не найден!"
    Double.print_and_log("Все еще находимся на странице авторизации.")
