import requests

class APIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {'Authorization': f'Bearer {api_key}'}

    def get_data(self, endpoint):
        response = requests.get(f'{self.base_url}/{endpoint}', headers=self.headers)
        return response

    def post_data(self, endpoint, data):
        response = requests.post(f'{self.base_url}/{endpoint}', json=data, headers=self.headers)
        return response

    def put_data(self, endpoint, data):
        response = requests.put(f'{self.base_url}/{endpoint}', json=data, headers=self.headers)
        return response

    def delete_data(self, endpoint):
        response = requests.delete(f'{self.base_url}/{endpoint}', headers=self.headers)
        return response
