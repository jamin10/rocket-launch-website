from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import requests

#from website.helpers import get_launches_info



views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/upcoming-launches', methods=["GET", "POST"])
@login_required
def upcoming_launches():

    if request.method == 'POST':

        url = "https://lldev.thespacedevs.com/2.2.0/launch/upcoming/?format=json"

        offset = request.form.get("offset")
        if offset == None:
            offset = 0
        else:
            pass

        url = url + "&limit=10&offset=" + offset
        print(url)

        launches_info = get_launches_info(url)

        return render_template("upcoming-launches.html", user=current_user, launches_info=launches_info)

    else:

        launches_info = get_launches_info("https://lldev.thespacedevs.com/2.2.0/launch/upcoming/?format=json")

        return render_template("upcoming-launches.html", user=current_user, launches_info=launches_info)


@views.route('/past-launches')
@login_required
def past_launches():
    return render_template("past-launches.html", user=current_user)


@views.route('/bookmarked-upcoming')
@login_required
def bookmarked_upcoming():
    return render_template("bookmarked-upcoming.html", user=current_user)


@views.route('/bookmarked-past')
@login_required
def bookmarked_past():
    return render_template("bookmarked-past.html", user=current_user)


# Functions 
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

        launches_info.append(info)

    return launches_info