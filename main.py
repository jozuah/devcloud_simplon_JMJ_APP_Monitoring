from flask import Flask, request, render_template, jsonify, redirect, url_for
from db import *
import json
import time
# import urllib.parse

app = Flask(__name__)


@app.route("/api")
def get_data_list():
    groups = request.args.get('groups') if request.args.get(
        'groups') else None
    if groups == None:
        return redirect(url_for('data_not_found'))
    else:
        try:
            db = DB()
            # groups = urllib.parse.unquote_plus(groups)
            # print(groups)
            groups = groups.replace('%20', ' ')
            print(groups)
            data = db.select_from_db(groups)
        except:
            return 'error'
    return jsonify(data)


@app.route("/all_data")
def get_all_data():
    try:
        db = DB()
        data = db.select_all()
        return jsonify(data)
    except:
        return 'error'


@app.route("/")
def home():
    return 'bienvenue sur le back-end'


@app.errorhandler(404)
def data_not_found(e):
    return 'data not found'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
