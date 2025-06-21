import logging


class Double:
    # дублирование сообщения
    @staticmethod
    def print_and_log(message):
        print(message)
        logging.info(message)
