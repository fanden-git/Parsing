"""
Изучить список открытых API (https://www.programmableweb.com/category/all/apis)
Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы
к нему, пройдя авторизацию. Ответ сервера записать в файл.
"""
import requests
import json
import os
from user_agent import generate_user_agent
from icecream import ic


def json_response(url, params=None):
    headers = {'User-Agent': generate_user_agent()}
    response = requests.get(url, headers=headers, params=params)
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
    params = {'api-key': '*****'}
    data_json = json_response(url, params)

    # запись всех данных в файл
    os.mkdir('data') if not os.path.isdir('data') else None
    with open(os.path.join('data', 'NYTimes.json'), 'w', encoding='utf-8') as f:
        json.dump(data_json, f)

    ic(data_json)



"""
ic| data_json: {'copyright': 'Copyright (c) 2021 The New York Times Company.  All Rights Reserved.',
                'num_results': 500,
                'results': [{'abstract': '',
                             'byline': 'BY SAMEER YASIR AND SUHASINI RAJ',
                             'created_date': '2021-05-06T06:29:25-04:00',
                             'des_facet': ['internal-essential'],
                             'first_published_date': '2021-05-06T06:29:25-04:00',
                             'geo_facet': None,
                             'item_type': 'Article',
                             'kicker': '',
                             'material_type_facet': 'Live Blog Post',
                             'multimedia': [{'caption': 'A vaccination center at a school in '
                                                        'New Delhi on Wednesday.\xa0',
                                             'copyright': 'Tauseef Mustafa/Agence '
                                                          'France-Presse — Getty Images',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06virus-briefing-india/merlin_187310751_62c86761-596b-44cf-a615-d0984064d6f8-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'A vaccination center at a school in '
                                                        'New Delhi on Wednesday.\xa0',
                                             'copyright': 'Tauseef Mustafa/Agence '
                                                          'France-Presse — Getty Images',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06virus-briefing-india/merlin_187310751_62c86761-596b-44cf-a615-d0984064d6f8-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'A vaccination center at a school in '
                                                        'New Delhi on Wednesday.\xa0',
                                             'copyright': 'Tauseef Mustafa/Agence '
                                                          'France-Presse — Getty Images',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06virus-briefing-india/merlin_187310751_62c86761-596b-44cf-a615-d0984064d6f8-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'A vaccination center at a school in '
                                                        'New Delhi on Wednesday.\xa0',
                                             'copyright': 'Tauseef Mustafa/Agence '
                                                          'France-Presse — Getty Images',
                                             'format': 'Normal',
                                             'height': 126,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06virus-briefing-india/merlin_187310751_62c86761-596b-44cf-a615-d0984064d6f8-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': None,
                             'per_facet': None,
                             'published_date': '2021-05-06T06:29:25-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '06-virus-briefing-india',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': '',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/06/world/06virus-briefing-india/merlin_187310751_62c86761-596b-44cf-a615-d0984064d6f8-thumbStandard.jpg',
                             'title': 'India’s vaccinations decline as its coronavirus '
                                      'outbreak reaches new highs.',
                             'updated_date': '2021-05-06T06:29:25-04:00',
                             'url': 'https://www.nytimes.com/live/2021/05/06/world/covid-vaccine-coronavirus-cases/indias-vaccinations-decline-as-its-coronavirus-outbreak-reaches-new-highs'},
                            {'abstract': 'French fishing crews are threatening to blockade a '
                                         'port on the island of Jersey in a standoff over '
                                         'post-Brexit fishing rights in the waters nearby.',
                             'byline': 'BY MARK LANDLER AND STEPHEN CASTLE',
                             'created_date': '2021-05-06T06:26:49-04:00',
                             'des_facet': ['Politics and Government',
                                           'International Trade and World Market',
                                           'Fishing, Commercial',
                                           'Great Britain Withdrawal from EU (Brexit)'],
                             'first_published_date': '2021-05-06T06:26:49-04:00',
                             'geo_facet': ['Channel Islands', 'Great Britain'],
                             'item_type': 'Article',
                             'kicker': '',
                             'material_type_facet': 'News',
                             'multimedia': [{'caption': 'French fishing boats at the entrance '
                                                        'to the harbor in St. Helier, Jersey, '
                                                        'on Thursday.',
                                             'copyright': 'Marc Le Cornu, via Reuters',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06jersey/06jersey-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'French fishing boats at the entrance '
                                                        'to the harbor in St. Helier, Jersey, '
                                                        'on Thursday.',
                                             'copyright': 'Marc Le Cornu, via Reuters',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06jersey/merlin_187356834_0ab47df7-fa6b-44a0-b42e-8960ba77cfab-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'French fishing boats at the entrance '
                                                        'to the harbor in St. Helier, Jersey, '
                                                        'on Thursday.',
                                             'copyright': 'Marc Le Cornu, via Reuters',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06jersey/merlin_187356834_0ab47df7-fa6b-44a0-b42e-8960ba77cfab-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'French fishing boats at the entrance '
                                                        'to the harbor in St. Helier, Jersey, '
                                                        'on Thursday.',
                                             'copyright': 'Marc Le Cornu, via Reuters',
                                             'format': 'Normal',
                                             'height': 127,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06jersey/merlin_187356834_0ab47df7-fa6b-44a0-b42e-8960ba77cfab-articleInline.jpg',
                                             'width': 190}], ...................                             
...................................
"""