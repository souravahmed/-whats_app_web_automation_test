from Pages.user_api import UserApi

class Test_User_Api:
    
    def test_success_user_sign_up(self):
        user_api = UserApi("register")
        payload = {"email": "janet.weaver@reqres.in", "password": "1234"}
        result = user_api.sign_up_user(payload)
        response = result["response"]
        is_success = True if response["token"] else False
        assert is_success
        
    def test_invalid_sign_up(self):
        user_api = UserApi("register")
        payload = {"email": "janet.weaver@reqres.in"}
        result = user_api.sign_up_user(payload)
        assert result["status_code"] == 400
        
    def test_success_sign_in(self):
        user_api = UserApi("login")
        payload = {"email": "janet.weaver@reqres.in", "password": "1234"}
        result = user_api.sign_in_user(payload)
        response = result["response"]
        is_success = True if response["token"] else False
        assert is_success
        
    def test_invalid_sign_in(self):
        user_api = UserApi("login")
        payload = {"email": "janet.weaver@reqres.in"}
        result = user_api.sign_in_user(payload)
        assert result["status_code"] == 400
        
    
    def test_list_users(self):
        user_api = UserApi("users?page=2")
        result = user_api.get_user_list()
        response = result["response"]
        assert True if response["data"] else False
        
    
    def test_single_user(self):
        user_api = UserApi("users/2")
        result = user_api.get_single_user()
        response = result["response"]
        assert True if response["data"] else False
        
    def test_success_post_user(self):
        user_api = UserApi("users")
        payload = {"name": "morpheus", "job": "leader"}
        result = user_api.post_user(payload)
        response = result["response"]
        assert True if response["id"] else False
        
    def test_success_update_user(self):
        user_api = UserApi("users/2")
        payload = {"name": "morpheus", "job": "zoin resident"}
        result = user_api.update_user(payload)
        response = result["response"]
        assert True if response["updatedAt"] else False                 