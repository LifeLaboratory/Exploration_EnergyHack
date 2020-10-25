# coding=utf-8
import os
import sys
import flask
from flask_restful import Api
from route_list import ROUTES
import io
from base.base_name import CORS_HEADERS
from PC_report import generate_pc_report
from LEP_report import generate_lep_report

sys.path.append(os.getcwd()+'/../')
sys.path.append(os.getcwd()+'../')

_app = flask.Flask(__name__, static_folder="static")
_app.config['JSON_AS_ASCII'] = False
api = Api(_app)
HEADER = {'Access-Control-Allow-Origin': '*'}
_app.jinja_env.auto_reload = True
_app.config['TEMPLATES_AUTO_RELOAD'] = True


@_app.errorhandler(404)
def not_found(error):
    return {'error': 'Not found'}, 404


# '/api/pc_report/<int:id_company>': PCReport,
@_app.route('/api/pc_report/<int:id_company>')
def pc_report(id_company):
    generate_pc_report(id_company)
    """Serves the logo image."""
    with open("static/Отчет_ПС_new.xlsx", 'rb') as bites:
        return flask.send_file(
                     io.BytesIO(bites.read()),
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        ), CORS_HEADERS

# '/api/lep_report/<int:id_company>': LEPReport,

@_app.route('/api/lep_report/<int:id_company>')
def lep_report(id_company):
    generate_lep_report(id_company)
    """Serves the logo image."""
    with open("static/Отчет_ЛЭП_new.xlsx", 'rb') as bites:
        return flask.send_file(
                     io.BytesIO(bites.read()),
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        ), CORS_HEADERS



if __name__ == '__main__':
    try:
        for route, route_class in ROUTES.items():
            api.add_resource(route_class, route)
        _app.run(host='0.0.0.0', port=13451, threaded=True)
    except Exception as e:
        print('Main except = ', e)
