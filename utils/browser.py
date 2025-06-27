import logging

import allure
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class Browser:

    def __init__(self, browser_type="chrome"):
        self.browser_type = browser_type.lower()
        self.driver = self.__init_driver()

    # выбор типа браузера
    def __init_driver(self):
        if self.browser_type == "chrome":
            return self.__chrome()
        elif self.browser_type == "firefox":
            return self.__firefox()
        elif self.browser_type == "edge":
            return self.__edge()
        else:
            raise ValueError(f"Неподдерживаемый браузер: {self.browser_type}")

    # браузер Chrome
    @staticmethod
    def __chrome():
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--log-level=3")  # Уровень логирования: 0 = INFO, 3 = FATAL
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        return webdriver.Chrome(options=options, service=service)

    # браузер Firefox
    @staticmethod
    def __firefox():
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service)

    # браузер Edge
    @staticmethod
    def __edge():
        service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service)

    @allure.step("Открыть браузер/развернуть окно на весь экран")
    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        logging.info(f"Браузер {self.browser_type} открыт ({url}).")

    @allure.step("Закрыть браузер")
    def quit(self):
        self.driver.quit()
        logging.info(f"Браузер {self.browser_type} закрыт.")
