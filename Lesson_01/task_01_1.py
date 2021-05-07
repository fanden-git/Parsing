"""
Посмотреть документацию к API GitHub, разобраться
как вывести список репозиториев для конкретного
пользователя, сохранить JSON-вывод в файле *.json
"""
import requests
import json
import os
from user_agent import generate_user_agent


def json_response(url, params=None):
    headers = {'User-Agent': generate_user_agent()}
    response = requests.get(url, headers=headers, params=params)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Response status code is not 200')
    except Exception as e:
        print(e)


# **********************************************************
if __name__ == '__main__':

    user = 'binance'
    url = f'https://api.github.com/users/{user}/repos'
    data_json = json_response(url)

    # запись всех данных в файл
    os.mkdir('data') if not os.path.isdir('data') else None
    with open(os.path.join('data', 'repos.json'), 'w', encoding='utf-8') as f:
        json.dump(data_json, f)

    print(f'Репозитории {user}:\n')
    for i in range(len(data_json)):
        print(data_json[i]['name'])


"""
Репозитории binance:

binance-api-postman
binance-public-data
binance-spot-api-docs
desktop
"""
