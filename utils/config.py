from faker import Faker


# конфигурации

class Url:
    # базовый URL
    BASE_URL = "http://91.197.96.80/"


class AuthConfig:
    # учетная запись покупателя
    SHOPPER_LOGIN = "покупатель4"
    SHOPPER_PASSWORD = "покупатель4"

    # учетная запись администратора ADMIN
    ADMIN_LOGIN = "admin"
    ADMIN_PASSWORD = "admin"


class ProductData:
    # значения для нового продукта
    @staticmethod
    def get_product_data():
        return {
            "Наименование": "Тестовый Пирожок Вишневый",
            "Описание": "Обжаренный во фритюре пирожок со сладкой начинкой из вишни 80 г",
            "Ожидаемая категория": "Пирожок",
            "Цена": 65,
            "Новая цена": 70,
            "URL картинки": "https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/"
                            "521573545-pirogok-vishnevyj-600x600.webp"
        }


class ProductConfig:
    # данные для действия с продуктом
    PRODUCT_NAME = "Бургер с курицей"
    QUANTITY_1 = 1
    QUANTITY_2 = 2
    QUANTITY_3 = 3
    QUANTITY_105 = 105
    QUANTITY_505 = 505


class FilterConfig:
    # значения для выпадающего меню
    SORT_BY_PRICE_LOW_TO_HIGH = "Цена: Сначала подешевле"
    SORT_BY_PRICE_HIGH_TO_LOW = "Цена: Сначала подороже"
    SORT_BY_NAME_A_TO_Z = "Наименование: от A до Я"
    SORT_BY_NAME_Z_TO_A = "Наименование: от Я до А"

    # значения для фильтра: категории
    BURGER = "Бургер"
    PIE = "Пирожок"
    ROLL = "Ролл"
    SANDWICH = "Сэндвич"

    # значения для фильтра: цена
    MIN_PRICE = 100
    MAX_PRICE = 150


class UserData:
    # генерирование данных пользователя
    def __init__(self):
        self.__faker = Faker("ru_Ru")

    def get_user_data(self):
        return {
            "Имя": self.__faker.first_name_male(),
            "Фамилия": self.__faker.last_name_male(),
            "Отчество": self.__faker.middle_name_male(),
            "Адрес доставки": self.__faker.street_address(),
            "Номер карты": " ".join(
                [str(self.__faker.random_number(digits=4, fix_len=True)) for _ in range(4)]
            ),
            "Нечисловой номер карты": " ".join(
                [self.__faker.password(length=4, digits=False, upper_case=False) for _ in range(4)]
            )
        }
