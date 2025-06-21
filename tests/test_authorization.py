import logging

from pages.authorization_page import AuthorizationPage
from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.fixed_navigation_bar.menu.menu import Menu
from pages.products_page import ProductsPage
from utils.double import Double


def test_autf_1(shopper_auth):
    driver = shopper_auth
    logging.info("Вход в роли пользователя")
    logging.info("Открыть страницу авторизации (http://91.197.96.80).")
    logging.info("Ввести корректные логин и пароль покупателя.")
    logging.info("Нажать на кнопку \"Войти\".")

    products_page = ProductsPage(driver)

    logging.info("Убедиться в успешной авторизации (Найти надпись \"Продукты\")")
    title_products = products_page.get_title_products()
    assert title_products == "Продукты", \
        "Ошибка: Заголовок \"Продукты\" на странице не найден!"
    Double.print_and_log("Выполнен переход на страницу \"Продукты\".")


def test_autf_2(admin_auth):
    driver = admin_auth
    logging.info("Вход в роли администратора")
    logging.info("Открыть страницу авторизации (http://91.197.96.80).")
    logging.info("Ввести корректные логин и пароль администратора.")
    logging.info("Нажать на кнопку \"Войти\".")

    products_page = ProductsPage(driver)
    fixed_panel_icons = FixedPanelIcons(driver)
    menu = Menu(driver)

    logging.info("Убедиться в успешной авторизации (Найти надпись \"Продукты\")")
    title_products = products_page.get_title_products()
    assert title_products == "Продукты", \
        "Ошибка: Заголовок \"Продукты\" на странице не найден!"
    print("Выполнен переход на страницу \"Продукты\".")

    logging.info("Убедиться, что авторизовались в роли администратора "
                 "(Во вкладке \"Меню\" найти пункт \"Редактировать товары\").")
    fixed_panel_icons.open_menu()

    item_edit_products = menu.edit_products_in_menu().text
    assert item_edit_products == "Редактировать товары", \
        "Ошибка: Пункт \"Редактировать товары\" в меню не найден!"
    Double.print_and_log("В меню имеется пункт \"Редактировать товары\".")


def test_autf_3(none_auth):
    driver = none_auth
    logging.info("Вход не выполнен")
    logging.info("Открыть страницу авторизации (http://91.197.96.80).")
    logging.info("Оставить поля для ввода логина и пароля пустыми.")
    logging.info("Нажать на кнопку \"Войти\".")

    authorization_page = AuthorizationPage(driver)

    logging.info("Убедиться, что все еще находимся на странице авторизации.")
    title_authorization = authorization_page.title_authorization()
    assert title_authorization == "Авторизация", \
        "Ошибка: Заголовок \"Авторизация\" на странице не найден!"
    Double.print_and_log("Все еще находимся на странице авторизации.")
