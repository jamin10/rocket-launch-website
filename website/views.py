from re import L
from unicodedata import category
from flask import Blueprint, render_template, request, jsonify, flash
from flask_login import login_required, current_user
import json
import requests
from .models import Launch, User
from .helpers import *
from . import db
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/upcoming-launches', methods=["GET", "POST"])
@login_required
def upcoming_launches():

    if request.method == 'POST':

        # Base url 
        url = "https://lldev.thespacedevs.com/2.2.0/launch/upcoming/?format=json"

        # Offset for which results to show on page 
        offset = request.form.get("offset")
        if offset == None:
            offset = 0
        else:
            pass

        # Adjust URL for API request 
        url = url + "&limit=10&offset=" + offset
        launches_info = get_launches_info(url)

        return render_template("upcoming-launches.html", user=current_user, launches_info=launches_info)

    else:

        launches_info = get_launches_info("https://lldev.thespacedevs.com/2.2.0/launch/upcoming/?format=json")

        return render_template("upcoming-launches.html", user=current_user, launches_info=launches_info)


@views.route('/past-launches', methods=["GET", "POST"])
@login_required
def past_launches():

    if request.method == 'POST':

        # Base url 
        url = "https://lldev.thespacedevs.com/2.2.0/launch/?format=json"

        # Offset for which results to show on page 
        offset = request.form.get("offset")
        if offset == None:
            offset = 0
        else:
            pass

        # Adjust URL for API request 
        url = url + "&limit=10&offset=" + offset
        launches_info = get_launches_info(url)

        return render_template("past-launches.html", user=current_user, launches_info=launches_info)

    else:

        launches_info = get_launches_info("https://lldev.thespacedevs.com/2.2.0/launch/?format=json")

        return render_template("past-launches.html", user=current_user, launches_info=launches_info)


@views.route('/bookmarked-upcoming')
@login_required
def bookmarked_upcoming():

    now = datetime.now()
    print(now)
    # Order launches by window start time 
    ordered_launches = Launch.query.filter((Launch.user_id==current_user.id), (Launch.window_start>now)).order_by(Launch.window_start)

    return render_template("bookmarked-upcoming.html", user=current_user, launches=ordered_launches)


@views.route('/bookmarked-past')
@login_required
def bookmarked_past():

    now = datetime.now()
    print(now)
    # Order launches by window start time 
    ordered_launches = Launch.query.filter((Launch.user_id==current_user.id), (Launch.window_start<now)).order_by(Launch.window_start)

    return render_template("bookmarked-past.html", user=current_user, launches=ordered_launches)


@views.route('/bookmark-launch', methods=['POST'])
def bookmark_launch():
    # Get data from button click 
    launch = json.loads(request.data)
    launchSlug = launch['slug']

    # Check if already bookmarked 
    launch = Launch.query.get(launchSlug)
    if launch:
        if launch.user_id == current_user.id:
            flash('Launch already bookmarked!', category='error')
            return jsonify({})

    # Search API with slug to retrieve data to be stored in database 
    url = "https://lldev.thespacedevs.com/2.2.0/launch/?format=json" + f"&slug={launchSlug}"
    launches_info = get_launches_info(url)
    info = launches_info[0]
    
    # Add data to database 
    new_bookmark = Launch(slug=launchSlug, name=info["name"], lsp_name=info['lsp_name'], rocket_name=info['rocket_name'], \
        location_name=info['location_name'], image=info['image'], window_start=info['window_start'], user_id=current_user.id)
    db.session.add(new_bookmark)
    db.session.commit()
    flash('Launch bookmarked!', category='success')

    # Return empty response 
    return jsonify({})


@views.route('/delete-launch', methods=['POST'])
def delete_launch():
    # Get data from button click 
    launch = json.loads(request.data)
    launchSlug = launch['slug']

    # Check if in database and remove 
    launch = Launch.query.get(launchSlug)
    if launch:
        if launch.user_id == current_user.id:
            db.session.delete(launch)
            db.session.commit()
            flash('Bookmark deleted!', category='success')

    return jsonify({})