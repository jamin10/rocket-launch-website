import requests
from datetime import datetime


def get_launches_info(url):
    response = requests.get(url)
    launches = response.json()
    results = launches['results']

    launches_info = []

    for result in results:

        info = {}

        info['slug'] = result["slug"]
        info['url'] = result["url"]
        info['name'] = result["name"]
        info['lsp_name'] = result['launch_service_provider']['name']
        info['rocket_name'] = result['rocket']['configuration']['name']
        info['location_name'] = result['pad']['name']
        info['image'] = result['image']
        info['window_start'] = change_to_datetime_object(result['window_start'])

        launches_info.append(info)

    return launches_info


def change_to_datetime_object(date_and_time):

    datetime_format = date_and_time[:-1].replace('T', ' ')
    date_time_obj = datetime.strptime(datetime_format, '%Y-%m-%d %H:%M:%S')

    return date_time_obj


def get_space_news(url):
    response = requests.get(url)
    news = response.json()

    return news



