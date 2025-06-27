import logging

import allure
from selenium.webdriver.common.by import By

from utils.action_with_element import ActionWithElement


class UserDataPage(ActionWithElement):
    USER_DATA_LOCATOR = (By.XPATH, "//div[@class='navbar-brand']")
    BUTTON_PLACE_ORDER_LOCATOR = (By.CSS_SELECTOR, ".btn-success")
    BUTTON_BACK_TO_SHOP_LOCATOR = (By.CSS_SELECTOR, ".btn-dark")
    FIRST_NAME_LOCATOR = (By.XPATH, "//input[@placeholder='Имя']")
    LAST_NAME_LOCATOR = (By.XPATH, "//input[@placeholder='Фамилия']")
    MIDDLE_NAME_LOCATOR = (By.XPATH, "//input[@placeholder='Отчество']")
    ADDRESS_LOCATOR = (By.XPATH, "//input[@placeholder='Адрес доставки']")
    CARD_NUMBER_LOCATOR = (By.XPATH, "//input[@placeholder='Номер карты']")
    ERROR_MESSAGE_LOCATOR = (By.CSS_SELECTOR, "div.alert.alert-danger")

    @allure.step("Получить заголовок 'Оформление заказа: Данные пользователя'")
    def get_title_user_data(self):
        return self.visibility_of_element_located(self.USER_DATA_LOCATOR, "Данные пользователя").text

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_button_place_order(self):
        button_place_order = self.visibility_of_element_located(
            self.BUTTON_PLACE_ORDER_LOCATOR,
            "Оформить заказ"
        )
        self.click_button(button_place_order)
        logging.info("Нажатие кнопки 'Оформить заказ'. "
                     "Переход на страницу 'Оформление заказа: Подтверждение заказа'.")

    @allure.step("Нажать кнопку 'Обратно в магазин'")
    def click_button_back_to_shop(self):
        button_back_to_shop = self.visibility_of_element_located(
            self.BUTTON_BACK_TO_SHOP_LOCATOR,
            "Обратно в магазин"
        )
        self.click_button(button_back_to_shop)
        logging.info("Нажатие кнопки 'Обратно в магазин'.")

    @allure.step("Заполнение полей данными пользователя")
    def add_user_data(self, first_name=None, last_name=None, middle_name=None, address=None, card_number=None):
        fields_data = [
            (first_name, self.FIRST_NAME_LOCATOR, "Имя", "Имя не введено."),
            (last_name, self.LAST_NAME_LOCATOR, "Фамилия", "Фамилия не введена."),
            (middle_name, self.MIDDLE_NAME_LOCATOR, "Отчество", "Отчество не введено."),
            (address, self.ADDRESS_LOCATOR, "Адрес доставки", "Адрес не введен."),
            (card_number, self.CARD_NUMBER_LOCATOR, "Номер карты", "Номер карты не введен.")
        ]
        logging.info(f"Добавлено⤵️")
        for value, locator, field_name, error_msg in fields_data:
            if value:
                self.visibility_of_element_located(locator, field_name).send_keys(value)
                logging.info(f"{field_name}: '{value}'")
            else:
                logging.info(error_msg)

    @allure.step("Получить сообщение об ошибке")
    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE_LOCATOR[0], self.ERROR_MESSAGE_LOCATOR[1])
