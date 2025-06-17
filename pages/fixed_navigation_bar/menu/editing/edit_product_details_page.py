from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from utils.expectation import Expectation

PRICE_LOCATOR = (By.XPATH, "//input[@placeholder='Цена']")
BUTTON_CREATE_PRODUCT_LOCATOR = (By.CSS_SELECTOR, ".btn-success")
DESCRIPTION_LOCATOR = (By.XPATH, "//input[@placeholder='Описание']")


class EditProductDetailsPage(Expectation):

    # новая цена
    def new_price(self, new_price):
        price = self.visibility_of_element_located(PRICE_LOCATOR, "Цена")
        self.move_to_element(price)

        price.send_keys(Keys.CONTROL + "a")
        price.send_keys(Keys.DELETE)
        print("Поле \"Цена\" очищено.")

        price.send_keys(new_price)
        print(f"Установлена новая цена - \"{new_price}\"р.")

    # очистить описание
    def clear_description(self):
        description = self.visibility_of_element_located(DESCRIPTION_LOCATOR, "Описание")
        self.move_to_element(description)

        description.send_keys(Keys.CONTROL + "a")
        description.send_keys(Keys.DELETE)
        print("Поле \"Описание\" очищено.")

    # кнопка "Обновить товар"
    def button_update_product(self):
        button_update_product = self.visibility_of_element_located(
            BUTTON_CREATE_PRODUCT_LOCATOR,
            "Обновить товар"
        )
        self.move_to_element(button_update_product)
        return button_update_product

    # нажать кнопку "Обновить товар"
    def click_button_update_product(self):
        self.button_update_product().click()
        print("Нажата кнопка \"Создать товар\".")
