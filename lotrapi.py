import requests


class LotrAPI:
    API_KEY = "giwMdZJEMM2AzGK5Rdiz"
    LOTR_API_ENDPOINT = "https://the-one-api.dev/v2"

    def __init__(self):
        self.headers = headers = {
            'Authorization': f'Bearer {self.API_KEY}',
            'Content-Type': 'application/json'
        }

    def get_data(self, data_type):
        url = f"{self.LOTR_API_ENDPOINT}/{data_type}"
        try:
            response = requests.get(url=url, headers=self.headers)
            response.raise_for_status()
            data = response.json().get('docs', [])  # Get 'docs' if present
            return data
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def get_data1(self, data_type):
        url = f"{self.LOTR_API_ENDPOINT}/{data_type}"
        params = {
            "offset": 3
        }
        try:
            response = requests.get(url=url, params=params, headers=self.headers)
            response.raise_for_status()
            data = response.json()  # Get 'docs' if present
            print(data)
            return data
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
