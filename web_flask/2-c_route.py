from flask import Flask
''' Flask application'''


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def holberton():
    '''hello holberton'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Display HBNB'''
    return 'HBNB'


@app.route('/c/<text>')
def ctext(text):
    ''' C '''
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
