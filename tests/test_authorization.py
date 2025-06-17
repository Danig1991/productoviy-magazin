import pytest

from pages.authorization_page import AuthorizationPage
from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.fixed_navigation_bar.menu.menu import Menu
from pages.products_page import ProductsPage


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_autf_1(authorization):
    # Открыть страницу авторизации (http://91.197.96.80).
    # Ввести корректные логин и пароль покупателя.
    # Нажать на кнопку "Войти".
    driver = authorization

    # Убедиться в успешной авторизации (Найти надпись "Продукты")
    title_products = ProductsPage(driver).get_title_products()
    assert title_products == "Продукты", \
        "Ошибка: Заголовок \"Продукты\" на странице не найден!"
    print("Выполнен переход на страницу \"Продукты\".")


# вход в роли администратора
@pytest.mark.parametrize("authorization", ["admin"], indirect=True)
def test_autf_2(authorization):
    # Открыть страницу авторизации (http://91.197.96.80).
    # Ввести корректные логин и пароль администратора.
    # Нажать на кнопку "Войти".
    driver = authorization

    # Убедиться в успешной авторизации (Найти надпись "Продукты")
    title_products = ProductsPage(driver).get_title_products()
    assert title_products == "Продукты", \
        "Ошибка: Заголовок \"Продукты\" на странице не найден!"
    print("Выполнен переход на страницу \"Продукты\".")

    # Убедиться, что авторизовались в роли администратора
    # (Во вкладке "Меню" найти пункт "Редактировать товары").
    FixedPanelIcons(driver).open_menu()

    item_edit_products = Menu(driver).edit_products_in_menu().text
    assert item_edit_products == "Редактировать товары", \
        "Ошибка: Пункт \"Редактировать товары\" в меню не найден!"
    print("В меню имеется пункт \"Редактировать товары\".")


# вход не выполнен
@pytest.mark.parametrize("authorization", ["none"], indirect=True)
def test_autf_3(authorization):
    # Открыть страницу авторизации (http://91.197.96.80).
    # Оставить поля для ввода логина и пароля пустыми.
    # Нажать на кнопку "Войти".
    driver = authorization

    # Убедиться, что все еще находимся на странице авторизации.
    title_authorization = AuthorizationPage(driver).title_authorization()
    assert title_authorization == "Авторизация", \
        "Ошибка: Заголовок \"Авторизация\" на странице не найден!"
    print("Все еще находимся на странице авторизации.")
