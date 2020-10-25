from flask import Flask
from flask import request
from flask import render_template
import json

import src.user_classifier as uc
import src.user_types as ut

app = Flask(__name__)

current_request = ut.UserData(ut.YOUNG, "", ut.SEARCH_ENGINE, ut.SINGLE, ut.AVERAGE, ut.INC_70_130)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        age = int(request.args.get('age_group'))
        interests = request.args.get('interests')
        source = bool(request.args.get('source'))
        family = bool(request.args.get('family'))
        education = int(request.args.get('education'))
        income = int(request.args.get('income'))

        current_request = ut.UserData(age, interests, source, family, education, income)

        return render_template('index.html')


         


@app.route('/add', methods=['POST'])
def add_new_category():
    data = json.loads(request.data)

@app.route('/get/data', methods=['GET'])
def get_frontend_data():
    pass

    

