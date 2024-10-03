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

    def get_data1(self, data_type, page):
        url = f"{self.LOTR_API_ENDPOINT}/{data_type}"
        params = {
            # "offset": 3,
            "page": page
        }
        try:
            # response = requests.get(url=url, params=params, headers=self.headers)
            # response.raise_for_status()
            # data = response.json().get('docs', [])  # Get 'docs' if present
            data = []
            print(data)
            return data
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def fetch_quotes_for_character(self, character_name):
        characters = self.get_data("character")
        character_id = [character['_id'] for character in characters if character_name in character['name']]
        character_id = character_id[0] if character_id else None

        if character_id:
            url = f"{self.LOTR_API_ENDPOINT}//character/{character_id}/quote"
            params = {
                "page": 2,
                "limit": 20
            }
            try:
                response = requests.get(url=url, params=params, headers=self.headers)
                response.raise_for_status()
                data = response.json().get('docs', [])  # Get 'docs' if present
                print(data)
                return data
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return None
        return None
