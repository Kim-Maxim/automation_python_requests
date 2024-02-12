import json

from requests import Response


"""Методы для проверки наших запросов"""


class Checking():

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        
        assert response.status_code == status_code
        if response.status_code == status_code:
            print("Успешно!!! Статус код = " + str(response.status_code))
        else:
            print("Провал!!! Статус код = " + str(response.status_code))

    """Метод для проверки налчия полей в ответ запроса"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")