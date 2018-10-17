import unittest
import json
from app import app
from app.models import Database
from app.models import Users, Orders, Menu


def test_promote_user():
    """tests for promote up a user"""
    test_app = app.test_client()
    response =  test_app.put('/api/v2/users/20')
    assert response.status_code == 201
    assert response.content_type == 'application/json' 

