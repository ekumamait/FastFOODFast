import unittest
import json
from app.routes import app
from app.models import Orders


class My_TestClass(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.order = Orders()

    def test_index_page_response(self):
        """tests for index page """
        response = self.app.get('/')
        self.assertTrue(response, 'Welcome to FastFOODFast')

    def test_get_all_orders(self):
        """tests for getting all orders in the list"""
        response = self.app.get('/api/v1/orders')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_getting_single_order(self):
        """ tests for getting a single order """
        resp = self.app.get('/api/v1/orders/1')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_add_an_order(self):
        """ tests for adding an order """
        resp = self.app.post('/api/v1/orders',
                data=json.dumps(dict(meal="kungpao",
                location="kololo", quantity="10")),
                content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_edit_order(self):
        """ tests for editing an order """
        resp = self.app.put('/api/v1/orders/1',
                data=json.dumps(dict(meal="chicken biryani",
                location="kololo", quantity="10")),
                content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_empty_field_in_order(self):
        """ tests for adding an order empty field"""
        resp = self.app.post('/api/v1/orders',
                data=json.dumps(dict(meal="kungpao",
                location="kololo", quantity=" ")),
                content_type='application/json')
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.content_type, 'application/json')

    def test_wrong_id_provided_when_getting_single_order(self):
        """ test wrong id provided when_getting_single_order"""
        resp = self.app.get('/api/v1/orders/{}',
                data=json.dumps(dict(meal="matooke",
                location="kololo", quantity="10")),
                content_type='application/json')
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(resp.content_type, 'application/json')

    def test_wrong_id_provided_when_updating_order(self):
        """ tests for updating an order with missing"""
        resp = self.app.put('/api/v1/orders/{}',
                data=json.dumps(dict(meal="matooke",
                location="kololo", quantity="10")),
                content_type='application/json')
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(resp.content_type, 'application/json')

    def test_wrong_method_provided_when_getting_order(self):
        """ tests for getting an order with wrong methods """
        resp = self.app.put('/api/v1/orders')
        self.assertEqual(resp.status_code, 405)
        self.assertEqual(resp.content_type, 'application/json')

    def test_wrong_method_provided_when_putting_order(self):
        """ tests for getting an order with wrong methods """
        resp = self.app.delete('/api/v1/orders/1')
        self.assertEqual(resp.status_code, 405)
        self.assertEqual(resp.content_type, 'application/json')


if __name__ == '__main__':
    unittest.main()
