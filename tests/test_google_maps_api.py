from requests import Response
from utils.api import GoogleMapsApi


"""Создание, изменение и удаление новой локации"""
class TestCreatePlace:

    def test_create_new_place(self):
        
        print("Метод Post")
        result_post: Response = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("Метод Get-Post")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        
        print("Метод Put")
        result_put: Response = GoogleMapsApi.put_new_place(place_id)

        print("Метод Get-Put")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)