import unittest
import json
from app import app
from app.models import Database
from app.models import Users
from tests.token import Token

class My_TestClass(unittest.TestCase):

    def setUp(self):

        self.dbcon = Database()
        self.dbcon.table()
        self.app = app.test_client()

    def test_wrong_password(self):
        """tests for logging in a user with wrong password"""
        self.app.post('/api/v2/auth/sign_up', 
         data=json.dumps(dict(
            user_name="james",
            user_email="james@mail.com", 
            user_password="1234")), 
        content_type='application/json')
        response =  self.app.post('/api/v2/auth/login', 
        data=json.dumps(dict(
            Username="james", 
            Password="12")), 
            content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.content_type, 'application/json')

    def test_empty_username_fields(self):
        """tests for logging in a user with empty username fields"""
        self.app.post('/api/v2/auth/sign_up', 
         data=json.dumps(dict(
            user_name="james", 
            user_email="james@mail.com",
            user_password="1234")), 
        content_type='application/json')
        response =  self.app.post('/api/v2/auth/login', 
        data=json.dumps(dict(
            Username=" ", 
            Password="12")), 
            content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.content_type, 'application/json')

    def test_empty_password_fields(self):
        """tests for logging in a user with empty password fields"""
        self.app.post('/api/v2/auth/sign_up', 
         data=json.dumps(dict(
            user_name="james", 
            user_email="james@mail.com",
            user_password="1234")), 
        content_type='application/json')
        response =  self.app.post('/api/v2/auth/login', 
        data=json.dumps(dict(
            Username="james", 
            Password=" ")), 
            content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.content_type, 'application/json')  

    def test_login(self):
        """tests for logging in a user"""
        self.app.post('/api/v2/auth/sign_up', 
        data=json.dumps(dict(
            user_name="james", 
            user_email="james@mail.com", 
            user_password="1234")), 
            content_type='application/json')
        response =  self.app.post('/api/v2/auth/login', 
        data=json.dumps(dict(
            Username="james", 
            Password="1234")), 
            content_type='application/json')
        message = json.loads(response.data)['message']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(message, 'succefully') 
                

    def tearDown(self):
        db = Database()
        db.drop_tables()

if __name__ == '__main__':
    unittest.main()