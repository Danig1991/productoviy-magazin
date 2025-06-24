import allure
from selenium.webdriver.common.by import By

from utils.expectation import Expectation

USER_DATA_LOCATOR = (By.XPATH, "//div[@class='navbar-brand']")
BUTTON_PLACE_ORDER_LOCATOR = (By.CSS_SELECTOR, ".btn-success")
BUTTON_BACK_TO_SHOP_LOCATOR = (By.CSS_SELECTOR, ".btn-dark")
FIRST_NAME_LOCATOR = (By.XPATH, "//input[@placeholder='Имя']")
LAST_NAME_LOCATOR = (By.XPATH, "//input[@placeholder='Фамилия']")
MIDDLE_NAME_LOCATOR = (By.XPATH, "//input[@placeholder='Отчество']")
ADDRESS_LOCATOR = (By.XPATH, "//input[@placeholder='Адрес доставки']")
CARD_NUMBER_LOCATOR = (By.XPATH, "//input[@placeholder='Номер карты']")
ERROR_MESSAGE_LOCATOR = (By.CSS_SELECTOR, "div.alert.alert-danger")


class UserDataPage(Expectation):

    @allure.step("Получить заголовок 'Оформление заказа: Данные пользователя'")
    def get_title_user_data(self):
        return self.visibility_of_element_located(USER_DATA_LOCATOR, "Данные пользователя").text

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_button_place_order(self):
        button_place_order = self.visibility_of_element_located(BUTTON_PLACE_ORDER_LOCATOR, "Оформить заказ")
        self.move_to_element(button_place_order)
        button_place_order.click()
        print("На странице 'Оформление заказа: Данные пользователя' нажата кнопка 'Оформить заказ'.")

    @allure.step("Нажать кнопку 'Обратно в магазин'")
    def click_button_back_to_shop(self):
        button_back_to_shop = self.visibility_of_element_located(
            BUTTON_BACK_TO_SHOP_LOCATOR,
            "Обратно в магазин"
        )
        self.move_to_element(button_back_to_shop)
        button_back_to_shop.click()
        print("Нажата кнопка 'Обратно в магазин'.")

    @allure.step("Добавить имя")
    def add_first_name(self, first_name):
        self.visibility_of_element_located(FIRST_NAME_LOCATOR, "Имя").send_keys(first_name)
        print(f"Добавлено имя: '{first_name}'")
        return first_name

    @allure.step("Добавить фамилию")
    def add_last_name(self, last_name):
        self.visibility_of_element_located(LAST_NAME_LOCATOR, "Фамилия").send_keys(last_name)
        print(f"Добавлена фамилия: '{last_name}'")
        return last_name

    @allure.step("Добавить отчество")
    def add_middle_name(self, middle_name):
        self.visibility_of_element_located(MIDDLE_NAME_LOCATOR, "Отчество").send_keys(middle_name)
        print(f"Добавлено отчество: '{middle_name}'")
        return middle_name

    @allure.step("Добавить адрес доставки")
    def add_address(self, address):
        self.visibility_of_element_located(ADDRESS_LOCATOR, "Адрес доставки").send_keys(address)
        print(f"Добавлен адрес доставки: '{address}'")
        return address

    @allure.step("Добавить номер карты")
    def add_card_number(self, card_number):
        self.visibility_of_element_located(CARD_NUMBER_LOCATOR, "Номер карты").send_keys(card_number)
        print(f"Добавлен номер карты: '{card_number}'")
        return card_number

    @allure.step("Получить сообщение об ошибке")
    def get_error_message(self):
        return self.find_element(ERROR_MESSAGE_LOCATOR[0], ERROR_MESSAGE_LOCATOR[1])
