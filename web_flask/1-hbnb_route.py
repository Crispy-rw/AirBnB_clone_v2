#!/usr/bin/python3
from flask import Flask
''' Flask application'''


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def holberton():
    '''hello holberton'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''Display HBNB'''
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
