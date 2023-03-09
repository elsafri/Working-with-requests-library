from pprint import pprint
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path_to_file: str):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        params = {'path': disk_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get('href', '')
        resp = requests.put(url=href, data=open(path_to_file, 'rb'))


if __name__ == '__main__':
    disk_path =
    path_to_file =
    token =
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
