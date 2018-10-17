import unittest
import json
from app import app
from app.models import Database
# from app.models import Users
from tests.token import Token

# class My_TestClass(unittest.TestCase):

    # def __init__(self, app, vim):
    #     test_app = app.test_client() 

    # def setUp():
    #     dbcon = Database()
    #     self.dbcon.table()
    # # self.app = app.test_client()

def test_wrong_password():
    """tests for logging in a user with wrong password"""
    # import pdb;pdb.set_trace()
    print(app)
    test_app = app.test_client()
    test_app.post('/api/v2/auth/sign_up', 
        data=json.dumps(dict(
        user_name="james",
        user_email="james@mail.com", 
        user_password="1234")), 
    content_type='application/json')
    response =  test_app.post('/api/v2/auth/login', 
    data=json.dumps(dict(
        Username="james", 
        Password="12")), 
        content_type='application/json')

    assert response.status_code == 401
    assert response.content_type == 'application/json'

def test_empty_username_fields():
    """tests for logging in a user with empty username fields"""
    test_app = app.test_client()
    test_app.post('/api/v2/auth/sign_up', 
        data=json.dumps(dict(
        user_name="james", 
        user_email="james@mail.com",
        user_password="1234")), 
    content_type='application/json')
    response =  test_app.post('/api/v2/auth/login', 
    data=json.dumps(dict(
        Username=" ", 
        Password="12")), 
        content_type='application/json')

    assert response.status_code == 401
    assert response.content_type == 'application/json'

def test_empty_password_fields():
    """tests for logging in a user with empty password fields"""
    test_app = app.test_client()
    test_app.post('/api/v2/auth/sign_up', 
        data=json.dumps(dict(
        user_name="james", 
        user_email="james@mail.com",
        user_password="1234")), 
    content_type='application/json')
    response =  test_app.post('/api/v2/auth/login', 
    data=json.dumps(dict(
        Username="james", 
        Password=" ")), 
        content_type='application/json')
    print(response)
    assert response.status_code == 401
    assert response.content_type == 'application/json' 

def test_login():
    """tests for logging in a user"""
    test_app = app.test_client()
    test_app.post('/api/v2/auth/sign_up', 
    data=json.dumps(dict(
        user_name="james", 
        user_email="james@mail.com", 
        user_password="1234")), 
        content_type='application/json')
    response =  test_app.post('/api/v2/auth/login', 
    data=json.dumps(dict(
        Username="james", 
        Password="1234")), 
        content_type='application/json')
    message = json.loads(response.data)['message']
    assert response.status_code == 200
    assert message == 'succefully' 
                

    # def tearDown(self):
    #     db = Database()
    #     db.drop_tables()

