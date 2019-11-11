from app import app
from app.controls import person_control as control
from app.utils import helper
from flask import request
@app.route('/')
def hello():
    return 'Welcome!'

@app.route('/getAllPersons')
def get_all_persons():
    try:
        data = control.getAllPersons()
        return helper.json_return(200, True, {'persons':data}, None)
    except Exception as e:
        print(e)
        error_return = helper.json_return(600, False, None, ['Có lỗi ngoại lệ:{0}'.format(str(e.args[1]))])
        return error_return
@app.route('/addPerson', methods=['POST'])
def add_person():
    try:
        data = control.addPerson(request.json)
        if data[0] == 200:
            return helper.json_return(200, True, {'person':data[1]}, None)
        else:
            return helper.json_return(data[0], False, {'person':None}, [data[1]])
    except Exception as e:
        print('has some errors: {0}'.format(e))
        error_return = helper.json_return(600, False, None, ['Có lỗi ngoại lệ: {0}'.format(str(e))])
        return error_return
@app.route('/updatePerson', methods=['POST'])
def update_person():
    try:
        data = control.updatePerson(request.json)
        if data[0] == 200:
            return helper.json_return(200, True, {'person':data[1]}, None)
        else:
            return helper.json_return(data[0], False, {'person':None}, [data[1]])
    except Exception as e:
        print('has some errors: {0}'.format(e))
        error_return = helper.json_return(600, False, None, ['Có lỗi ngoại lệ: {0}'.format(str(e))])
        return error_return

@app.route('/deletePerson', methods=['POST'])
def delete_person():
    try:
        if not request.json:
            return helper.json_return(600, False, None, ['Json không hợp lệ'])
        data = control.deletePerson(request.json)
        if data[0] == 200:
            return helper.json_return(200, True, {'person':data[1]}, None)
        else:
            return helper.json_return(data[0], False, {'person':None}, [data[1]])
    except Exception as e:
        print('has some errors: {0}'.format(e))
        error_return = helper.json_return(600, False, None, ['Có lỗi ngoại lệ: {0}'.format(str(e))])
        return error_return