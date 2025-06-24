import allure
from selenium.webdriver.common.by import By

from utils.expectation import Expectation

ORDER_CONFIRMATION_LOCATOR = (By.XPATH, "//div[@class='navbar-brand']")
CUSTOMER_DETAILS_LOCATOR = (By.XPATH, "//div[contains(text(), 'Данные о клиенте')]/following-sibling::div[1]/div")
DELIVERY_LOCATOR = (By.XPATH, "//div[contains(text(), 'Доставка')]/following-sibling::div[1]/div")
PAYMENT_LOCATOR = (By.XPATH, "//div[contains(text(), 'Оплата')]/following-sibling::div[1]/div")
PRICE_LOCATOR = (By.XPATH, "//div[contains(text(), 'Стоимость')]/following-sibling::div[1]/div")
COMPLETE_ORDER_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".btn-success")


class OrderConfirmationPage(Expectation):

    @allure.step("Получить заголовок 'Оформление заказа: Подтверждение заказа'")
    def get_title_order_confirmation(self):
        return self.visibility_of_element_located(ORDER_CONFIRMATION_LOCATOR, "Подтверждение заказа").text

    @allure.step("Получить данные для подтверждения заказа")
    def get_order_confirmation_data(self):
        data = {}

        # данные о клиенте
        customer_details = self.visibility_of_all_elements_located(CUSTOMER_DETAILS_LOCATOR, "Данные о клиенте")
        data["Имя"] = customer_details[0].text.split(":")[1].strip()
        data["Фамилия"] = customer_details[1].text.split(":")[1].strip()
        data["Отчество"] = customer_details[2].text.split(":")[1].strip()

        # доставка
        delivery = self.visibility_of_all_elements_located(DELIVERY_LOCATOR, "Доставка")
        data["Адрес доставки"] = delivery[0].text.split(":")[1].strip()

        # оплата
        payment = self.visibility_of_all_elements_located(PAYMENT_LOCATOR, "Оплата")
        data["Номер карты"] = payment[1].text.split(":")[1].strip()

        # стоимость
        price = self.visibility_of_all_elements_located(PRICE_LOCATOR, "Стоимость")
        data["Итоговая стоимость"] = int(price[1].text.split(":")[1].replace("₽", "").strip())

        return data

    @allure.step("Нажать кнопку 'Завершить заказ'")
    def click_complete_order_button(self):
        complete_order_button = self.visibility_of_element_located(
            COMPLETE_ORDER_BUTTON_LOCATOR,
            "Завершить заказ"
        )
        self.move_to_element(complete_order_button)
        complete_order_button.click()
        print("На странице для подтверждения заказа нажата кнопка 'Завершить заказ'.")
