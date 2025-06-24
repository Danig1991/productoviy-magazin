import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utils.expectation import Expectation

TITLE_PRODUCTS_LOCATOR = (By.XPATH, "//*[@class='navbar-brand']")
TEST_PRODUCT_LOCATOR = (By.XPATH, "//*[contains(text(), 'Тестовый')]")
PRICE_TEST_PRODUCT_LOCATOR = (
    By.XPATH,
    "//*[contains(text(), 'Тестовый')]"
    "/ancestor::div[contains(@class, 'store-card m-3')]"
    "//div[contains(@class, 'fs-5')]"
)
PRODUCT_NAMES_LOCATOR = (By.CSS_SELECTOR, ".card-title")
DROPDOWN_LOCATOR = (By.CSS_SELECTOR, ".form-select")
PRICES_OF_PRODUCTS_LOCATOR = (By.CSS_SELECTOR, "div.fs-5")
FILTER_BUTTON_LOCATOR = (By.XPATH, "//button[@data-bs-toggle='dropdown']")
PRODUCT_CARDS_LOCATOR = (By.CSS_SELECTOR, ".store-card.m-3")
PRICE_FROM_LOCATOR = (By.ID, "priceFrom")
PRICE_TO_LOCATOR = (By.ID, "priceTo")
PLUS_BUTTON_LOCATOR = (
    By.XPATH,
    "//span[@class='material-symbols-outlined m-auto m-2' and text()='add']/ancestor::button"
)


class ProductsPage(Expectation):

    @allure.step("Получить заголовок 'Продукты'")
    def get_title_products(self):
        return self.visibility_of_element_located(TITLE_PRODUCTS_LOCATOR, "Продукты").text

    @allure.step("Получить имя тестового продукта")
    def get_name_test_product(self):
        return self.visibility_of_element_located(TEST_PRODUCT_LOCATOR, "Тестовый").text

    @allure.step("Получить цену тестового продукта")
    def get_price_test_product(self):
        text_price_test_product = self.visibility_of_element_located(
            PRICE_TEST_PRODUCT_LOCATOR,
            "Цена тестового продукта"
        ).text
        print(f"Найдена цена тестового продукта - '{text_price_test_product}'.")
        return int(float(text_price_test_product[:-2]))

    @allure.step("Получить список наименований продукции")
    def get_list_of_product_names(self):
        names_of_elements = self.visibility_of_all_elements_located(
            PRODUCT_NAMES_LOCATOR,
            "Наименования продукции"
        )
        product_names = []
        for element in names_of_elements:
            product_names.append(element.text)

        return product_names

    @allure.step("Выбрать вариант из выпадающего списка")
    def select_dropdown_option(self, value):
        dropdown = self.visibility_of_element_located(DROPDOWN_LOCATOR, "Выпадающий список")

        select = Select(dropdown)
        select.select_by_visible_text(value)
        print(f"В выпадающем списке выбрано значение: '{value}'.")

    @allure.step("Получить список цен продуктов")
    def get_list_of_product_prices(self):
        price_elements = self.visibility_of_all_elements_located(PRICES_OF_PRODUCTS_LOCATOR, "Цены продуктов")

        prices_of_products = []
        for element in price_elements:
            prices_of_products.append(int(float(element.text[:-2])))

        return prices_of_products

    @allure.step("Нажать меню фильтров")
    def click_filter_menu(self):
        filter_button = self.visibility_of_element_located(FILTER_BUTTON_LOCATOR, "Меню фильтров")
        filter_button.click()
        if "true" in filter_button.get_attribute("aria-expanded"):
            print("Меню фильтров открыто.")
        else:
            print("Меню фильтров закрыто.")

    @allure.step("Активация чек-боксов в 'Категории'")
    def checkbox_activation(self, value, activate):
        checkbox_locator = (By.XPATH, f"//input[@value='{value}']")
        checkbox_element = self.visibility_of_element_located(checkbox_locator, f"Категория: {value}")
        current_state = checkbox_element.is_selected()
        action_needed = current_state != activate

        if action_needed:
            checkbox_element.click()
            new_state = not current_state
            action_text = "изменена на"
        else:
            new_state = current_state
            action_text = "осталась"

        status = "активна" if new_state else "не активна"
        print(f"Категория: '{value}\' - {action_text} {status}.")

    @allure.step("Получить количество карточек продукта")
    def get_product_card_count(self):
        return len(self.find_elements(PRODUCT_CARDS_LOCATOR[0], PRODUCT_NAMES_LOCATOR[1]))

    @allure.step("Установка диапазона цены")
    def set_price_filter_range(self, min_price, max_price):
        def set_price(locator, error_msg, value):
            price = self.visibility_of_element_located(locator, error_msg)
            price.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
            price.send_keys(value)

        set_price(PRICE_FROM_LOCATOR, "Цена: от", min_price)
        set_price(PRICE_TO_LOCATOR, "Цена: до", max_price)
        print(f"Установлен диапазон цены от {min_price} до {max_price}.")

    @allure.step("Получить значение счетчика продукта")
    def get_product_counter_value(self, product_name):
        time.sleep(2)
        counter_value = self.visibility_of_element_located(
            (
                By.XPATH,
                f"//*[contains(text(), '{product_name}')]"
                "/ancestor::div[contains(@class, 'store-card m-3')]"
                "//input[contains(@class, 'form-control shadow-none')]"

            ),
            f"Счетчик продукта '{product_name}'"
        ).get_attribute("value")
        return int(counter_value)

    # Нажать выбранную кнопку несколько раз
    def _click_selected_button_repeatedly(self, product_name, action, clicks):
        selected_button = self.visibility_of_element_located(
            (
                By.XPATH,
                f"//*[contains(text(), '{product_name}')]"
                "/ancestor::div[contains(@class, 'store-card m-3')]"
                f"//span[text()='{action}']"
                "/ancestor::button"
            ),
            f"Кнопка {'+' if action == 'add' else '-'} для '{product_name}'"
        )
        self.move_to_element(selected_button)

        for _ in range(clicks):
            selected_button.click()
            time.sleep(0.15)

    @allure.step("Установить количество продукта")
    def set_product_quantity(self, product_name, target_quantity):
        current_quantity = self.get_product_counter_value(product_name)
        if current_quantity == target_quantity:
            print(f"Количество продукта '{product_name}' - {current_quantity} шт.")
            return

        while True:
            print("Изменение количества продукта.")
            new_quantity = self.get_product_counter_value(product_name)

            action = "add" if target_quantity > new_quantity else "remove"
            clicks = abs(target_quantity - new_quantity)
            self._click_selected_button_repeatedly(product_name, action, clicks)

            if new_quantity == target_quantity:
                print(f"Количество '{product_name}' изменено: с {current_quantity} шт. на {new_quantity} шт.")
                break

    @allure.step("Уменьшить количество товара на указанное значение")
    def decrease_product_quantity(self, product_name, decrease_by):

        self._click_selected_button_repeatedly(product_name, "remove", decrease_by)

        new_quantity = self.get_product_counter_value(product_name)
        print(f"Количество '{product_name}' уменьшено на {decrease_by}. Текущее: {new_quantity} шт.")
