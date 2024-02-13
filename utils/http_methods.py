import requests
import allure

"""Список HTTP методов"""


class http_method:
    headers = {"Content-Type": "application/json"}
    cookies = ""

    @staticmethod
    def get(url):
        with allure.step("Get"):
            result = requests.get(
                url, headers=http_method.headers, cookies=http_method.cookies
            )
            return result

    @staticmethod
    def post(url, body):
        with allure.step("Post"):
            result = requests.post(
                url, json=body, headers=http_method.headers, cookies=http_method.cookies
            )
            return result

    @staticmethod
    def put(url, body):
        with allure.step("Put"):
            result = requests.put(
                url, json=body, headers=http_method.headers, cookies=http_method.cookies
            )
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("Delete"):
            result = requests.delete(
                url, json=body, headers=http_method.headers, cookies=http_method.cookies
            )
            return result
