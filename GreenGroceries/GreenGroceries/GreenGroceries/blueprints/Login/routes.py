from flask import render_template, url_for, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user

from GreenGroceries.models import Farmer, Customer
from GreenGroceries.queries import get_user_by_user_name, insert_farmer, insert_customer
from GreenGroceries.utils.choices import UserTypeChoices

Login = Blueprint('Login', __name__)


@Login.route("/")
@Login.route("/home")
def home():
    return render_template('pages/home.html')


@Login.route("/about")
def about():
    return render_template('pages/about.html')


@Login.route("/style-guide")
def style_guide():
    return render_template('pages/style-guide.html')





