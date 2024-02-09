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
    
    """Метод для проверки новой локации"""

    @staticmethod
    def get_new_place(place_id):

        get_resourse = "/maps/api/place/get/json" #Ресурс метода get
        get_url = base_url + get_resourse + key + "&place_id=" + place_id 
        print(get_url)
        result_get = http_method.get(get_url)
        print(result_get.text)
        return result_get
    
    """Метод для изменения новой локации"""

    @staticmethod
    def put_new_place(place_id):

        put_resourse = "/maps/api/place/update/json"
        put_url = base_url + put_resourse + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address":"100 Lenina street, RU", 
            "key":"qaclick123" 
        }
        result_put = http_method.put(put_url, body=json_for_update_new_location)
        print(result_put.text)
        return result_put
