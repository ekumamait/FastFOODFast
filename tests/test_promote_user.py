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

    def test_sign_up(self):
        """tests for promote up a user"""
        response =  self.app.post('/api/v2/users/20')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json') 
    
    def tearDown(self):
        db = Database()
        db.drop_tables()

if __name__ == '__main__':
    unittest.main()