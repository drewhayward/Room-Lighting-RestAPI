# Must import LightCtrl
from app import app
from app import LightCtrl
from flask import abort
from flask import request
from flask import make_response
from flask import jsonify
import re
import os
import binascii
import time

tokens = [];

colorFormat = re.compile('^#?[a-f0-9]{6}$');

# Checks if a given token is valid
def checkToken(check):
    for i in range(len(tokens)):
        token, issue = tokens[i]
        if(check == token):
            # Check if the token was issued in the past day
            if(abs(issue - time.time()) < 86400):
                return True
            # Remove the token if it is expired
            else:
                del tokens[i]
                return False
    return False


@app.route('/api/token/', methods=['GET'])
def getToken():
    if 'password' not in request.headers:
        about(400)

    if request.headers['password'] == "Lightsablazing":
        token = binascii.hexlify(os.urandom(10))
        tokens.append((token,time.time()))
        return make_response(jsonify({'token': token}),200)
    else:
        return make_response('Invalid Password', 401)


@app.route('/api/strip/', methods=['POST'])
def stripColor():
    # Authorization check
    if 'token' not in request.headers:
        abort(400)
    if not checkToken(request.headers['token']):
        return make_response('Invalid token', 401)

    # Parameter check
    if not request.json or not 'color' in request.json or not 'strip' in request.json:
        abort(400)

    strip = request.json.get('strip')
    color = request.json.get('color')

    # Parameter validity check
    if colorFormat.match(color) is None:
        abort(400)
    if strip not in LightCtrl.stripmap.keys():
        abort(400)

    LightCtrl.setStripColor(strip, color)

    return make_response('',200)


@app.route('/api/light/', methods=['POST'])
def setLight():
    # Authorization check
    if 'token' not in request.headers:
        abort(400)
    if not checkToken(request.headers['token']):
        return make_response('Invalid token', 401)

    # Parameter check
    if not request.json or not 'light' in request.json or not 'state' in request.json:
        abort(400)

    light = request.json.get('light')
    state = request.json.get('state')

    # Parmeter validity check
    if light not in LightCtrl.lightmap.keys():
        abort(400)

    LightCtrl.setLightState(request.json.get('light'), request.json.get('state'));

    return make_response('',200)


@app.route('/api/state/', methods=['GET'])
def get_state():
    # Authorization check
    if 'token' not in request.headers:
        abort(400)
    if not checkToken(request.headers['token']):
        return make_response('Invalid token', 401)

    state = LightCtrl.getState()

    return make_response(jsonify(state),200)


@app.errorhandler(404)
def not_found(error):
    return make_response('The requested resource doesn\'t exist',404)


@app.errorhandler(400)
def bad_request(error):
    return make_response('The request is not formatted correctly', 400)
