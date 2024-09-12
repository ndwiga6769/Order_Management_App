import unittest
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    
    def test_get_customers(self):
        result = self.app.get('/customers')
        self.assertEqual(result.status_code, 200)

    
    def test_create_customer(self):
        result = self.app.post('/customers', json={"name": "John Doe", "code": "C001"})
        self.assertEqual(result.status_code, 201)

    
    def test_create_order(self):
        result = self.app.post('/orders', json={"customer_id": 1, "item": "Item1", "amount": 100, "time": "2024-09-12"})
        self.assertEqual(result.status_code, 201)

if __name__ == '__main__':
    unittest.main()
