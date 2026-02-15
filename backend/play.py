import json
from flask import Flask, request

schools = []
schools_counter = 0
teachers = []
teachers_counter = 0
app = Flask(__name__)

@app.route('/school/add')
def Add_school():
    global schools_counter
    school_id = str(schools_counter)
    schools_counter += 1
    school_name = request.args.get('school_name')
    school_state = request.args.get('school_state')
    school_city = request.args.get('school_city')
    school_street_address = request.args.get('school_street_address')
    school_phone = request.args.get('school_phone')
    school = {
        'school_name' : school_name,
        'school_state' : school_state,
        'school_city' : school_city,
        'school_street_address' : school_street_address,
        'school_phone' : school_phone,
        'school_id' : school_id
    }
    schools.append(school)
    return str(school_id)

@app.route('/school/query')
def Query_school():
    query_schoolID = request.args.get('school_id')
    for school in schools:
        if query_schoolID == school['school_id']:
            return '<h1>' + str(school) + '</h1>'
    return 'No school found. Imagine'

@app.route('/school/remove')
def Remove_school():
    school_id = request.args.get('school_id')
    for school in schools:
        if school['school_id'] == school_id:
            schools.remove(school)
            return '<h1>You removed '+ school['school_id'] +'</h1>'  
    return '<h1>Imaging trying to remove something that doesn''t exist.</h1>'

@app.route('/teacher/add')
def Add_teacher():
    global teachers_counter
    teacher_id = str(teachers_counter)
    teachers_counter += 1
    teacher_school_id = request.args.get('school_id')
    teacher_name = request.args.get('teacher_name')
    teacher_email = request.args.get('teacher_email')
    teacher = {
        'teacher_name': teacher_name,
        'teacher_email': teacher_email,
        'school_id':teacher_school_id,
        'teacher_id':teacher_id
    }
    teachers.append(teacher)
    return str(teacher_id)

@app.route('/teacher/query')
def Query_teacher():
    teacher_school_id = request.args.get('school_id')
    teacher_name = request.args.get('teacher_name')
    teacher_email = request.args.get('teacher_email')
    teacher_id = request.args.get('teacher_id')
    valid_teachers = []
    for teacher in teachers:
        if ((teacher['teacher_id'] == teacher_id or teacher_id == None) and 
            (teacher['school_id'] == teacher_school_id or teacher_school_id == None) and 
            (teacher['teacher_name'] == teacher_name or teacher_name == None) and
            (teacher['teacher_email'] == teacher_email or teacher_email == None)
            ):
            valid_teachers.append(teacher)
    return json.dumps(valid_teachers)

@app.route('/teacher/remove')
def Remove_teacher():
    teacher_id = request.args.get('teacher_id')
    for teacher in teachers:
        if teacher['teacher_id'] == teacher_id:
            teachers.remove(teacher)
            return '<h1>Success</h1>'
    return '<h1>Failure</h1>'
    

if __name__ == '__main__':
    app.run(host='127.0.0.1')
