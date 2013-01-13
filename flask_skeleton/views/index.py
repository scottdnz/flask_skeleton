#!/usr/bin/env python
#-*- coding: utf-8 -*-


"""
.. module:: index
.. moduleauthor:: Scott Davies <scottdnz@hotmail.co.nz>

This module contains functions to render a web page. 
"""


from flask import (Blueprint, request, render_template)

#from flask_skeleton.config import app


index = Blueprint("index", __name__)
    
@index.route("/", methods=["GET"])
def index_fn():
    """ A page view. Returns a template for ...
    """
    page_title = "Index"
    
    if request.method == "GET":
        return render_template("index.html",
                                pg_title=page_title,
                                )

#    elif request.method == "POST":
#        if request.form.has_key(""):
#           val = request.form[""]

