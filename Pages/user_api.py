from .base_api import BaseApi

class UserApi(BaseApi):
    
    def __init__(self, url):
        super().__init__(url)
        
        
    def sign_up_user(self, payload):
        return self.post_request(payload)
    
    def sign_in_user(self, payload):
        return self.post_request(payload)
    
    def get_user_list(self):
        return self.get_request()
    
    def get_single_user(self):
        return self.get_request()
    
    def post_user(self, payload):
        return self.post_request(payload)
    
    def update_user(self, payload):
        return self.put_request(payload)   