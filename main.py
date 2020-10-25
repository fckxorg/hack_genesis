from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        age = request.args.get('age')
        sex = request.args.get('sex')

        if sex == 'f':
            return 'I am the index page for ' + age + ' years old women'
        return 'I am the index page for ' + age + ' years old men'
    
    if request.method == 'POST':
        pass


@app.route('/add', methods=['POST'])
def add_new_category():
    data = json.loads(request.data)
    

