from flask import Flask, jsonify
from api.bangladesh import *
from api.dhaka import *

def create_app(test_config=None):
    app = Flask('__api__', instance_relative_config=True)
    # app.config.from_envvar('SETTINGS')
    app.config['JSON_AS_ASCII'] = False


    @app.route('/district')
    def district_route():
        district_confirm_dict = getDistrictConfirmDict()
        return jsonify(bangladesh.scrape_districts(district_confirm_dict))

    @app.route('/dhaka')
    def dhaka_route():
        return jsonify(dhaka.scrape_dhaka_area())

    @app.route('/district/csv')
    def district_csv_route():
        district_confirm_dict = getDistrictConfirmDict()
        return jsonify(getDistrictCsvJson(district_confirm_dict))


    @app.route('/district/dict')
    def district_confirmed_dict_route():
        district_confirm_dict = getDistrictConfirmDict()
        return jsonify(district_confirm_dict)

    return app


if __name__ == "__main__":
        app = create_app()
        app.run()
