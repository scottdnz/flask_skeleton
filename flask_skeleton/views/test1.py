#!/usr/bin/env python
#-*- coding: utf-8 -*-


"""
.. module:: test1
.. moduleauthor:: Scott Davies <scottdnz@hotmail.co.nz>

This module contains functions to render a web page. 
"""


from flask import (Blueprint, request, render_template)

#from flask_skeleton.config import app


test1 = Blueprint("test1", __name__)
    
@test1.route("/test1", methods=["GET"])
def test1_fn():
    """ A page view. Returns a template for ...
    """
    page_title = "Test1"
    
    if request.method == "GET":
        return render_template("test1.html",
                                pg_title=page_title,
                                )

#    elif request.method == "POST":
#        if request.form.has_key(""):
#           val = request.form[""]

