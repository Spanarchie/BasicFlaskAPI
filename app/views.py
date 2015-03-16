from app import app

__author__ = 'colinmoore-hill'

from flask import render_template, flash, redirect, session, url_for, request, g

from .models import Player



@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@app.route('/')
def index():
    user = "Fred"
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           user=user,
                           posts=posts)

@app.route('/players')
def player():
    pass







