from flask import Flask, jsonify, abort
from setup_params_route import get_param_convert
from db import *
import json

app = Flask(__name__)


@app.route("/api/")
@app.route("/api")
def get_data_list():
    data_filter = get_param_convert()
    try:
        db = DB()
        data = db.select_from_db(data_filter)
    except:
        return 'error'
    return jsonify(data)


@app.route("/")
def home():
    return 'bienvenue sur le back-end'


@app.errorhandler(404)
def data_not_found(e):
    return 'data not found'
