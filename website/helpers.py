import requests

search = "SpaceX"
url = f"https://ll.thespacedevs.com/2.2.0/launch/upcoming/?format=json"

def get_launches_info(url):
    response = requests.get(url)
    launches = response.json()
    results = launches['results']

    launches_info = []

    for result in results:

        info = {}

        info['id'] = result["id"]
        info['url'] = result["url"]
        info['name'] = result["name"]
        info['lsp_name'] = result['launch_service_provider']['name']
        info['rocket_name'] = result['rocket']['configuration']['name']
        info['location_name'] = result['pad']['name']
        info['image'] = result['image']
        info['window_start'] = result['window_start']
        #info['next'] = result['next']
        #info['previous'] = result['previous']

        launches_info.append(info)

    #print(launches)

get_launches_info("https://ll.thespacedevs.com/2.2.0/launch/upcoming/?format=json")