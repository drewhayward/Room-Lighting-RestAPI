# Must import LightCtrl
from app import app
from flask import abort
from flask import request
from flask import make_response
from flask import jsonify

@app.route('/api/strip/', methods=['POST'])
def stripColor():

    if not request.json or not 'color' in request.json or not 'strip' in request.json:
        abort(400)
    #TODO Check for valid colors
    print(request.json.get('strip'))
    print(request.json.get('color'))
    return make_response('',200)


@app.route('/api/light/', methods=['POST'])
def setLight():
    if not request.json or not 'light' in request.json or not 'state' in request.json:
        abort(400)
    #TODO pass to light controller
    print(request.json.get('light'))
    print(request.json.get('state'))
    return make_response('',200)

@app.route('/api/state', methods=['GET'])
def get_state():

    return make_response('',200)

@app.errorhandler(404)
def not_found(error):
    return make_response('The requested resource doesn\'t exist',404)


@app.errorhandler(400)
def bad_request(error):
    return make_response('The request is not formatted correctly', 400)
