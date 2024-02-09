from requests import Response
from utils.api import GoogleMapsApi


"""Создание, изменение и удаление новой локации"""
class TestCreatePlace:

    def test_create_new_place(self):
        
        print("Метод Post")
        result_post: Response = GoogleMapsApi.create_new_place()