#!/usr/bin/env python
#-*- coding: utf-8 -*-


"""
    flask_skeleton.config
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    This module contains a function that creates a Flask application for the 
    project and configures a custom logger. It also imports the web page view
    modules, then registers these views for the application.
"""


from flask import Flask


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")
    return app


app = create_app()


@app.before_request
def before_request():
    """ """
    # Connect to DB.
    pass


@app.teardown_request
def teardown_request(exception=None):
    """ """
    # Disconnect from DB.
    pass
    

from views.index import index
from views.test1 import test1

blueprints = (index, test1)
[app.register_blueprint(bp) for bp in blueprints]
