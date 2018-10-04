from app import app
import json

class Token():

    @staticmethod
    def get_token():

        app.test_client().post('/api/v2/auth/sign_up', 
                data=json.dumps(dict(
                    user_name="james", 
                    user_email="james@mail.com", 
                    user_password="1234")), 
                    content_type='application/json')
        response =  app.test_client().post('/api/v2/auth/login', 
        data=json.dumps(dict(
            Username="james", 
            Password="1234")), 
            content_type='application/json')
        token = json.loads(response.data)['token']
        return token