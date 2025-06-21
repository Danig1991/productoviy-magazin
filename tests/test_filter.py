import logging

from pages.products_page import ProductsPage
from utils.config import FilterConfig
from utils.double import Double


def test_filter_1(shopper_auth):
    driver = shopper_auth
    logging.info("Вход в роли пользователя")

    products_page = ProductsPage(driver)
    sort_by_price_low_to_high = FilterConfig.SORT_BY_PRICE_LOW_TO_HIGH

    logging.info("На странице с продуктами найти и нажать выпадающий список.")
    logging.info("В выпадающем списке выбрать значение: \"Цена: Сначала подешевле\".")
    products_page.select_dropdown_option(sort_by_price_low_to_high)

    logging.info("Убедиться, что ассортимент товара отсортирован верно.")
    product_prices = products_page.get_list_of_product_prices()
    assert product_prices == sorted(product_prices), \
        f"Ошибка: Цены не отсортированы по возрастанию! Фактический порядок: {product_prices}"
    Double.print_and_log("Товар отображается по цене от меньшей к большей.")


def test_filter_2(shopper_auth):
    driver = shopper_auth
    logging.info("Вход в роли пользователя")

    products_page = ProductsPage(driver)
    sort_by_price_high_to_low = FilterConfig.SORT_BY_PRICE_HIGH_TO_LOW

    logging.info("На странице с продуктами найти и нажать выпадающий список.")
    logging.info("В выпадающем списке выбрать значение: \"Цена: Сначала подороже\".")
    products_page.select_dropdown_option(sort_by_price_high_to_low)

    logging.info("Убедиться, что ассортимент товара отсортирован верно.")
    product_prices = products_page.get_list_of_product_prices()
    assert product_prices == sorted(product_prices, reverse=True), \
        f"Ошибка: Цены не отсортированы по убыванию! Фактический порядок: {product_prices}"
    Double.print_and_log("Товар отображается по цене от большей к меньшей.")


def test_filter_3(shopper_auth):
    driver = shopper_auth
    logging.info("Вход в роли пользователя")

    products_page = ProductsPage(driver)
    sort_by_name_a_to_z = FilterConfig.SORT_BY_NAME_A_TO_Z

    logging.info("На странице с продуктами найти и нажать выпадающий список.")
    logging.info("В выпадающем списке выбрать значение: \"Наименование: от А до Я\".")
    products_page.select_dropdown_option(sort_by_name_a_to_z)

    logging.info("Убедиться, что ассортимент товара отсортирован верно.")
    product_names = products_page.get_list_of_product_names()
    assert product_names == sorted(product_names), \
        f"Ошибка: Наименования продуктов не отсортированы по алфавиту! Фактический порядок: {product_names}"
    Double.print_and_log("Товар отображается в алфавитном порядке.")


def test_filter_4(shopper_auth):
    driver = shopper_auth
    logging.info("Вход в роли пользователя")

    products_page = ProductsPage(driver)
    sort_by_name_z_to_a = FilterConfig.SORT_BY_NAME_Z_TO_A

    logging.info("На странице с продуктами найти и нажать выпадающий список.")
    logging.info("В выпадающем списке выбрать значение: \"Наименование: от Я до А\".")
    products_page.select_dropdown_option(sort_by_name_z_to_a)

    logging.info("Убедиться, что ассортимент товара отсортирован верно.")
    product_names = products_page.get_list_of_product_names()
    assert product_names == sorted(product_names, reverse=True), \
        (f"Ошибка: Наименования продуктов не отсортированы по алфавиту в обратном порядке! "
         f"Фактический порядок: {product_names}")
    Double.print_and_log("Товар отображается по алфавиту в обратном порядке.")


def test_filter_5(shopper_auth):
    driver = shopper_auth
    logging.info("Вход в роли пользователя")

    products_page = ProductsPage(driver)
    burger = FilterConfig.BURGER
    sandwich = FilterConfig.SANDWICH
    pie = FilterConfig.PIE
    roll = FilterConfig.ROLL

    logging.info("На странице с продуктами найти и нажать кнопку фильтра (иконка с ползунками).")
    logging.info("В блоке \"Категории\" оставить активным чек-бокс \"Бургер\".")
    products_page.click_filter_menu()
    products_page.checkbox_activation(value=burger, activate=True)
    products_page.checkbox_activation(value=sandwich, activate=False)
    products_page.checkbox_activation(value=pie, activate=False)
    products_page.checkbox_activation(value=roll, activate=False)
    products_page.click_filter_menu()

    logging.info("Убедиться, что товар соответствует выбранной категории.")
    product_names = ProductsPage(driver).get_list_of_product_names()
    for name in product_names:
        assert "Бургер" in name, \
            f"Ошибка: Продукт: \"{name}\" - не соответствует категории \"Бургер\"!"
    Double.print_and_log("Продукты соответствуют категории \"Бургер\".")


def test_filter_6(shopper_auth):
    driver = shopper_auth
    logging.info("Вход в роли пользователя")

    products_page = ProductsPage(driver)
    burger = FilterConfig.BURGER
    sandwich = FilterConfig.SANDWICH
    pie = FilterConfig.PIE
    roll = FilterConfig.ROLL

    logging.info("На странице с продуктами найти и нажать кнопку фильтра (иконка с ползунками).")
    logging.info("В блоке \"Категории\" оставить активным чек-бокс \"Сэндвич\".")
    products_page.click_filter_menu()
    products_page.checkbox_activation(value=sandwich, activate=True)
    products_page.checkbox_activation(value=burger, activate=False)
    products_page.checkbox_activation(value=pie, activate=False)
    products_page.checkbox_activation(value=roll, activate=False)
    products_page.click_filter_menu()

    logging.info("Убедиться, что товар соответствует выбранной категории.")
    product_names = ProductsPage(driver).get_list_of_product_names()
    for name in product_names:
        assert "Сэндвич" in name, \
            f"Ошибка: Продукт: \"{name}\" - не соответствует категории \"Сэндвич\"!"
    Double.print_and_log("Продукты соответствуют категории \"Сэндвич\".")


def test_filter_7(shopper_auth):
    driver = shopper_auth
    logging.info("Вход в роли пользователя")

    products_page = ProductsPage(driver)
    burger = FilterConfig.BURGER
    sandwich = FilterConfig.SANDWICH
    pie = FilterConfig.PIE
    roll = FilterConfig.ROLL

    logging.info("На странице с продуктами найти и нажать кнопку фильтра (иконка с ползунками).")
    logging.info("В блоке \"Категории\" не активен ни один чек-бокс.")
    products_page.click_filter_menu()
    products_page.checkbox_activation(value=sandwich, activate=False)
    products_page.checkbox_activation(value=burger, activate=False)
    products_page.checkbox_activation(value=pie, activate=False)
    products_page.checkbox_activation(value=roll, activate=False)
    products_page.click_filter_menu()

    logging.info("Убедиться, что товар отсутствует.")
    product_card_count = products_page.get_product_card_count()
    assert product_card_count == 0, \
        f"Ошибка: Найдено {product_card_count} товаров, ожидалось: 0"

    Double.print_and_log("Ни один товар не отображается.")


def test_filter_8(shopper_auth):
    driver = shopper_auth
    logging.info("Вход в роли пользователя")

    products_page = ProductsPage(driver)
    min_price = FilterConfig.MIN_PRICE
    max_price = FilterConfig.MAX_PRICE

    logging.info("На странице с продуктами найти и нажать кнопку фильтра (иконка с ползунками).")
    logging.info("В блоке \"Цена\" ввести данные: в поле \"от\" - 100, в поле \"до\" - 150.")
    products_page.click_filter_menu()
    products_page.set_price_filter_range(min_price, max_price)
    products_page.click_filter_menu()

    logging.info("Убедиться, что товар соответствует введенному ценовому диапазону.")
    product_prices = products_page.get_list_of_product_prices()
    for price in product_prices:
        assert min_price <= price <= max_price, \
            f"Ошибка: Цена {price} вне диапазона: от {min_price} до {max_price}!"
    Double.print_and_log("Товар соответствует введенному ценовому диапазону.")
