import logging

import allure

from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.fixed_navigation_bar.menu.editing.add_product_page import AddProductPage
from pages.fixed_navigation_bar.menu.editing.edit_product_details_page import EditProductDetailsPage
from pages.fixed_navigation_bar.menu.editing.edit_products_page import EditProductsPage
from pages.fixed_navigation_bar.menu.menu import Menu
from pages.products_page import ProductsPage
from utils.config import ProductData


@allure.epic("Тест профиля администратора")
@allure.title("Добавление нового товара в ассортимент.")
def test_admin_1(admin_auth):
    driver = admin_auth
    product_data = ProductData().get_product_data()
    name = product_data["Наименование"]

    # Нажать на кнопку 'Меню'.
    FixedPanelIcons(driver).open_menu()
    # Найти и нажать на пункт 'Редактировать товары'.
    Menu(driver).click_edit_products_in_menu()
    # Найти и нажать на кнопку 'Добавить товар'.
    EditProductsPage(driver).click_add_product_button()

    logging.info("Заполнить обязательные поля необходимыми данными.")
    AddProductPage(driver).add_product_data(
        name=name,
        description=product_data["Описание"],
        category=product_data["Ожидаемая категория"],
        price=product_data["Цена"],
        image_url=product_data["URL картинки"]
    )

    # Нажать на кнопку 'Создать товар'.
    AddProductPage(driver).click_button_create_product()
    # Во вкладке 'Меню' найти и нажать на пункт 'Магазин'.
    FixedPanelIcons(driver).open_menu()
    Menu(driver).click_shop_in_menu()

    logging.info("Убедиться, что товар создан и находится в списке продуктов.")
    name_test_product = ProductsPage(driver).get_name_test_product()
    assert name_test_product == name, \
        f"Ошибка: Продукт '{name}' на странице не найден!"
    logging.info(f"Созданный товар '{name}' находится на странице с продуктами.")


@allure.epic("Тест профиля администратора")
@allure.title("Проверка добавления нового товара, оставить незаполненным обязательное поле.")
def test_admin_2(admin_auth):
    driver = admin_auth
    product_data = ProductData().get_product_data()

    # Нажать на кнопку 'Меню'.
    FixedPanelIcons(driver).open_menu()
    # Найти и нажать на пункт 'Редактировать товары'.
    Menu(driver).click_edit_products_in_menu()
    # Найти и нажать на кнопку 'Добавить товар'.
    EditProductsPage(driver).click_add_product_button()

    logging.info("Оставить одно обязательное поле незаполненным.")
    AddProductPage(driver).add_product_data(
        name=product_data["Наименование"],
        description=product_data["Описание"],
        category=product_data["Ожидаемая категория"],
        price=product_data["Цена"]
    )

    logging.info("Убедиться, что кнопка 'Создать товар' не активна.")
    button_create_product = AddProductPage(driver).button_create_product()
    assert not button_create_product.is_enabled(), \
        "Ошибка: Кнопка не должна быть активной!"
    logging.info("Кнопка 'Создать товар' не активна.")


@allure.epic("Тест профиля администратора")
@allure.title("Редактирование имеющегося товара.")
def test_admin_3(admin_auth):
    driver = admin_auth
    new_price = ProductData().get_product_data()["Новая цена"]

    # Нажать на кнопку 'Меню'.
    FixedPanelIcons(driver).open_menu()
    # Найти и нажать на пункт 'Редактировать товары'.
    Menu(driver).click_edit_products_in_menu()
    # Найти добавленный ранее товар и нажать на кнопку редактирования (иконка карандаша).
    EditProductsPage(driver).click_edit_product_button()
    # Редактировать поле 'Цена, Р', указать новое значение.
    EditProductDetailsPage(driver).new_price(new_price)
    # Найти и нажать на кнопку 'Обновить товар'.
    EditProductDetailsPage(driver).click_button_update_product()
    # Во вкладке 'Меню' найти и нажать на пункт 'Магазин'.
    FixedPanelIcons(driver).open_menu()
    Menu(driver).click_shop_in_menu()

    logging.info("Убедиться, что цена товара изменилась на сохраненную ранее.")
    price_test_product = ProductsPage(driver).get_price_test_product()
    assert price_test_product == new_price, \
        f"Ошибка: Цена '{price_test_product}' не соответствует измененной!"
    logging.info("Цена тестового продукта изменилась на сохраненную ранее.")


@allure.epic("Тест профиля администратора")
@allure.title("Проверка редактирования имеющегося товара, оставить незаполненным обязательное поле.")
def test_admin_4(admin_auth):
    driver = admin_auth

    # Нажать на кнопку 'Меню'.
    FixedPanelIcons(driver).open_menu()
    # Найти и нажать на пункт 'Редактировать товары'.
    Menu(driver).click_edit_products_in_menu()
    # Найти добавленный товар и нажать на кнопку редактирования (иконка карандаша).
    EditProductsPage(driver).click_edit_product_button()
    # Очистить поле 'Описание' и оставить незаполненным.
    EditProductDetailsPage(driver).clear_description()

    logging.info("Убедиться, что кнопка 'Обновить товар' не активна.")
    button_update_product = EditProductDetailsPage(driver).button_update_product()
    assert not button_update_product.is_enabled(), \
        "Ошибка: Кнопка не должна быть активной!"
    logging.info("Кнопка 'Обновить товар' не активна.")


@allure.epic("Тест профиля администратора")
@allure.title("Удаление товара из ассортимента.")
def test_admin_5(admin_auth):
    driver = admin_auth

    # Нажать на кнопку 'Меню'.
    FixedPanelIcons(driver).open_menu()
    # Найти и нажать на пункт 'Редактировать товары'.
    Menu(driver).click_edit_products_in_menu()
    # Найти добавленный ранее товар и нажать на кнопку удаления (иконка корзины).
    EditProductsPage(driver).remove_test_product()
    # Во вкладке 'Меню' найти и нажать на пункт 'Магазин'.
    FixedPanelIcons(driver).open_menu()
    Menu(driver).click_shop_in_menu()

    logging.info("Убедиться, что удаленный товар больше не присутствует в списке продуктов.")
    product_names = ProductsPage(driver).get_list_of_product_names()
    for name in product_names:
        assert "Тестовый" not in name, \
            "Ошибка: Найден продукт со словом 'Тестовый' в наименовании!"
    logging.info("Тестовый продукт отсутствует в списке продуктов.")
