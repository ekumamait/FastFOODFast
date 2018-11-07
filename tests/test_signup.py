import unittest
import json
from app import app
from app.models import Database
from app.models import Users


def test_duplicate_user():
    """tests for signing up a user twice"""
    test_app = app.test_client()
    test_app.post('/api/v2/auth/sign_up', 
        data=json.dumps(dict(
        user_name="deal", 
        user_email="deal@mail.com", 
        user_password="1234")), 
    content_type='application/json')
    response =  test_app.post('/api/v2/auth/sign_up', 
        data=json.dumps(dict(
        user_name="deal", 
        user_email="deal@mail.com", 
        user_password="1234")), 
    content_type='application/json')

    assert response.status_code == 401
    assert response.content_type == 'application/json'

def test_wrong_email_format():
    """tests for signing up a user with wrong email format"""
    test_app = app.test_client()
    response =  test_app.post('/api/v2/auth/sign_up', 
        data=json.dumps(dict(
        user_name="james1", 
        user_email="james1mailcom", 
        user_password="1234")), 
    content_type='application/json')

    assert response.status_code == 401
    assert response.content_type == 'application/json'

def test_empty_username_field():
    """tests for signing up a user with empty username field"""
    test_app = app.test_client()
    response =  test_app.post('/api/v2/auth/sign_up', 
        data=json.dumps(dict(
        user_name=" ", 
        user_email="james@mail.com", 
        user_password=" ")), 
    content_type='application/json')

    assert response.status_code == 401
    assert response.content_type == 'application/json' 

def test_empty_email_field():
    """tests for signing up a user with empty email field"""
    test_app = app.test_client()
    response =  test_app.post('/api/v2/auth/sign_up', 
        data=json.dumps(dict(
        user_name="james", 
        user_email=" ", 
        user_password="1234")), 
    content_type='application/json')

    assert response.status_code == 401
    assert response.content_type == 'application/json'

def test_empty_password_field():
    """tests for signing up a user with empty password field"""
    test_app = app.test_client()
    response =  test_app.post('/api/v2/auth/sign_up', 
        data=json.dumps(dict(
        user_name="james", 
        user_email="james@mail.com", 
        user_password=" ")), 
    content_type='application/json')

    assert response.status_code == 401
    assert response.content_type == 'application/json'            
        

def test_sign_up():
    """tests for signing up a user"""
    test_app = app.test_client()
    response =  test_app.post('/api/v2/auth/sign_up', 
    data=json.dumps({
        "user_name": "avenger",
        "user_email": "avenger@mail.com",
        "user_password": "person"
        }), 
        content_type='application/json')
    assert response.status_code == 201
    assert response.content_type == 'application/json'


