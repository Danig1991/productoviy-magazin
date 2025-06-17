import pytest

from pages.authorization_page import AuthorizationPage
from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.fixed_navigation_bar.menu.menu import Menu
from pages.products_page import ProductsPage
from pages.shopping_cart_page import ShoppingCartPage


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_menu_1(authorization):
    driver = authorization

    menu_items = Menu(driver)

    # Нажать на кнопку "Меню".
    FixedPanelIcons(driver).open_menu()

    # Убедиться в наличии пунктов: "Магазин", "Корзинка", "Выход".
    shop_in_menu = menu_items.shop_in_menu()
    shopping_cart_in_menu = menu_items.shopping_cart_in_menu()
    exit_button_in_menu = menu_items.exit_button_in_menu()

    assert shop_in_menu.is_displayed(), "Ошибка: Пункт \"Магазин\" не найден или не отображается!"
    assert shopping_cart_in_menu.is_displayed(), "Ошибка: Пункт \"Корзинка\" не найден или не отображается!"
    assert exit_button_in_menu.is_displayed(), "Ошибка: Кнопка \"Выход\" не найдена или не отображается!"

    print("Пункты: \"Магазин\", \"Корзинка\", \"Выход\" присутствуют в меню.")


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_menu_2(authorization):
    driver = authorization

    # Нажать на кнопку "Меню".
    FixedPanelIcons(driver).open_menu()
    # Во вкладке "Меню" найти и нажать на пункт "Магазин".
    Menu(driver).click_shop_in_menu()

    # Убедиться, что находимся на странице "Продукты".
    title_products = ProductsPage(driver).get_title_products()
    assert title_products == "Продукты", \
        "Ошибка: Заголовок \"Продукты\" на странице не найден!"
    print("Выполнен корректный переход на страницу \"Продукты\".")


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_menu_3(authorization):
    driver = authorization

    # Нажать на кнопку "Меню".
    FixedPanelIcons(driver).open_menu()
    # Во вкладке "Меню" найти и нажать на пункт "Корзинка".
    Menu(driver).click_shopping_cart_in_menu()

    # Убедиться, что находимся на странице "Корзинка".
    title_shopping_cart = ShoppingCartPage(driver).get_title_shopping_cart()
    assert title_shopping_cart == "Корзинка", \
        "Ошибка: Заголовок \"Корзинка\" на странице не найден!"
    print("Выполнен корректный переход на страницу \"Корзинка\".")


# вход в роли пользователя
@pytest.mark.parametrize("authorization", ["shopper"], indirect=True)
def test_menu_4(authorization):
    driver = authorization

    # Нажать на кнопку "Меню".
    FixedPanelIcons(driver).open_menu()
    # Во вкладке "Меню" найти и нажать на кнопку "Выход".
    Menu(driver).click_exit_button_in_menu()

    # Убедиться, что находимся на странице авторизации.
    title_authorization = AuthorizationPage(driver).title_authorization()
    assert title_authorization == "Авторизация", \
        "Ошибка: Заголовок \"Авторизация\" на странице не найден!"
    print("Завершение сессии пользователя, переход на страницу авторизации.")
