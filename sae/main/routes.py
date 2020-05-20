from flask import render_template, request, redirect, url_for,  Blueprint
from flask_login import current_user
from sae.models import Character, User
from flask_login import login_user, current_user, logout_user, login_required, login_manager

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    if not current_user.is_authenticated:
        return redirect(url_for("users.login"))
    else:
        user = current_user
        characters = Character.query.filter_by(author=user).order_by(Character.level.desc())
        return render_template("home.html", user=user, characters=characters)
