from flask import Flask, request, render_template, jsonify, redirect
from db import *
import json

app = Flask(__name__)


@app.route("/api")
def get_data_list():
    try:
        db = DB()
        data = db.select_from_db()
        db.__disconnect__()
        return jsonify(data)
    except:
        return 'error'


@app.route("/")
def home():
    return 'ok'
