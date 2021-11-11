import requests
import json
from .config import ConstData
class BaseApi(object):
    """
    this Base api class is serving basic attributes for every single api page inherited from this class
    
    """
    
    def __init__(self, url):
        self.url = ConstData.BASE_API_URL + url
        
    
    def get_request(self):
        response = requests.get(self.url)    
        return self.__get_response(response)
    
    def post_request(self, payload):
        response = requests.post(self.url, data=json.dumps(payload), headers= {'Accept': 'application/json','Content-Type': 'application/json'})
        return self.__get_response(response)
    
    def put_request(self, payload):
        response = requests.put(self.url, data=json.dumps(payload), headers= {'Accept': 'application/json','Content-Type': 'application/json'})
        return self.__get_response(response)
    
    def __get_response(self, response):
        return {"status_code": response.status_code, "response" :  response.json()}