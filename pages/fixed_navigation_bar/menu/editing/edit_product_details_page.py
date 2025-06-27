import logging

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from utils.action_with_element import ActionWithElement


class EditProductDetailsPage(ActionWithElement):
    PRICE_LOCATOR = (By.XPATH, "//input[@placeholder='Цена']")
    BUTTON_CREATE_PRODUCT_LOCATOR = (By.CSS_SELECTOR, ".btn-success")
    DESCRIPTION_LOCATOR = (By.XPATH, "//input[@placeholder='Описание']")

    @allure.step("Установить новую цену")
    def new_price(self, new_price):
        price = self.visibility_of_element_located(self.PRICE_LOCATOR, "Цена")
        self.move_to_element(price)

        price.send_keys(Keys.CONTROL + "a")
        price.send_keys(Keys.DELETE)
        logging.info("Поле 'Цена' очищено.")

        price.send_keys(new_price)
        logging.info(f"Установлена новая цена - '{new_price}'р.")

    @allure.step("Очистить описание")
    def clear_description(self):
        description = self.visibility_of_element_located(self.DESCRIPTION_LOCATOR, "Описание")
        self.move_to_element(description)

        description.send_keys(Keys.CONTROL + "a")
        description.send_keys(Keys.DELETE)
        logging.info("Поле 'Описание' очищено.")

    # кнопка "Обновить товар"
    def button_update_product(self):
        button_update_product = self.visibility_of_element_located(
            self.BUTTON_CREATE_PRODUCT_LOCATOR,
            "Обновить товар"
        )
        return button_update_product

    @allure.step("Нажать кнопку 'Обновить товар'")
    def click_button_update_product(self):
        self.click_button(self.button_update_product())
        logging.info("Нажатие кнопки 'Обновить товар'.")
