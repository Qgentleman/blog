from flask import Flask
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return 'index'

@app.before_first_request
def before_first_request():
    print('before')

@app.before_request
def before_request():
    print('before_request')

@app.after_request
def after_request():
    print('after_request')


@app.teardown_request
def teardown_request():
    print('teardown')

if __name__ == 'main':
    manager.run()