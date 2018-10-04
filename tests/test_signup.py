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
 
    def test_duplicate_user(self):
        """tests for signing up a user twice"""
        self.app.post('/api/v2/auth/sign_up', 
         data=json.dumps(dict(
            user_name="deal", 
            user_email="deal@mail.com", 
            user_password="1234")), 
        content_type='application/json')
        response =  self.app.post('/api/v2/auth/sign_up', 
         data=json.dumps(dict(
            user_name="deal", 
            user_email="deal@mail.com", 
            user_password="1234")), 
        content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.content_type, 'application/json')

    def test_wrong_email_format(self):
        """tests for signing up a user with wrong email format"""
        response =  self.app.post('/api/v2/auth/sign_up', 
         data=json.dumps(dict(
            user_name="james1", 
            user_email="james1mailcom", 
            user_password="1234")), 
        content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.content_type, 'application/json')

    def test_empty_username_field(self):
        """tests for signing up a user with empty username field"""
        response =  self.app.post('/api/v2/auth/sign_up', 
         data=json.dumps(dict(
            user_name=" ", 
            user_email="james@mail.com", 
            user_password=" ")), 
        content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.content_type, 'application/json') 

    def test_empty_email_field(self):
        """tests for signing up a user with empty email field"""
        response =  self.app.post('/api/v2/auth/sign_up', 
         data=json.dumps(dict(
            user_name="james", 
            user_email=" ", 
            user_password="1234")), 
        content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.content_type, 'application/json')

    def test_empty_password_field(self):
        """tests for signing up a user with empty password field"""
        response =  self.app.post('/api/v2/auth/sign_up', 
         data=json.dumps(dict(
            user_name="james", 
            user_email="james@mail.com", 
            user_password=" ")), 
        content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.content_type, 'application/json')            
         

    def test_sign_up(self):
        """tests for signing up a user"""
        response =  self.app.post('/api/v2/auth/sign_up', 
        data=json.dumps({
            "user_name": "opio",
            "user_email": "opio@mail.com",
            "user_password": "sean"
            }), 
            content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')


    def tearDown(self):
        db = Database()
        db.drop_tables()

if __name__ == '__main__':
    unittest.main()