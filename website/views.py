from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/upcoming-launches')
@login_required
def upcoming_launches():
    return render_template("upcoming-launches.html", user=current_user)


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

