from . import db
from flask import render_template, Blueprint
from flask_login import current_user


routes = Blueprint("routes", __name__)

@routes.route('/home')
def home():
    return render_template("home.html", user = current_user)

@routes.route('/buy_creatine')
def creatine():
    return render_template("creatine.html", user = current_user)

@routes.route('/buy_dumbbells')
def dumbbells():
    return render_template("dumbbells.html", user = current_user)

@routes.route('/buy_gloves')
def gloves():
    return render_template("boxing_gloves.html", user = current_user)

@routes.route('/buy_shirt')
def shirt():
    return render_template("shirt.html", user = current_user)

@routes.route('/buy_whey')
def whey():
    return render_template("whey.html", user = current_user)

@routes.route('/buy_drink')
def drink():
    return render_template("drink.html", user = current_user)