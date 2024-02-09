import requests

"""Список HTTP методов"""

class http_method:
    headers = {'Content-Type': 'application/json'}
    cookies = ''

    @staticmethod
    def get(url):
        result = requests.get(url, headers = http_method.headers, cookies=http_method.cookies)
        return result
    
    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers = http_method.headers, cookies=http_method.cookies)
        return result
    
    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers = http_method.headers, cookies=http_method.cookies)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers = http_method.headers, cookies=http_method.cookies)
        return result