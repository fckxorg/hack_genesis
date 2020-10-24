from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    age = request.args.get('age')
    sex = request.args.get('sex')

    if sex == 'f':
        return 'I am the index page for ' + age + ' years old women'
    return 'I am the index page for ' + age + ' years old men'
