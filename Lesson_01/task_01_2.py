"""
Изучить список открытых API (https://www.programmableweb.com/category/all/apis)
Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы
к нему, пройдя авторизацию. Ответ сервера записать в файл.
"""

import requests
import json
import os
from icecream import ic


def json_response(url, params=None):
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception as e:
        print(e)

# **********************************************************
"""
The New York Times Newswire 
https://www.programmableweb.com/api/new-york-times-newswire-rest-api
https://developer.nytimes.com/docs/timeswire-product/1/overview
"""

if __name__ == '__main__':

    url = 'https://api.nytimes.com/svc/news/v3/content/nyt/world.json'
    params = {'api-key': ' ***** '}
    data_json = json_response(url, params)

    # запись всех данных в файл
    os.mkdir('data') if not os.path.isdir('data') else None
    with open(os.path.join('data', 'NYTimes.json'), 'w', encoding='utf-8') as f:
        json.dump(data_json, f)

    list_news = []
    for i in range(len(data_json['results'])):
        block = data_json['results'][i]
        list_news.append((block['published_date'],
                          block['title'],
                          block['abstract'],
                          block['url']))

    with open(os.path.join('data', 'list_nyt_news.json'), 'w', encoding='utf-8') as f:
        json.dump(list_news, f)

    ic(list_news)

"""
ic| list_news: [('2021-05-06T14:17:02-04:00',
                 'Somalia Moves to Defuse Tensions Both at Home and Abroad',
                 'The Somali leader dropped his divisive bid to extend his term, and the '
                 'country also moved to mend fences with its neighbor Kenya, restoring '
                 'diplomatic relations.',
                 'https://www.nytimes.com/2021/05/06/world/africa/somalia-kenya-diplomatic-relations.html'),
                 ...]
"""
