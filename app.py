
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__, static_folder='./build', static_url_path='/')


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return app.send_static_file('index.html')



@app.route('/hello')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return [{'name': 'Sola Jegede','location':'Texas'},{'name':'Ope Jegede','location':'British Columbia'}]

@app.route('/home')
def home():
    return {'home': 'Where the heart is.'}
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()



    app = Flask(__name__, static_folder='../build', static_url_path='/')
