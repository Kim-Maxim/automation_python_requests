from requests import Response
from utils.api import GoogleMapsApi
from utils.checking import Checking

"""Создание, изменение и удаление новой локации"""
class TestCreatePlace:

    def test_create_new_place(self):
        
        print("Метод Post")
        result_post: Response = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)

        print("Метод Get-Post")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        
        print("Метод Put")
        result_put: Response = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)

        print("Метод Get-Put")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)

        print("Метод Delete")
        result_delete: Response = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)

        print("Метод Get-Delete")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)