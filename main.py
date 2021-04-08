from flask import Flask, request, render_template, jsonify, redirect
from db import *
from urllib import parse
import json

app = Flask(__name__)


@app.route('/api/', defaults={'groups': None})
@app.route("/api/<groups>")
def get_data_list(groups):
    try:
        db = DB()
        groups = parse.unquote_plus(groups)
        data = db.select_from_db(groups)
        return jsonify(data)
    except:
        return 'error'


@app.route("/")
def home():
    return 'ok'
