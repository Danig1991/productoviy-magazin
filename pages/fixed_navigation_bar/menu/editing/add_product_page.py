import logging

import allure
from selenium.webdriver.common.by import By

from utils.action_with_element import ActionWithElement


class AddProductPage(ActionWithElement):
    NAME_LOCATOR = (By.XPATH, "//input[@placeholder='Наименование']")
    DESCRIPTION_LOCATOR = (By.XPATH, "//input[@placeholder='Описание']")
    CATEGORY_LOCATOR = (By.XPATH, "//input[@placeholder='Ожидаемая категория']")
    PRICE_LOCATOR = (By.XPATH, "//input[@placeholder='Цена']")
    IMAGE_URL_LOCATOR = (By.XPATH, "//input[@placeholder='Image Source']")
    BUTTON_BACK_TO_PRODUCTS_LOCATOR = (By.XPATH, "//button[contains(text(), 'Обратно к товарам')]")
    BUTTON_CREATE_PRODUCT_LOCATOR = (By.XPATH, "//button[contains(text(), 'Создать товар')]")

    @allure.step("Заполнение полей карточки товара")
    def add_product_data(self, name=None, description=None, category=None, price=None, image_url=None):
        fields_data = [
            (name, self.NAME_LOCATOR, "Наименование", "Наименование не введено."),
            (description, self.DESCRIPTION_LOCATOR, "Описание", "Описание не введено."),
            (category, self.CATEGORY_LOCATOR, "Ожидаемая категория", "Ожидаемая категория не введена."),
            (price, self.PRICE_LOCATOR, "Цена", "Цена не введена."),
            (image_url, self.IMAGE_URL_LOCATOR, "URL картинки", "URL картинки не введен.")
        ]
        logging.info(f"Добавлено⤵️")
        for value, locator, field_name, error_msg in fields_data:
            if value:
                self.visibility_of_element_located(locator, field_name).send_keys(value)
                logging.info(f"{field_name}: '{value}'")
            else:
                logging.info(error_msg)

    @allure.step("Нажать кнопку 'Обратно к товарам'")
    def click_button_back_to_products(self):
        button_back_to_products = self.visibility_of_element_located(
            self.BUTTON_BACK_TO_PRODUCTS_LOCATOR,
            "Обратно к товарам"
        )
        self.click_button(button_back_to_products)
        logging.info("Нажатие кнопки 'Обратно к товарам'.")

    # кнопка "Создать товар"
    def button_create_product(self):
        button_create_product = self.visibility_of_element_located(
            self.BUTTON_CREATE_PRODUCT_LOCATOR,
            "Создать товар"
        )
        return button_create_product

    @allure.step("Нажать кнопку 'Создать товар'")
    def click_button_create_product(self):
        self.click_button(self.button_create_product())
        logging.info("Нажатие кнопки 'Создать товар'.")
