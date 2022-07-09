# python version 3.9.12 env: equake_env
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, MetaData, inspect, Table

from flask import Flask, jsonify, render_template
from flask import url_for
import json


# #################################################
# # Flask Setup
# #################################################
app = Flask(__name__, static_url_path='/static/')

# #################################################
# # Flask Routes
# #################################################
# with open('Database/json/earthquake.json', 'r') as myfile:
#     data = myfile.read()

@app.route("/")
def welcome():
    # """List all available api routes."""
    return render_template('index.html')

@app.route("/yvaine")
def page1():
    # """List all available api routes."""
    return render_template('yvaine.html')

@app.route("/resume")
def page2():
    # """List all available api routes."""
    return render_template('resume.html')

@app.route("/portfolio")
def page3():
    # """List all available api routes."""
    return render_template('portfolio.html')


if __name__ == '__main__':
    app.run(debug=True)