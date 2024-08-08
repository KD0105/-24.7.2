import unittest
from api import APIClient

class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.client = APIClient('https://api.example.com', 'fake_api_key')

    def test_get_data_success(self):
        response = self.client.get_data('endpoint')
        self.assertEqual(response.status_code, 200)

    def test_post_data_success(self):
        data = {'key': 'value'}
        response = self.client.post_data('endpoint', data)
        self.assertEqual(response.status_code, 200)

    def test_put_data_success(self):
        data = {'key': 'value'}
        response = self.client.put_data('endpoint', data)
        self.assertEqual(response.status_code, 200)

    def test_delete_data_success(self):
        response = self.client.delete_data('endpoint')
        self.assertEqual(response.status_code, 200)

    def test_get_data_invalid_endpoint(self):
        response = self.client.get_data('invalid_endpoint')
        self.assertEqual(response.status_code, 404)

    def test_post_data_invalid_data(self):
        data = {'invalid_key': 'value'}
        response = self.client.post_data('endpoint', data)
        self.assertEqual(response.status_code, 400)

    def test_put_data_invalid_data(self):
        data = {'invalid_key': 'value'}
        response = self.client.put_data('endpoint', data)
        self.assertEqual(response.status_code, 400)

    def test_delete_data_invalid_endpoint(self):
        response = self.client.delete_data('invalid_endpoint')
        self.assertEqual(response.status_code, 404)

    def test_get_data_missing_auth(self):
        self.client.headers = {}
        response = self.client.get_data('endpoint')
        self.assertEqual(response.status_code, 401)

    def test_post_data_missing_auth(self):
        self.client.headers = {}
        data = {'key': 'value'}
        response = self.client.post_data('endpoint', data)
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
