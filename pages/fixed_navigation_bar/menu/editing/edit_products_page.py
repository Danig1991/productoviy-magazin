from selenium.webdriver.common.by import By

from utils.expectation import Expectation

ADD_PRODUCT_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".btn-success")
EDIT_PRODUCT_BUTTON_LOCATOR = (
    By.XPATH,
    "//*[contains(text(), 'Тестовый')]"
    "/ancestor::div[contains(@class, 'store-card')]"
    "//button[contains(@class, 'btn-outline-success')]"
)
DELETE_PRODUCT_BUTTON_LOCATOR = (
    By.XPATH,
    "//*[contains(text(), 'Тестовый')]"
    "/ancestor::div[contains(@class, 'store-card')]"
    "//button[contains(@class, 'btn-outline-danger')]"
)


class EditProductsPage(Expectation):

    # нажать кнопку "Добавить товар"
    def click_add_product_button(self):
        add_product_button = self.visibility_of_element_located(
            ADD_PRODUCT_BUTTON_LOCATOR,
            "Добавить товар"
        )
        self.move_to_element(add_product_button)
        add_product_button.click()
        print("Нажата кнопка \"Добавить товар\".")

    # нажать кнопку редактирования товара(иконка карандаша)
    def click_edit_product_button(self):
        edit_product_button = self.visibility_of_element_located(
            EDIT_PRODUCT_BUTTON_LOCATOR,
            "Тестовый продукт(иконка карандаша)"
        )
        self.move_to_element(edit_product_button)
        edit_product_button.click()
        print("Редактирование товара(иконка карандаша).")

    # удалить тестовый продукт(иконка корзины)
    def remove_test_product(self):
        basket_icon = self.visibility_of_element_located(
            DELETE_PRODUCT_BUTTON_LOCATOR,
            "Тестовый продукт(иконка корзины)"
        )
        self.move_to_element(basket_icon)
        basket_icon.click()
        print("Тестовый продукт удален.")
