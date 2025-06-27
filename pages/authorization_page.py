import logging

import allure
from selenium.webdriver.common.by import By

from utils.action_with_element import ActionWithElement


class AuthorizationPage(ActionWithElement):
    LOGIN_LOCATOR = (By.XPATH, "//input[@placeholder='Логин']")
    PASSWORD_LOCATOR = (By.XPATH, "//input[@placeholder='Пароль']")
    LOGIN_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".btn")
    TITLE_AUTHORIZATION_LOCATOR = (By.CSS_SELECTOR, ".fs-2")

    @allure.step("Ввод логина.")
    def enter_login(self, login=None):
        if not login:
            logging.info("Логин не введен!")
        else:
            self.visibility_of_element_located(self.LOGIN_LOCATOR, "Логин").send_keys(login)
            logging.info(f"Введен логин: {login}")

    @allure.step("Ввод пароля")
    def enter_password(self, password=None):
        if not password:
            logging.info("Пароль не введен!")
        else:
            self.visibility_of_element_located(self.PASSWORD_LOCATOR, "Пароль").send_keys(password)
            logging.info(f"Введен пароль: {password}")

    @allure.step("Нажать кнопку 'Войти'")
    def click_the_login_button(self):
        login_button = self.visibility_of_element_located(self.LOGIN_BUTTON_LOCATOR, "Войти")
        self.click_button(login_button)
        logging.info("Нажатие кнопки 'Войти'.")

    @allure.step("Получить заголовок 'Авторизация'")
    def get_title_authorization(self):
        return self.visibility_of_element_located(self.TITLE_AUTHORIZATION_LOCATOR, "Авторизация").text
