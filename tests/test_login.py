import unittest
import json
from app import app
from app.models import Database
from app.models import Users, Orders, Menu

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
            username="james", 
            password="12")), 
            content_type='application/json')

        self.assertEqual(response.status_code, 400)
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
            username=" ", 
            password="12")), 
            content_type='application/json')

        self.assertEqual(response.status_code, 400)
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
            username="james", 
            password=" ")), 
            content_type='application/json')

        self.assertEqual(response.status_code, 400)
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
            username="james", 
            password="1234")), 
            content_type='application/json')
        token = json.loads(response.data.decode())["token"]
        self.assertEqual(response.status_code, 200)
        self.assertIn(token, str(response.data)) 
                

    def tearDown(self):
        db = Database()
        db.drop_tables()

if __name__ == '__main__':
    unittest.main()