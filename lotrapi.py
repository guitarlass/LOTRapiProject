import requests
import random
from pprint import pprint


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

    def get_random_character_data(self, data_type):
        url = f"{self.LOTR_API_ENDPOINT}/{data_type}"
        offset = random.randint(1, 933)
        params = {
            # "page": 2,
            "limit": 10,
            "offset": offset
        }
        try:
            response = requests.get(url=url, params=params, headers=self.headers)
            response.raise_for_status()
            data = response.json().get('docs', [])  # Get 'docs' if present
            # print(data)
            return data
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def fetch_quotes_for_character(self, character_name):
        characters = self.get_data("character?sort=name:asc")
        character_id = [character['_id'] for character in characters if character_name.lower() in character['name'].lower()]
        character_id = character_id[0] if character_id else None

        if character_id:
            url = f"{self.LOTR_API_ENDPOINT}/character/{character_id}/quote"
            offset = random.randint(1, 299)
            params = {
                # "page": 2,
                # "limit": 20
                # "offset": offset
            }
            try:
                response = requests.get(url=url, headers=self.headers)#, params=params
                response.raise_for_status()
                # print(response.json())
                data = response.json().get('docs', [])   # Get 'docs' if present
                # print(data)
                return data
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return None
        return None
