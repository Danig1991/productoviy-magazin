import pytest

from configurations.values_for_new_product import NAME, DESCRIPTION, CATEGORY, PRICE, IMAGE_URL, NEW_PRICE
from pages.fixed_navigation_bar.fixed_panel_icons import FixedPanelIcons
from pages.fixed_navigation_bar.menu.editing.add_product_page import AddProductPage
from pages.fixed_navigation_bar.menu.editing.edit_product_details_page import EditProductDetailsPage
from pages.fixed_navigation_bar.menu.editing.edit_products_page import EditProductsPage
from pages.fixed_navigation_bar.menu.menu import Menu
from pages.products_page import ProductsPage


# вход в роли администратора
@pytest.mark.parametrize("authorization", ["admin"], indirect=True)
def test_admin_1(authorization):
    driver = authorization

    fixed_panel_icons = FixedPanelIcons(driver)
    menu = Menu(driver)
    edit_products_page = EditProductsPage(driver)
    add_product_page = AddProductPage(driver)
    products_page = ProductsPage(driver)

    # Нажать на кнопку "Меню".
    fixed_panel_icons.open_menu()
    # Найти и нажать на пункт "Редактировать товары".
    menu.click_edit_products_in_menu()
    # Найти и нажать на кнопку "Добавить товар".
    edit_products_page.click_add_product_button()

    # Заполнить обязательные поля необходимыми данными.
    add_product_page.add_name(name=NAME)
    add_product_page.add_description(description=DESCRIPTION)
    add_product_page.add_category(category=CATEGORY)
    add_product_page.add_price(price=PRICE)
    add_product_page.add_image_url(image_url=IMAGE_URL)

    # Нажать на кнопку "Создать товар".
    add_product_page.click_button_create_product()

    # Во вкладке "Меню" найти и нажать на пункт "Магазин".
    fixed_panel_icons.open_menu()
    menu.click_shop_in_menu()

    # Убедиться, что товар создан и находится в списке продуктов.
    name_test_product = products_page.get_name_test_product()
    assert name_test_product == NAME, \
        f"Ошибка: Продукт \"{NAME}\" на странице не найден!"
    print(f"Созданный товар \"{NAME}\" находится на странице с продуктами.")


# вход в роли администратора
@pytest.mark.parametrize("authorization", ["admin"], indirect=True)
def test_admin_2(authorization):
    driver = authorization

    fixed_panel_icons = FixedPanelIcons(driver)
    menu = Menu(driver)
    edit_products_page = EditProductsPage(driver)
    add_product_page = AddProductPage(driver)

    # Нажать на кнопку "Меню".
    fixed_panel_icons.open_menu()
    # Найти и нажать на пункт "Редактировать товары".
    menu.click_edit_products_in_menu()
    # Найти и нажать на кнопку "Добавить товар".
    edit_products_page.click_add_product_button()

    # Оставить одно обязательное поле незаполненным.
    add_product_page.add_name(name=NAME)
    add_product_page.add_description(description=DESCRIPTION)
    add_product_page.add_category(category=CATEGORY)
    add_product_page.add_price(price=PRICE)

    # Убедиться, что кнопка "Создать товар" не активна.
    button_create_product = add_product_page.button_create_product()
    assert not button_create_product.is_enabled(), \
        "Ошибка: Кнопка не должна быть активной!"
    print("Кнопка \"Создать товар\" не активна.")


# вход в роли администратора
@pytest.mark.parametrize("authorization", ["admin"], indirect=True)
def test_admin_3(authorization):
    driver = authorization

    fixed_panel_icons = FixedPanelIcons(driver)
    menu = Menu(driver)
    edit_products_page = EditProductsPage(driver)
    edit_product_details_page = EditProductDetailsPage(driver)
    products_page = ProductsPage(driver)

    # Нажать на кнопку "Меню".
    fixed_panel_icons.open_menu()
    # Найти и нажать на пункт "Редактировать товары".
    menu.click_edit_products_in_menu()
    # Найти добавленный ранее товар и нажать на кнопку редактирования (иконка карандаша).
    edit_products_page.click_edit_product_button()

    # Редактировать поле "Цена, Р", указать новое значение.
    edit_product_details_page.new_price(new_price=NEW_PRICE)
    # Найти и нажать на кнопку "Обновить товар".
    edit_product_details_page.click_button_update_product()

    # Во вкладке "Меню" найти и нажать на пункт "Магазин".
    fixed_panel_icons.open_menu()
    menu.click_shop_in_menu()

    # Убедиться, что цена товара изменилась на сохраненную ранее.
    price_test_product = products_page.get_price_test_product()
    assert price_test_product == NEW_PRICE, \
        f"Ошибка: Цена \"{price_test_product}\" не соответствует измененной!"
    print("Цена тестового продукта изменилась на сохраненную ранее.")


# вход в роли администратора
@pytest.mark.parametrize("authorization", ["admin"], indirect=True)
def test_admin_4(authorization):
    driver = authorization

    fixed_panel_icons = FixedPanelIcons(driver)
    menu = Menu(driver)
    edit_products_page = EditProductsPage(driver)
    edit_product_details_page = EditProductDetailsPage(driver)

    # Нажать на кнопку "Меню".
    fixed_panel_icons.open_menu()
    # Найти и нажать на пункт "Редактировать товары".
    menu.click_edit_products_in_menu()
    # Найти добавленный товар и нажать на кнопку редактирования (иконка карандаша).
    edit_products_page.click_edit_product_button()

    # Очистить поле "Описание" и оставить незаполненным.
    edit_product_details_page.clear_description()

    # Убедиться, что кнопка "Обновить товар" не активна.
    button_update_product = edit_product_details_page.button_update_product()
    assert not button_update_product.is_enabled(), \
        "Ошибка: Кнопка не должна быть активной!"
    print("Кнопка \"Обновить товар\" не активна.")


# вход в роли администратора
@pytest.mark.parametrize("authorization", ["admin"], indirect=True)
def test_admin_5(authorization):
    driver = authorization

    fixed_panel_icons = FixedPanelIcons(driver)
    menu = Menu(driver)
    edit_products_page = EditProductsPage(driver)
    products_page = ProductsPage(driver)

    # Нажать на кнопку "Меню".
    fixed_panel_icons.open_menu()
    # Найти и нажать на пункт "Редактировать товары".
    menu.click_edit_products_in_menu()

    # Найти добавленный ранее товар и нажать на кнопку удаления (иконка корзины).
    edit_products_page.remove_test_product()

    # Во вкладке "Меню" найти и нажать на пункт "Магазин".
    fixed_panel_icons.open_menu()
    menu.click_shop_in_menu()

    # Убедиться, что удаленный товар больше не присутствует в списке продуктов.
    product_names = products_page.get_list_of_product_names()
    for name in product_names:
        assert "Тестовый" not in name, \
            "Ошибка: Найден продукт со словом \"Тестовый\" в наименовании!"
    print("Тестовый продукт отсутствует в списке продуктов.")
