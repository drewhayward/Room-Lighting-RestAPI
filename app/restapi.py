# Must import LightCtrl
from app import app
from flask import abort
from flask import request
from flask import make_response
from flask import jsonify
import os
import binascii
import time

tokens = [];

def checkToken(check):
    for token, issue in tokens:
        if(check == token and abs(issue - time.time()) < 86400):
            return True
        else:
            return False
    return False

@app.route('/api/token/', methods=['GET'])
def getToken():
    if 'password' not in request.headers:
        about(400)

    if request.headers['password'] == "deadbeef":
        token = binascii.hexlify(os.urandom(10))
        tokens.append((token,time.time()))
        return make_response(jsonify({'token': token}),200)
    else:
        return make_response('Invalid Password', 401)



@app.route('/api/strip/', methods=['POST'])
def stripColor():
    if 'token' not in request.headers:
        abort(400)
    if not checkToken(request.headers['token']):
        return make_response('Invalid token', 401)
    if not request.json or not 'color' in request.json or not 'strip' in request.json:
        abort(400)
    #TODO Check for valid colors
    print(request.json.get('strip'))
    print(request.json.get('color'))
    return make_response('',200)


@app.route('/api/light/', methods=['POST'])
def setLight():
    if 'token' not in request.headers:
        abort(400)
    if not checkToken(request.headers['token']):
        return make_response('Invalid token', 401)

    if not request.json or not 'light' in request.json or not 'state' in request.json:
        abort(400)
    #TODO pass to light controller
    print(request.json.get('light'))
    print(request.json.get('state'))
    return make_response('',200)

@app.route('/api/state/', methods=['GET'])
def get_state():
    if 'token' not in request.headers:
        abort(400)
    if not checkToken(request.headers['token']):
        return make_response('Invalid token', 401)

    return make_response('',200)

@app.errorhandler(404)
def not_found(error):
    return make_response('The requested resource doesn\'t exist',404)


@app.errorhandler(400)
def bad_request(error):
    return make_response('The request is not formatted correctly', 400)
