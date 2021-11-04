from pprint import pprint

import requests

TOKEN = ''

class YaUploader:
    def __init__(self, token: str):
        self.token = token
    
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def upload_file_to_disk(self, file_path, filename):
        href = self.upload(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    
# if __name__ == '__main__':
#     ya = YaUploader(token=TOKEN)
#     # pprint(ya.get_files_list())
#     ya.upload_file_to_disk('test/test.txt', 'test.txt')

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = TOKEN
    uploader = YaUploader(token)
    path_to_file = (uploader.upload_file_to_disk('test/test.txt', 'test.txt'))
    result = uploader.upload(path_to_file)
    pprint(uploader.get_files_list())