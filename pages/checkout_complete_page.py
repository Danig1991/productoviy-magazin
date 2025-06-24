import allure
from selenium.webdriver.common.by import By

from utils.expectation import Expectation

TITLE_ORDER_SUCCESSFULLY_CREATED_LOCATOR = (By.CSS_SELECTOR, "div.navbar-brand")


class CheckoutCompletePage(Expectation):

    @allure.step("Получить заголовок 'Оформление заказа: Заказ успешно создан'")
    def get_title_order_successfully_created(self):
        return self.visibility_of_element_located(
            TITLE_ORDER_SUCCESSFULLY_CREATED_LOCATOR,
            "Оформление заказа: Заказ успешно создан"
        ).text
