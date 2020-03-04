import json


def get_server_info_value(key: str):

    with open('project/conf/server_info.json', mode='rt', encoding='utf-8') as file:
        data = json.load(file)
        for k, v in data.items():
            if k == key:
                return v
        raise ValueError('서버정보를 확인할 수 없습니다.')


def get_private_info_value(key: str):

    with open('project/conf/private_info.json', mode='rt', encoding='utf-8') as file:
        data = json.load(file)
        for k, v in data.items():
            if k == key:
                return v
        raise ValueError('개인정보를 확인할 수 없습니다.')

