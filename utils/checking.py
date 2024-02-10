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

