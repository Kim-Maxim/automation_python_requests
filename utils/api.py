from utils.http_methods import http_method


"""Методы для тестирования Google Maps Api"""

base_url = 'https://rahulshettyacademy.com' #Базовал URL
key = "?key=qaclick123" #Параметр для всех запросов

class GoogleMapsApi():

    """Метод для создания новой локации"""
    @staticmethod
    def create_new_place():
        json_for_create_location = {
            "location": {
            "lat": -38.382554,
            "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
            "shoe park",
            "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resorse = "/maps/api/place/add/json" #Ресурс метода post
        post_url = base_url + post_resorse + key
        print(post_url)
        result_post = http_method.post(post_url, body=json_for_create_location)
        print(result_post.text)
        return result_post