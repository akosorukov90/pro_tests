import requests


class YaDisk:
    def __init__(self, token: str):
        self.token = token

    def create_folder(self, name_folder):
        HEADERS = {'Authorization': f'OAuth {self.token}'}
        response = requests.put(
            'https://cloud-api.yandex.net/v1/disk/resources',
            params={'path': name_folder},
            headers=HEADERS,
        )
        return str(response.status_code)

    def search_folder(self, name_folder):
        HEADERS = {'Authorization': f'OAuth {self.token}'}
        response = requests.get(
            'https://cloud-api.yandex.net/v1/disk/resources/',
            params={'path': name_folder},
            headers=HEADERS,
        )
        return str(response.status_code)

    def delete_folder(self, name_folder):
        HEADERS = {'Authorization': f'OAuth {self.token}'}
        response = requests.delete(
            'https://cloud-api.yandex.net/v1/disk/resources/',
            params={'path': name_folder},
            headers=HEADERS,
        )
        return str(response.status_code)
