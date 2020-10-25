from flask import Flask
from flask import request
from flask import render_template
import json

import src.user_classifier as uc
import src.user_types as ut
from src.feature_deduction import deds, BROKERAGE, INVEST

app = Flask(__name__)

current_request = ut.UserData(ut.YOUNG, "", ut.SEARCH_ENGINE, ut.SINGLE, ut.AVERAGE, ut.INC_70_130)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        age = int(request.args.get('age_group'))
        interests = request.args.get('interests')
        source = int(request.args.get('source'))
        family = int(request.args.get('family'))
        education = int(request.args.get('education'))
        income = int(request.args.get('income'))
        
        global current_request
        current_request = ut.UserData(age, interests, source, family, education, income)

        return render_template('index.html')


         

@app.route('/view/rule', methods=['GET'])
def view_add_rule():
    return render_template('rules.html')

@app.route('/set/rule', methods=['POST'])
def add_new_rule():
    category = request.form['category']
    rule = request.form['rule']
    data = {'rule' : rule, 'category' : category}
    
    if category == 'YOUNG':
        req_cat = ut.YOUNG
    if 'ACCOUNT' in rule:
        if 'BROKER' in rule:
            req_value = BROKERAGE
        else:
            req_value = INVEST

    deds['account_type'].add_rule(lambda x: x.age == req_cat, req_value)
    return render_template('rules.html')

@app.route('/get/data', methods=['GET'])
def get_frontend_data():
    intermediate_repr = uc.get_intermediate_representation(current_request)    
    json_data = uc.get_page_json(intermediate_repr)
    print(json_data)
    return json_data

    

