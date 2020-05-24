import os

from flask import Flask, jsonify
from api.bangladesh import *
from api.dhaka import *


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_envvar('SETTINGS')

    @app.route('/district')
    def district_route():
        return jsonify(bangladesh.scrape_districts())

    @app.route('/dhaka')
    def dhaka_route():
        return jsonify(dhaka.scrape_dhaka_area())

    return app
