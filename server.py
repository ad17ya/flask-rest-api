# Implementing a REST API with Python and Flask

from telnetlib import STATUS
from flask import Flask, url_for
from flask import request
from flask import json
from flask import Response
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def api_root():
    return "Welcome"

@app.route('/articles')
def api_articles():
    return "List of " + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return "You are reading " + articleid

@app.route('/hello')
def api_hello():
    data  = {
        'hello' : 'world',
        'number' : 3
    }

    js = json.dumps(data)

    resp = jsonify(data)
    resp.status_code = 200
    resp.headers['Link'] = 'http://luisrei.com'

    return resp

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return 'GET'
    elif request.method == 'POST':
        return 'POST'
    elif request.method == 'PATCH':
        return 'PATCH'
    elif request.method == 'PUT':
        return 'PUT'
    elif request.method == 'DELETE':
        return 'DELETE'

@app.route('/messages', methods=['POST'])
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    
    elif request.headers['Content-Type'] == 'application/octet-stream':
        print("here")
        f = open('./write_binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status' : 404,
        'message' : 'Not Found: ' + request.url,
    }

    resp = jsonify(message)
    resp.status_code = 404
    return resp

@app.route('/users/<userid>', methods=['GET'])
def api_users(userid):
    users = {'1':'john', '2':'steve', '3':'bill'}

    if userid in users:
        return jsonify({userid: users[userid]})
    else:
        return not_found()

if __name__ == '__main__':
    app.run()
