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
                                             'width': 190}],
                             'org_facet': None,
                             'per_facet': ['Johnson, Boris'],
                             'published_date': '2021-05-06T06:26:49-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '06jersey',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': 'Europe',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/06/world/06jersey/06jersey-thumbStandard.jpg',
                             'title': 'U.K. and France Send Naval Ships to Channel Island in '
                                      'Tense Fishing Dispute',
                             'updated_date': '2021-05-06T06:33:38-04:00',
                             'url': 'https://www.nytimes.com/2021/05/06/world/europe/uk-france-jersey-fishing.html'},
                            {'abstract': '',
                             'byline': 'BY NATASHA FROST AND YAN ZHUANG',
                             'created_date': '2021-05-06T05:25:50-04:00',
                             'des_facet': ['internal-essential'],
                             'first_published_date': '2021-05-06T05:25:50-04:00',
                             'geo_facet': None,
                             'item_type': 'Article',
                             'kicker': 'Global Roundup',
                             'material_type_facet': 'Live Blog Post',
                             'multimedia': [{'caption': 'A checkpoint in Suva, Fiji, last '
                                                        'week, after the Fijian capital '
                                                        'entered a 14-day lockdown.',
                                             'copyright': 'Leon Lord/Agence France-Presse — '
                                                          'Getty Images',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06virus-briefing-roundup/06virus-briefing-roundup-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'A checkpoint in Suva, Fiji, last '
                                                        'week, after the Fijian capital '
                                                        'entered a 14-day lockdown.',
                                             'copyright': 'Leon Lord/Agence France-Presse — '
                                                          'Getty Images',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06virus-briefing-roundup/merlin_186965841_64f3f913-5113-4548-a9dc-209e7f805257-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'A checkpoint in Suva, Fiji, last '
                                                        'week, after the Fijian capital '
                                                        'entered a 14-day lockdown.',
                                             'copyright': 'Leon Lord/Agence France-Presse — '
                                                          'Getty Images',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06virus-briefing-roundup/merlin_186965841_64f3f913-5113-4548-a9dc-209e7f805257-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'A checkpoint in Suva, Fiji, last '
                                                        'week, after the Fijian capital '
                                                        'entered a 14-day lockdown.',
                                             'copyright': 'Leon Lord/Agence France-Presse — '
                                                          'Getty Images',
                                             'format': 'Normal',
                                             'height': 127,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06virus-briefing-roundup/merlin_186965841_64f3f913-5113-4548-a9dc-209e7f805257-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': None,
                             'per_facet': None,
                             'published_date': '2021-05-06T05:25:50-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '06-virus-briefing-global-roundup',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': '',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/06/world/06virus-briefing-roundup/06virus-briefing-roundup-thumbStandard.jpg',
                             'title': 'Troops lock down a hospital to contain a rare outbreak '
                                      'in Fiji, and other news from around the world.',
                             'updated_date': '2021-05-06T06:43:43-04:00',
                             'url': 'https://www.nytimes.com/live/2021/05/06/world/covid-vaccine-coronavirus-cases/troops-lock-down-a-hospital-to-contain-a-rare-outbreak-in-fiji-and-other-news-from-around-the-world'},
                            {'abstract': 'After years working on American bases in '
                                         'Afghanistan and fearful of the Taliban, Afghans are '
                                         'heading to Turkey and Europe.',
                             'byline': 'BY CARLOTTA GALL',
                             'created_date': '2021-05-06T05:00:19-04:00',
                             'des_facet': ['Afghanistan War (2001- )',
                                           'Immigration and Emigration'],
                             'first_published_date': '2021-05-06T05:00:19-04:00',
                             'geo_facet': ['Afghanistan', 'Istanbul (Turkey)', 'Turkey'],
                             'item_type': 'Article',
                             'kicker': '',
                             'material_type_facet': 'News',
                             'multimedia': [{'caption': 'An Afghan refugee collecting plastic '
                                                        'and cardboard for recycling in '
                                                        'Istanbul.',
                                             'copyright': 'Ivor Prickett for The New York '
                                                          'Times',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/us/06turkey-afghans-promo/06turkey-afghans-promo-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'An Afghan refugee collecting plastic '
                                                        'and cardboard for recycling in '
                                                        'Istanbul.',
                                             'copyright': 'Ivor Prickett for The New York '
                                                          'Times',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/us/06turkey-afghans-promo/06turkey-afghans-promo-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'An Afghan refugee collecting plastic '
                                                        'and cardboard for recycling in '
                                                        'Istanbul.',
                                             'copyright': 'Ivor Prickett for The New York '
                                                          'Times',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/us/06turkey-afghans-promo/06turkey-afghans-promo-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'An Afghan refugee collecting plastic '
                                                        'and cardboard for recycling in '
                                                        'Istanbul.',
                                             'copyright': 'Ivor Prickett for The New York '
                                                          'Times',
                                             'format': 'Normal',
                                             'height': 127,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/us/06turkey-afghans-promo/06turkey-afghans-promo-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': ['Taliban'],
                             'per_facet': None,
                             'published_date': '2021-05-06T05:00:19-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '06turkey-afghans',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': 'Asia Pacific',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/06/us/06turkey-afghans-promo/06turkey-afghans-promo-thumbStandard.jpg',
                             'title': 'Afghans Fleeing Home Are Filling the Lowliest Jobs in '
                                      'Istanbul',
                             'updated_date': '2021-05-06T05:00:19-04:00',
                             'url': 'https://www.nytimes.com/2021/05/06/world/asia/afghan-migrants-istanbul.html'},
                            {'abstract': '',
                             'byline': 'BY MATINA STEVIS-GRIDNEFF',
                             'created_date': '2021-05-06T04:59:09-04:00',
                             'des_facet': ['internal-essential'],
                             'first_published_date': '2021-05-06T04:59:09-04:00',
                             'geo_facet': None,
                             'item_type': 'Article',
                             'kicker': '',
                             'material_type_facet': 'Live Blog Post',
                             'multimedia': [{'caption': 'The European Union is one of the '
                                                        'world’s largest producers, exporters '
                                                        'and consumers of vaccines.',
                                             'copyright': 'Alessandro Grassani for The New '
                                                          'York Times',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06virus-briefing-eu/06virus-briefing-eu-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'The European Union is one of the '
                                                        'world’s largest producers, exporters '
                                                        'and consumers of vaccines.',
                                             'copyright': 'Alessandro Grassani for The New '
                                                          'York Times',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06virus-briefing-eu/merlin_181698105_29d33187-b283-455c-8eca-4e1f76dad2d3-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'The European Union is one of the '
                                                        'world’s largest producers, exporters '
                                                        'and consumers of vaccines.',
                                             'copyright': 'Alessandro Grassani for The New '
                                                          'York Times',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06virus-briefing-eu/merlin_181698105_29d33187-b283-455c-8eca-4e1f76dad2d3-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'The European Union is one of the '
                                                        'world’s largest producers, exporters '
                                                        'and consumers of vaccines.',
                                             'copyright': 'Alessandro Grassani for The New '
                                                          'York Times',
                                             'format': 'Normal',
                                             'height': 127,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06virus-briefing-eu/merlin_181698105_29d33187-b283-455c-8eca-4e1f76dad2d3-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': None,
                             'per_facet': None,
                             'published_date': '2021-05-06T04:59:09-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '06-virus-briefing-eu-vaccines',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': '',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/06/world/06virus-briefing-eu/06virus-briefing-eu-thumbStandard.jpg',
                             'title': 'The E.U. says it’s willing to discuss a patent waiver '
                                      'for Covid vaccines.',
                             'updated_date': '2021-05-06T04:59:09-04:00',
                             'url': 'https://www.nytimes.com/live/2021/05/06/world/covid-vaccine-coronavirus-cases/the-eu-says-its-willing-to-discuss-a-patent-waiver-for-covid-vaccines'},
                            {'abstract': '',
                             'byline': 'BY EMILY ANTHES, SHARON OTTERMAN, APOORVA MANDAVILLI '
                                       'AND ALLYSON WALLER',
                             'created_date': '2021-05-06T04:59:06-04:00',
                             'des_facet': ['internal-essential'],
                             'first_published_date': '2021-05-06T04:59:06-04:00',
                             'geo_facet': None,
                             'item_type': 'Article',
                             'kicker': '',
                             'material_type_facet': 'Live Blog Post',
                             'multimedia': [{'caption': 'Getting a dose of the Pfizer '
                                                        'BioNTech Covid-19 vaccine\xa0in '
                                                        'Aberdeen, Md., on Wednesday.\xa0',
                                             'copyright': 'Chip Somodevilla/Getty Images',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/science/06virus-brief-vaccine-variants/merlin_187334007_1b66fc0f-30e7-4e81-a56f-07cb6f02e032-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'Getting a dose of the Pfizer '
                                                        'BioNTech Covid-19 vaccine\xa0in '
                                                        'Aberdeen, Md., on Wednesday.\xa0',
                                             'copyright': 'Chip Somodevilla/Getty Images',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/science/06virus-brief-vaccine-variants/merlin_187334007_1b66fc0f-30e7-4e81-a56f-07cb6f02e032-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'Getting a dose of the Pfizer '
                                                        'BioNTech Covid-19 vaccine\xa0in '
                                                        'Aberdeen, Md., on Wednesday.\xa0',
                                             'copyright': 'Chip Somodevilla/Getty Images',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/science/06virus-brief-vaccine-variants/merlin_187334007_1b66fc0f-30e7-4e81-a56f-07cb6f02e032-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'Getting a dose of the Pfizer '
                                                        'BioNTech Covid-19 vaccine\xa0in '
                                                        'Aberdeen, Md., on Wednesday.\xa0',
                                             'copyright': 'Chip Somodevilla/Getty Images',
                                             'format': 'Normal',
                                             'height': 127,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/science/06virus-brief-vaccine-variants/merlin_187334007_1b66fc0f-30e7-4e81-a56f-07cb6f02e032-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': None,
                             'per_facet': None,
                             'published_date': '2021-05-06T04:59:06-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '06-virus-briefing-pfizer-variants',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': '',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/06/science/06virus-brief-vaccine-variants/merlin_187334007_1b66fc0f-30e7-4e81-a56f-07cb6f02e032-thumbStandard.jpg',
                             'title': 'New studies suggest that vaccines can protect against '
                                      'some variants and severe Covid cases.',
                             'updated_date': '2021-05-06T04:59:06-04:00',
                             'url': 'https://www.nytimes.com/live/2021/05/06/world/covid-vaccine-coronavirus-cases/new-studies-suggest-that-vaccines-can-protect-against-some-variants-and-severe-covid-cases'},
                            {'abstract': 'A $230,000 statue is part of an effort to revive '
                                         'tourism in the fishing town of Noto. Critics call '
                                         'it a waste of money as Japan struggles to contain a '
                                         'new outbreak.',
                             'byline': 'BY HISAKO UENO AND SHASHANK BENGALI',
                             'created_date': '2021-05-06T04:59:06-04:00',
                             'des_facet': ['Coronavirus (2019-nCoV)'],
                             'first_published_date': '2021-05-06T04:59:06-04:00',
                             'geo_facet': ['Japan'],
                             'item_type': 'Article',
                             'kicker': '',
                             'material_type_facet': 'News',
                             'multimedia': [{'caption': 'A giant squid statue, made at a cost '
                                                        'of nearly $230,000, in the town of '
                                                        'Noto, Japan.',
                                             'copyright': 'Noto Town, via Agence '
                                                          'France-Presse — Getty Images',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06-virus-briefing-japan-squid/06-virus-briefing-japan-squid-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'A giant squid statue, made at a cost '
                                                        'of nearly $230,000, in the town of '
                                                        'Noto, Japan.',
                                             'copyright': 'Noto Town, via Agence '
                                                          'France-Presse — Getty Images',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06-virus-briefing-japan-squid/06-virus-briefing-japan-squid-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'A giant squid statue, made at a cost '
                                                        'of nearly $230,000, in the town of '
                                                        'Noto, Japan.',
                                             'copyright': 'Noto Town, via Agence '
                                                          'France-Presse — Getty Images',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06-virus-briefing-japan-squid/06-virus-briefing-japan-squid-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'A giant squid statue, made at a cost '
                                                        'of nearly $230,000, in the town of '
                                                        'Noto, Japan.',
                                             'copyright': 'Noto Town, via Agence '
                                                          'France-Presse — Getty Images',
                                             'format': 'Normal',
                                             'height': 126,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06-virus-briefing-japan-squid/06-virus-briefing-japan-squid-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': None,
                             'per_facet': None,
                             'published_date': '2021-05-06T04:59:06-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '06-virus-briefing-japan-squid',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': 'Asia Pacific',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/06/world/06-virus-briefing-japan-squid/06-virus-briefing-japan-squid-thumbStandard.jpg',
                             'title': 'A town in Japan spent Covid relief funds on a giant '
                                      'squid statue.',
                             'updated_date': '2021-05-06T04:59:06-04:00',
                             'url': 'https://www.nytimes.com/2021/05/06/world/asia/japan-squid-statue.html'},
                            {'abstract': 'The head of the European Commission said the E.U. '
                                         'would consider proposals on waiving intellectual '
                                         'property rights, following the Biden '
                                         'administration’s reversal of U.S. policy.',
                             'byline': 'BY MATINA STEVIS-GRIDNEFF',
                             'created_date': '2021-05-06T04:27:01-04:00',
                             'des_facet': ['Coronavirus (2019-nCoV)',
                                           'Vaccination and Immunization'],
                             'first_published_date': '2021-05-06T04:27:01-04:00',
                             'geo_facet': ['Brussels (Belgium)'],
                             'item_type': 'Article',
                             'kicker': '',
                             'material_type_facet': 'News',
                             'multimedia': [{'caption': 'A vaccination center in the\xa0'
                                                        'Castello di Rivoli museum in Rivoli, '
                                                        'Italy.\xa0',
                                             'copyright': 'Alessandro Grassani for The New '
                                                          'York Times',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06virus-eu-vaccine1/06virus-eu-vaccine1-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'A vaccination center in the\xa0'
                                                        'Castello di Rivoli museum in Rivoli, '
                                                        'Italy.\xa0',
                                             'copyright': 'Alessandro Grassani for The New '
                                                          'York Times',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06virus-eu-vaccine1/merlin_187145244_bfb34b6b-1f78-4550-a3d0-4cbfa0bd1784-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'A vaccination center in the\xa0'
                                                        'Castello di Rivoli museum in Rivoli, '
                                                        'Italy.\xa0',
                                             'copyright': 'Alessandro Grassani for The New '
                                                          'York Times',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06virus-eu-vaccine1/merlin_187145244_bfb34b6b-1f78-4550-a3d0-4cbfa0bd1784-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'A vaccination center in the\xa0'
                                                        'Castello di Rivoli museum in Rivoli, '
                                                        'Italy.\xa0',
                                             'copyright': 'Alessandro Grassani for The New '
                                                          'York Times',
                                             'format': 'Normal',
                                             'height': 127,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06virus-eu-vaccine1/merlin_187145244_bfb34b6b-1f78-4550-a3d0-4cbfa0bd1784-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': None,
                             'per_facet': ['von der Leyen, Ursula'],
                             'published_date': '2021-05-06T04:27:01-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '06virus-eu-vaccines',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': 'Europe',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/06/world/06virus-eu-vaccine1/06virus-eu-vaccine1-thumbStandard.jpg',
                             'title': 'E.U. Leader Says Bloc Is Willing to Discuss Patent '
                                      'Waiver for Covid Vaccines',
                             'updated_date': '2021-05-06T05:27:38-04:00',
                             'url': 'https://www.nytimes.com/2021/05/06/world/europe/coronavirus-vaccine-patent-eu.html'},
                            {'abstract': 'If the pro-independence vote surges in Thursday’s '
                                         'elections for the Scottish Parliament, momentum for '
                                         'an another referendum on independence may become '
                                         'unstoppable.',
                             'byline': 'BY ANDREW TESTA AND STEPHEN CASTLE',
                             'created_date': '2021-05-06T00:15:20-04:00',
                             'des_facet': ['Referendums',
                                           'Secession and Independence Movements',
                                           'Great Britain Withdrawal from EU (Brexit)'],
                             'first_published_date': '2021-05-06T00:15:20-04:00',
                             'geo_facet': ['Scotland'],
                             'item_type': 'Article',
                             'kicker': '',
                             'material_type_facet': 'News',
                             'multimedia': [{'caption': 'The Carter Bar border point between '
                                                        'England and Scotland.\xa0',
                                             'copyright': '',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06Scotland-Photos/06Scotland-Photos-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'The Carter Bar border point between '
                                                        'England and Scotland.\xa0',
                                             'copyright': '',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06Scotland-Photos/06Scotland-Photos-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'The Carter Bar border point between '
                                                        'England and Scotland.\xa0',
                                             'copyright': '',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06Scotland-Photos/06Scotland-Photos-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'The Carter Bar border point between '
                                                        'England and Scotland.\xa0',
                                             'copyright': '',
                                             'format': 'Normal',
                                             'height': 127,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/06/world/06Scotland-Photos/06Scotland-Photos-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': ['Scottish National Party'],
                             'per_facet': ['Johnson, Boris',
                                           'Salmond, Alex',
                                           'Sturgeon, Nicola'],
                             'published_date': '2021-05-06T00:15:20-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '05scotland-photos',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': '',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/06/world/06Scotland-Photos/06Scotland-Photos-thumbStandard.jpg',
                             'title': 'Scenes of Scotland, as It Weighs Its Future Within '
                                      'Britain',
                             'updated_date': '2021-05-06T06:55:24-04:00',
                             'url': 'https://www.nytimes.com/2021/05/06/world/scotland-election-brexit-independence.html'},
                            {'abstract': 'The United States is also urging its citizens to '
                                         'leave the country.',
                             'byline': 'BY ALLYSON WALLER',
                             'created_date': '2021-05-05T22:31:07-04:00',
                             'des_facet': ['internal-essential', 'Coronavirus (2019-nCoV)'],
                             'first_published_date': '2021-05-05T22:31:07-04:00',
                             'geo_facet': ['India'],
                             'item_type': 'Article',
                             'kicker': '',
                             'material_type_facet': 'News',
                             'multimedia': [{'caption': 'Italian residents returned to '
                                                        'Bergamo, Italy, on Monday from the '
                                                        'northern Indian city of Amritsar '
                                                        'after taking a charter flight. The '
                                                        'United States government is urging '
                                                        'its citizens to leave the '
                                                        'country.\xa0',
                                             'copyright': 'Filippo Venezia/EPA, via '
                                                          'Shutterstock',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05virus-brief-state-dept-india/merlin_187259409_e9c5ba07-6272-41b2-b300-54da577a9a1d-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'Italian residents returned to '
                                                        'Bergamo, Italy, on Monday from the '
                                                        'northern Indian city of Amritsar '
                                                        'after taking a charter flight. The '
                                                        'United States government is urging '
                                                        'its citizens to leave the '
                                                        'country.\xa0',
                                             'copyright': 'Filippo Venezia/EPA, via '
                                                          'Shutterstock',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05virus-brief-state-dept-india/merlin_187259409_e9c5ba07-6272-41b2-b300-54da577a9a1d-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'Italian residents returned to '
                                                        'Bergamo, Italy, on Monday from the '
                                                        'northern Indian city of Amritsar '
                                                        'after taking a charter flight. The '
                                                        'United States government is urging '
                                                        'its citizens to leave the '
                                                        'country.\xa0',
                                             'copyright': 'Filippo Venezia/EPA, via '
                                                          'Shutterstock',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05virus-brief-state-dept-india/merlin_187259409_e9c5ba07-6272-41b2-b300-54da577a9a1d-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'Italian residents returned to '
                                                        'Bergamo, Italy, on Monday from the '
                                                        'northern Indian city of Amritsar '
                                                        'after taking a charter flight. The '
                                                        'United States government is urging '
                                                        'its citizens to leave the '
                                                        'country.\xa0',
                                             'copyright': 'Filippo Venezia/EPA, via '
                                                          'Shutterstock',
                                             'format': 'Normal',
                                             'height': 136,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05virus-brief-state-dept-india/merlin_187259409_e9c5ba07-6272-41b2-b300-54da577a9a1d-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': ['State Department'],
                             'per_facet': None,
                             'published_date': '2021-05-05T22:31:07-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '05-virus-briefing-state-department',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': '',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/05/world/05virus-brief-state-dept-india/merlin_187259409_e9c5ba07-6272-41b2-b300-54da577a9a1d-thumbStandard.jpg',
                             'title': 'State Department approves voluntary departure of '
                                      'nonemergency personnel from India.',
                             'updated_date': '2021-05-06T04:14:28-04:00',
                             'url': 'https://www.nytimes.com/2021/05/05/world/state-department-india-covid.html'},
                            {'abstract': 'Colombians continued to protest on Wednesday for an '
                                         'eighth day in a row, demanding an end to '
                                         'inequality, corruption and the economic devastation '
                                         'caused by the coronavirus.',
                             'byline': 'BY THE ASSOCIATED PRESS AND REUTERS',
                             'created_date': '2021-05-05T22:03:37-04:00',
                             'des_facet': ['Demonstrations, Protests and Riots',
                                           'Police Brutality, Misconduct and Shootings'],
                             'first_published_date': '2021-05-05T22:03:37-04:00',
                             'geo_facet': ['Colombia'],
                             'item_type': 'Video',
                             'kicker': '',
                             'material_type_facet': 'Video',
                             'multimedia': [{'caption': 'The police clashing with '
                                                        'demonstrators in a public square in '
                                                        'Bogotá during protests that have '
                                                        'left at least 24 people dead and 87 '
                                                        'missing.',
                                             'copyright': 'Federico Rios for The New York '
                                                          'Times',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05colombia-top-new/05colombia-top-new-thumbStandard-v2.jpg',
                                             'width': 75},
                                            {'caption': 'The police clashing with '
                                                        'demonstrators in a public square in '
                                                        'Bogotá during protests that have '
                                                        'left at least 24 people dead and 87 '
                                                        'missing.',
                                             'copyright': 'Federico Rios for The New York '
                                                          'Times',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05colombia-top-new/05colombia-top-new-mediumThreeByTwo210-v2.jpg',
                                             'width': 210},
                                            {'caption': 'The police clashing with '
                                                        'demonstrators in a public square in '
                                                        'Bogotá during protests that have '
                                                        'left at least 24 people dead and 87 '
                                                        'missing.',
                                             'copyright': 'Federico Rios for The New York '
                                                          'Times',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05colombia-top-new/05colombia-top-new-mediumThreeByTwo440-v2.jpg',
                                             'width': 440},
                                            {'caption': 'The police clashing with '
                                                        'demonstrators in a public square in '
                                                        'Bogotá during protests that have '
                                                        'left at least 24 people dead and 87 '
                                                        'missing.',
                                             'copyright': 'Federico Rios for The New York '
                                                          'Times',
                                             'format': 'Normal',
                                             'height': 127,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05colombia-top-new/05colombia-top-new-articleInline-v2.jpg',
                                             'width': 190}],
                             'org_facet': None,
                             'per_facet': None,
                             'published_date': '2021-05-05T22:03:37-04:00',
                             'related_urls': [{'suggested_link_text': 'Colombia Police '
                                                                      'Respond to Protests '
                                                                      'With Bullets, and '
                                                                      'Death Toll Mounts',
                                               'url': 'https://www.nytimes.com/2021/05/05/world/americas/colombia-covid-protests-duque.html'}],
                             'section': 'World',
                             'slug_name': '05vid-colombia-protests',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': 'Americas',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/05/world/05colombia-top-new/05colombia-top-new-thumbStandard-v2.jpg',
                             'title': 'Protests Continue in Colombia',
                             'updated_date': '2021-05-05T22:03:37-04:00',
                             'url': 'https://www.nytimes.com/video/world/americas/100000007748095/colombia-crisis-protest.html'},
                            {'abstract': '印度疫情严重，中国民族主义宣传引发反弹；菲律宾外长对中国爆粗口引发外交风波；Facebook维持对特朗普禁言令；英国中期选举保守党选情占优；美国称俄罗斯仅从乌克兰边境少量撤兵……这里是今日要闻。',
                             'byline': 'BY EMILY CHAN AND KONEY BAI',
                             'created_date': '2021-05-05T22:00:41-04:00',
                             'des_facet': None,
                             'first_published_date': '2021-05-05T22:00:41-04:00',
                             'geo_facet': None,
                             'item_type': 'Article',
                             'kicker': '',
                             'material_type_facet': 'briefing',
                             'multimedia': [{'caption': '2020年12月，欧洲领导人和中国国家主席习近平举行视频会议。',
                                             'copyright': 'Pool photo by Sebastien Nogier',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/01/06/world/cn-06EU-china1-copy/06EU-china1-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': '2020年12月，欧洲领导人和中国国家主席习近平举行视频会议。',
                                             'copyright': 'Pool photo by Sebastien Nogier',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/01/06/world/cn-06EU-china1-copy/merlin_181799964_62be29cf-a006-44bd-89c5-b721a5f2c885-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': '2020年12月，欧洲领导人和中国国家主席习近平举行视频会议。',
                                             'copyright': 'Pool photo by Sebastien Nogier',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/01/06/world/cn-06EU-china1-copy/merlin_181799964_62be29cf-a006-44bd-89c5-b721a5f2c885-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': '2020年12月，欧洲领导人和中国国家主席习近平举行视频会议。',
                                             'copyright': 'Pool photo by Sebastien Nogier',
                                             'format': 'Normal',
                                             'height': 127,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/01/06/world/cn-06EU-china1-copy/merlin_181799964_62be29cf-a006-44bd-89c5-b721a5f2c885-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': None,
                             'per_facet': None,
                             'published_date': '2021-05-05T22:00:41-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': 'c06chinese-briefing-web',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': 'Asia Pacific',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/01/06/world/cn-06EU-china1-copy/06EU-china1-thumbStandard.jpg',
                             'title': '简报：欧盟加码对中资公司限制；美国支持取消新冠疫苗专利保护',
                             'updated_date': '2021-05-05T22:58:13-04:00',
                             'url': 'https://www.nytimes.com/zh-hans/2021/05/05/world/asia/eu-china-tension-covid-vaccine-patent.html'},
                            {'abstract': '',
                             'byline': 'BY JULIE TURKEWITZ AND SOFÍA VILLAMIL',
                             'created_date': '2021-05-05T21:57:38-04:00',
                             'des_facet': ['internal-essential'],
                             'first_published_date': '2021-05-05T21:57:38-04:00',
                             'geo_facet': None,
                             'item_type': 'Article',
                             'kicker': '',
                             'material_type_facet': 'Live Blog Post',
                             'multimedia': [{'caption': 'There were road blocks, fires and '
                                                        'riots in southern Bogotá on Tuesday '
                                                        'after a week of protests and strikes '
                                                        'over tax reforms proposed by the '
                                                        'Colombian government.',
                                             'copyright': 'Federico Rios for The New York '
                                                          'Times',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05virus-brief-colombia/05virus-brief-colombia-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'There were road blocks, fires and '
                                                        'riots in southern Bogotá on Tuesday '
                                                        'after a week of protests and strikes '
                                                        'over tax reforms proposed by the '
                                                        'Colombian government.',
                                             'copyright': 'Federico Rios for The New York '
                                                          'Times',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05virus-brief-colombia/merlin_187321587_c98165a5-a60d-4d53-8f38-d8c19c0d3c06-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'There were road blocks, fires and '
                                                        'riots in southern Bogotá on Tuesday '
                                                        'after a week of protests and strikes '
                                                        'over tax reforms proposed by the '
                                                        'Colombian government.',
                                             'copyright': 'Federico Rios for The New York '
                                                          'Times',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05virus-brief-colombia/merlin_187321587_c98165a5-a60d-4d53-8f38-d8c19c0d3c06-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'There were road blocks, fires and '
                                                        'riots in southern Bogotá on Tuesday '
                                                        'after a week of protests and strikes '
                                                        'over tax reforms proposed by the '
                                                        'Colombian government.',
                                             'copyright': 'Federico Rios for The New York '
                                                          'Times',
                                             'format': 'Normal',
                                             'height': 127,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05virus-brief-colombia/merlin_187321587_c98165a5-a60d-4d53-8f38-d8c19c0d3c06-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': None,
                             'per_facet': None,
                             'published_date': '2021-05-05T21:57:38-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '05-virus-briefing-colombia',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': '',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/05/world/05virus-brief-colombia/05virus-brief-colombia-thumbStandard.jpg',
                             'title': 'Colombia, strained by the pandemic and economic '
                                      'hardship, explodes in protest.',
                             'updated_date': '2021-05-06T04:04:49-04:00',
                             'url': 'https://www.nytimes.com/live/2021/05/05/world/covid-vaccine-coronavirus-cases/colombia-strained-by-the-pandemic-and-economic-hardship-explodes-in-protest'},
                            {'abstract': 'The eruption of anger in Colombia, where at least '
                                         '24 have died as the government cracks down on the '
                                         'protests, could spread to other countries in the '
                                         'region that share the same combustible conditions.',
                             'byline': 'BY JULIE TURKEWITZ AND SOFÍA VILLAMIL',
                             'created_date': '2021-05-05T18:37:03-04:00',
                             'des_facet': ['Demonstrations, Protests and Riots',
                                           'Coronavirus (2019-nCoV)'],
                             'first_published_date': '2021-05-05T18:37:03-04:00',
                             'geo_facet': ['Bogota (Colombia)', 'Latin America'],
                             'item_type': 'Article',
                             'kicker': '',
                             'material_type_facet': 'News',
                             'multimedia': [{'caption': 'The police clashing with '
                                                        'demonstrators in a public square in '
                                                        'Bogotá during protests that have '
                                                        'left at least 24 people dead and 87 '
                                                        'missing.',
                                             'copyright': 'Federico Rios for The New York '
                                                          'Times',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05colombia-top-new/05colombia-top-new-thumbStandard-v2.jpg',
                                             'width': 75},
                                            {'caption': 'The police clashing with '
                                                        'demonstrators in a public square in '
                                                        'Bogotá during protests that have '
                                                        'left at least 24 people dead and 87 '
                                                        'missing.',
                                             'copyright': 'Federico Rios for The New York '
                                                          'Times',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05colombia-top-new/05colombia-top-new-mediumThreeByTwo210-v2.jpg',
                                             'width': 210},
                                            {'caption': 'The police clashing with '
                                                        'demonstrators in a public square in '
                                                        'Bogotá during protests that have '
                                                        'left at least 24 people dead and 87 '
                                                        'missing.',
                                             'copyright': 'Federico Rios for The New York '
                                                          'Times',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05colombia-top-new/05colombia-top-new-mediumThreeByTwo440-v2.jpg',
                                             'width': 440},
                                            {'caption': 'The police clashing with '
                                                        'demonstrators in a public square in '
                                                        'Bogotá during protests that have '
                                                        'left at least 24 people dead and 87 '
                                                        'missing.',
                                             'copyright': 'Federico Rios for The New York '
                                                          'Times',
                                             'format': 'Normal',
                                             'height': 127,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05colombia-top-new/05colombia-top-new-articleInline-v2.jpg',
                                             'width': 190}],
                             'org_facet': None,
                             'per_facet': ['Duque, Ivan'],
                             'published_date': '2021-05-05T18:37:03-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '05colombia-protests',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': 'Americas',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/05/world/05colombia-top-new/05colombia-top-new-thumbStandard-v2.jpg',
                             'title': 'Colombia Police Respond to Protests With Bullets, and '
                                      'Death Toll Mounts',
                             'updated_date': '2021-05-06T04:16:13-04:00',
                             'url': 'https://www.nytimes.com/2021/05/05/world/americas/colombia-covid-protests-duque.html'},
                            {'abstract': 'The French president’s speech on the 200th '
                                         'anniversary of the emperor’s death combined a '
                                         'rebuke for a betrayal of the Enlightenment and '
                                         'recognition of his achievements.',
                             'byline': 'BY ROGER COHEN',
                             'created_date': '2021-05-05T17:35:18-04:00',
                             'des_facet': ['Politics and Government',
                                           'Slavery (Historical)',
                                           'Discrimination'],
                             'first_published_date': '2021-05-05T17:35:18-04:00',
                             'geo_facet': ['France'],
                             'item_type': 'Article',
                             'kicker': '',
                             'material_type_facet': 'News',
                             'multimedia': [{'caption': 'President Emmanuel Macron of France '
                                                        'and his wife, Brigitte, at the tomb '
                                                        'of Napoleon Bonaparte on Wednesday '
                                                        'in Paris.',
                                             'copyright': 'Pool photo by Christophe Petit '
                                                          'Tesson',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05france-macron/merlin_187326648_4e75c4cf-5b4b-48e1-bf1e-41421fc958ae-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'President Emmanuel Macron of France '
                                                        'and his wife, Brigitte, at the tomb '
                                                        'of Napoleon Bonaparte on Wednesday '
                                                        'in Paris.',
                                             'copyright': 'Pool photo by Christophe Petit '
                                                          'Tesson',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05france-macron/merlin_187326648_4e75c4cf-5b4b-48e1-bf1e-41421fc958ae-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'President Emmanuel Macron of France '
                                                        'and his wife, Brigitte, at the tomb '
                                                        'of Napoleon Bonaparte on Wednesday '
                                                        'in Paris.',
                                             'copyright': 'Pool photo by Christophe Petit '
                                                          'Tesson',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05france-macron/merlin_187326648_4e75c4cf-5b4b-48e1-bf1e-41421fc958ae-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'President Emmanuel Macron of France '
                                                        'and his wife, Brigitte, at the tomb '
                                                        'of Napoleon Bonaparte on Wednesday '
                                                        'in Paris.',
                                             'copyright': 'Pool photo by Christophe Petit '
                                                          'Tesson',
                                             'format': 'Normal',
                                             'height': 127,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05france-macron/merlin_187326648_4e75c4cf-5b4b-48e1-bf1e-41421fc958ae-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': None,
                             'per_facet': ['Bonaparte, Napoleon', 'Macron, Emmanuel (1977- )'],
                             'published_date': '2021-05-05T17:35:18-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '05France-Macron',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': 'Europe',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/05/world/05france-macron/merlin_187326648_4e75c4cf-5b4b-48e1-bf1e-41421fc958ae-thumbStandard.jpg',
                             'title': 'Macron Condemns Napoleon’s Restoration of Slavery',
                             'updated_date': '2021-05-06T04:55:24-04:00',
                             'url': 'https://www.nytimes.com/2021/05/05/world/europe/france-macron-napoleon-slavery.html'},
                            {'abstract': 'The two American men were teenagers in July 2019 '
                                         'when an early-morning scuffle with two plainclothes '
                                         'police officers in Rome turned deadly.',
                             'byline': 'BY ELISABETTA POVOLEDO',
                             'created_date': '2021-05-05T17:32:18-04:00',
                             'des_facet': ['Attacks on Police',
                                           'Murders, Attempted Murders and Homicides'],
                             'first_published_date': '2021-05-05T17:32:18-04:00',
                             'geo_facet': ['Italy', 'Rome (Italy)', 'United States'],
                             'item_type': 'Article',
                             'kicker': '',
                             'material_type_facet': 'News',
                             'multimedia': [{'caption': 'Gabriel Natale Hjorth, left, and '
                                                        'Finnegan Elder on trial in Rome on '
                                                        'Wednesday.',
                                             'copyright': 'Tiziana Fabi/Agence France-Presse '
                                                          '— Getty Images',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05italy-trial/05italy-trial-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'Gabriel Natale Hjorth, left, and '
                                                        'Finnegan Elder on trial in Rome on '
                                                        'Wednesday.',
                                             'copyright': 'Tiziana Fabi/Agence France-Presse '
                                                          '— Getty Images',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05italy-trial/05italy-trial-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'Gabriel Natale Hjorth, left, and '
                                                        'Finnegan Elder on trial in Rome on '
                                                        'Wednesday.',
                                             'copyright': 'Tiziana Fabi/Agence France-Presse '
                                                          '— Getty Images',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05italy-trial/05italy-trial-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'Gabriel Natale Hjorth, left, and '
                                                        'Finnegan Elder on trial in Rome on '
                                                        'Wednesday.',
                                             'copyright': 'Tiziana Fabi/Agence France-Presse '
                                                          '— Getty Images',
                                             'format': 'Normal',
                                             'height': 116,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05italy-trial/merlin_187310877_243526c3-2640-4299-aed9-715616ebe739-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': None,
                             'per_facet': ['Elder, Finnegan Lee',
                                           'Hjorth, Gabriel Christian Natale',
                                           'Cerciello Rega, Mario',
                                           'Varriale, Andrea'],
                             'published_date': '2021-05-05T17:32:18-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '05italy-trial',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': 'Europe',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/05/world/05italy-trial/05italy-trial-thumbStandard.jpg',
                             'title': '2 Americans Sentenced to Life in Prison for Murder of '
                                      'Italian Police Officer',
                             'updated_date': '2021-05-05T20:04:34-04:00',
                             'url': 'https://www.nytimes.com/2021/05/05/world/europe/americans-murder-italian-police-officer.html'},
                            {'abstract': 'The secretary of state will reassure Kyiv of '
                                         'backing against Russian hostilities, but call for '
                                         'more determined efforts to clean up the political '
                                         'system.',
                             'byline': 'BY MICHAEL CROWLEY AND ANDREW E. KRAMER',
                             'created_date': '2021-05-05T16:48:36-04:00',
                             'des_facet': ['Trump-Ukraine Whistle-Blower Complaint and '
                                           'Impeachment Inquiry',
                                           'United States International Relations',
                                           'Corruption (Institutional)',
                                           'Politics and Government'],
                             'first_published_date': '2021-05-05T16:48:36-04:00',
                             'geo_facet': ['Ukraine', 'Russia'],
                             'item_type': 'Article',
                             'kicker': '',
                             'material_type_facet': 'News',
                             'multimedia': [{'caption': 'Secretary of State Antony J. Blinken '
                                                        'at a meeting in London on Wednesday.',
                                             'copyright': 'Pool photo by Hollie Adams',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05blinken/05blinken-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'Secretary of State Antony J. Blinken '
                                                        'at a meeting in London on Wednesday.',
                                             'copyright': 'Pool photo by Hollie Adams',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05blinken/merlin_187313778_2e42f446-7ee4-4bf9-b0be-dd8b5bf0aff2-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'Secretary of State Antony J. Blinken '
                                                        'at a meeting in London on Wednesday.',
                                             'copyright': 'Pool photo by Hollie Adams',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05blinken/merlin_187313778_2e42f446-7ee4-4bf9-b0be-dd8b5bf0aff2-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'Secretary of State Antony J. Blinken '
                                                        'at a meeting in London on Wednesday.',
                                             'copyright': 'Pool photo by Hollie Adams',
                                             'format': 'Normal',
                                             'height': 127,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05blinken/merlin_187313778_2e42f446-7ee4-4bf9-b0be-dd8b5bf0aff2-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': None,
                             'per_facet': ['Blinken, Antony J',
                                           'Zelensky, Volodymyr',
                                           'Nuland, Victoria J',
                                           'Trump, Donald J'],
                             'published_date': '2021-05-05T16:48:36-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '05ukraine-blinken',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': 'Europe',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/05/world/05blinken/05blinken-thumbStandard.jpg',
                             'title': 'Blinken, on Ukraine Trip, Will Offer Support on Russia '
                                      'but Also Pressure on Corruption',
                             'updated_date': '2021-05-06T04:48:54-04:00',
                             'url': 'https://www.nytimes.com/2021/05/05/world/europe/antony-blinken-ukraine-trip.html'},
                            {'abstract': 'The frightening surge of coronavirus cases in India '
                                         'has overwhelmed many hospitals in recent days, at '
                                         'times forcing staff members to provide medical '
                                         'treatment inside ambulances while patients wait for '
                                         'beds.',
                             'byline': 'BY REUTERS',
                             'created_date': '2021-05-05T16:03:07-04:00',
                             'des_facet': ['Coronavirus (2019-nCoV)',
                                           'Hospitals',
                                           'Medicine and Health'],
                             'first_published_date': '2021-05-05T16:03:07-04:00',
                             'geo_facet': ['India'],
                             'item_type': 'Video',
                             'kicker': '',
                             'material_type_facet': 'Video',
                             'multimedia': [{'caption': 'Lilaben Gautambhai Modi, 80, sitting '
                                                        'in an ambulance today as she waits '
                                                        'to enter a hospital for Covid-19 '
                                                        'treatment, in Ahmedabad, India.',
                                             'copyright': 'Amit Dave/Reuters',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/us/05-virus-briefing-india/05-virus-briefing-india-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'Lilaben Gautambhai Modi, 80, sitting '
                                                        'in an ambulance today as she waits '
                                                        'to enter a hospital for Covid-19 '
                                                        'treatment, in Ahmedabad, India.',
                                             'copyright': 'Amit Dave/Reuters',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/us/05-virus-briefing-india/05-virus-briefing-india-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'Lilaben Gautambhai Modi, 80, sitting '
                                                        'in an ambulance today as she waits '
                                                        'to enter a hospital for Covid-19 '
                                                        'treatment, in Ahmedabad, India.',
                                             'copyright': 'Amit Dave/Reuters',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/us/05-virus-briefing-india/05-virus-briefing-india-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'Lilaben Gautambhai Modi, 80, sitting '
                                                        'in an ambulance today as she waits '
                                                        'to enter a hospital for Covid-19 '
                                                        'treatment, in Ahmedabad, India.',
                                             'copyright': 'Amit Dave/Reuters',
                                             'format': 'Normal',
                                             'height': 134,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/us/05-virus-briefing-india/merlin_187309602_1d687c2c-1bce-4f81-87b4-1b5910547f44-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': None,
                             'per_facet': None,
                             'published_date': '2021-05-05T16:03:07-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '05vid-india',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': 'Asia Pacific',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/05/us/05-virus-briefing-india/05-virus-briefing-india-thumbStandard.jpg',
                             'title': 'India’s Coronavirus Crisis Overwhelms Health System',
                             'updated_date': '2021-05-05T16:03:07-04:00',
                             'url': 'https://www.nytimes.com/video/world/asia/100000007747304/india-coronavirus-healthcare.html'},
                            {'abstract': 'Clinical trials showed that the vaccine, '
                                         'codeveloped with BioNTech, was safe for 12- to '
                                         '15-year-olds, Canada’s regulatory agency said.',
                             'byline': 'BY IAN AUSTEN, AUSTIN RAMZY, ISABELLA KWAI AND YAN '
                                       'ZHUANG',
                             'created_date': '2021-05-05T15:08:03-04:00',
                             'des_facet': ['internal-essential'],
                             'first_published_date': '2021-05-05T15:08:03-04:00',
                             'geo_facet': None,
                             'item_type': 'Article',
                             'kicker': 'Global Roundup',
                             'material_type_facet': 'Live Blog Post',
                             'multimedia': [{'caption': 'Health care workers administering '
                                                        'the Pfizer-BioNTech vaccine at a '
                                                        'Sikh house of worship in '
                                                        'Mississauga, Ontario.',
                                             'copyright': 'Carlos Osorio/Reuters',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/us/05-virus-briefing-global-roundup/05-virus-briefing-global-roundup-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'Health care workers administering '
                                                        'the Pfizer-BioNTech vaccine at a '
                                                        'Sikh house of worship in '
                                                        'Mississauga, Ontario.',
                                             'copyright': 'Carlos Osorio/Reuters',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/us/05-virus-briefing-global-roundup/05-virus-briefing-global-roundup-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'Health care workers administering '
                                                        'the Pfizer-BioNTech vaccine at a '
                                                        'Sikh house of worship in '
                                                        'Mississauga, Ontario.',
                                             'copyright': 'Carlos Osorio/Reuters',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/us/05-virus-briefing-global-roundup/05-virus-briefing-global-roundup-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'Health care workers administering '
                                                        'the Pfizer-BioNTech vaccine at a '
                                                        'Sikh house of worship in '
                                                        'Mississauga, Ontario.',
                                             'copyright': 'Carlos Osorio/Reuters',
                                             'format': 'Normal',
                                             'height': 127,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/us/05-virus-briefing-global-roundup/05-virus-briefing-global-roundup-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': None,
                             'per_facet': None,
                             'published_date': '2021-05-05T15:08:03-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '05-virus-briefing-global-roundup',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': '',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/05/us/05-virus-briefing-global-roundup/05-virus-briefing-global-roundup-thumbStandard.jpg',
                             'title': 'Canada authorizes Pfizer’s vaccine for adolescents, '
                                      'but shots won’t begin immediately.',
                             'updated_date': '2021-05-06T01:35:18-04:00',
                             'url': 'https://www.nytimes.com/live/2021/05/05/world/covid-vaccine-coronavirus-cases/canada-authorizes-pfizers-vaccine-for-adolescents-but-shots-wont-begin-immediately'},
                            {'abstract': 'Isabel Díaz Ayuso, a conservative politician dubbed '
                                         'a “Trumpista” by her opponents, won the Madrid '
                                         'regional election by a landslide after she refused '
                                         'to shut down the capital’s bars and shops.',
                             'byline': 'BY RAPHAEL MINDER',
                             'created_date': '2021-05-05T14:44:25-04:00',
                             'des_facet': ['Elections',
                                           'Politics and Government',
                                           'Coronavirus (2019-nCoV)',
                                           'Quarantines',
                                           'Content Type: Personal Profile'],
                             'first_published_date': '2021-05-05T14:44:25-04:00',
                             'geo_facet': ['Madrid (Spain)', 'Spain'],
                             'item_type': 'Article',
                             'kicker': '',
                             'material_type_facet': 'News',
                             'multimedia': [{'caption': 'Isabel Díaz Ayuso waving to '
                                                        'celebrating supporters from the '
                                                        'party’s headquarters in Madrid on '
                                                        'Tuesday evening.\xa0',
                                             'copyright': 'Bernat Armangue/Associated Press',
                                             'format': 'Standard Thumbnail',
                                             'height': 75,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05spain01/05spain01-thumbStandard.jpg',
                                             'width': 75},
                                            {'caption': 'Isabel Díaz Ayuso waving to '
                                                        'celebrating supporters from the '
                                                        'party’s headquarters in Madrid on '
                                                        'Tuesday evening.\xa0',
                                             'copyright': 'Bernat Armangue/Associated Press',
                                             'format': 'mediumThreeByTwo210',
                                             'height': 140,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05spain01/merlin_187293933_23ab8650-f9a4-4108-93e7-fab98053bf89-mediumThreeByTwo210.jpg',
                                             'width': 210},
                                            {'caption': 'Isabel Díaz Ayuso waving to '
                                                        'celebrating supporters from the '
                                                        'party’s headquarters in Madrid on '
                                                        'Tuesday evening.\xa0',
                                             'copyright': 'Bernat Armangue/Associated Press',
                                             'format': 'mediumThreeByTwo440',
                                             'height': 293,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05spain01/merlin_187293933_23ab8650-f9a4-4108-93e7-fab98053bf89-mediumThreeByTwo440.jpg',
                                             'width': 440},
                                            {'caption': 'Isabel Díaz Ayuso waving to '
                                                        'celebrating supporters from the '
                                                        'party’s headquarters in Madrid on '
                                                        'Tuesday evening.\xa0',
                                             'copyright': 'Bernat Armangue/Associated Press',
                                             'format': 'Normal',
                                             'height': 127,
                                             'subtype': 'photo',
                                             'type': 'image',
                                             'url': 'https://static01.nyt.com/images/2021/05/05/world/05spain01/merlin_187293933_23ab8650-f9a4-4108-93e7-fab98053bf89-articleInline.jpg',
                                             'width': 190}],
                             'org_facet': ['Popular Party (Spain)',
                                           'Vox (Spanish Political Party)'],
                             'per_facet': ['Ayuso, Isabel Diaz',
                                           'Sanchez Perez-Castejon, Pedro (1972- )'],
                             'published_date': '2021-05-05T14:44:25-04:00',
                             'related_urls': None,
                             'section': 'World',
                             'slug_name': '05spain',
                             'source': 'New York Times',
                             'subheadline': '',
                             'subsection': 'Europe',
                             'thumbnail_standard': 'https://static01.nyt.com/images/2021/05/05/world/05spain01/05spain01-thumbStandard.jpg',
                             'title': 'She Kept Madrid Open in the Pandemic. Voters Rewarded '
                                      'Her.',
                             'updated_date': '2021-05-06T04:52:59-04:00',
                             'url': 'https://www.nytimes.com/2021/05/05/world/europe/spain-election-madrid-isabel-diaz-ayuso.html'}],
                'status': 'OK'}

Process finished with exit code 0

"""