from flask import Blueprint, render_template, redirect, url_for
from flask import request
import requests
from website import db
from .models import User, Task
from flask_login import login_required, current_user
import os

# Create a blueprint
main_blueprint = Blueprint('main', __name__)

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

@main_blueprint.route('/', methods=['GET'])
# @login_required
def main_page():

    articles = []

    url = ('https://newsapi.org/v2/everything?'
            'q=DeepSeek&'
            #    'from=2025-02-07&'
            'sortBy=popularity&'
            'apiKey=' + NEWS_API_KEY
            )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        articles = data['articles']

    
    return render_template('dashboard.html', articles=articles)
    