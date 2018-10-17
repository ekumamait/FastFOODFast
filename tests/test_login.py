import unittest
import json
from app import app
from app.models import Database
from tests.token import Token


def test_wrong_password():
    """tests for logging in a user with wrong password"""
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

