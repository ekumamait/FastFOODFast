import unittest
import json
from api.routes import app

class My_TestClass(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_page_response(self):
        """tests for index page """
        response = self.app.get('/')
        self.assertTrue(response, 'Welcome to FastFOODFast')
  
    def test_get_all_orders(self):
        """tests for getting all orders in the list"""
        response =  self.app.get('/api/v1/orders')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_get_single_order(self):
        """ tests for getting a single order """
        pos = self.app.post('/api/v1/orders', data=json.dumps(dict(meal="kungpao", location="kololo", quantity="10")), content_type='application/json')
        self.assertEqual(pos.status_code, 200)
        resp = self.app.get('/api/v1/orders/1')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_add_an_order(self):
        """ tests for adding an order """
        resp = self.app.post('/api/v1/orders', data=json.dumps(dict(meal="kungpao", location="kololo", quantity="10")), content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_edit_order(self):
        """ tests for editing an order """
        pos = self.app.post('/api/v1/orders', data=json.dumps(dict(meal="kungpao", location="kololo", quantity="10")), content_type='application/json')
        self.assertEqual(pos.status_code, 200)
        resp = self.app.put('/api/v1/orders/1', data=json.dumps(dict(meal="chicken biryani", location="kololo", quantity="10")), content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

if __name__ == '__main__':
    unittest.main()