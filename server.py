# Implementing a REST API with Python and Flask

from flask import Flask, url_for
from flask import request
from flask import json

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
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello Anon'

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
    try:
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

    except Exception as err:
        print(err)

if __name__ == '__main__':
    app.run()