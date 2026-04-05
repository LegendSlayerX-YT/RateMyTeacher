import json
from flask import Flask, request
from dotenv import load_dotenv

from db.school import find_school, add_school, remove_school, school_not_exist_in_db
from db.vocab import SchoolEntity

load_dotenv()

schools = []
schools_counter = 0
teachers = []
teachers_counter = 0

app = Flask(__name__) #WHAT

# http://127.0.0.1:5000/school/add?school_name=aabbcc&school_country=kkddd
@app.route('/school/add')
def Add_school():
    school_entity = SchoolEntity(
        id=None,
        name=request.args.get('school_name'),
        country=request.args.get('school_country'),
        state=request.args.get('school_state'),
        city=request.args.get('school_city'),
        zip_code=request.args.get('school_zip_code'),
        address=request.args.get('school_street_address'),
        grade_level=request.args.get('school_grade_level'),
    )
    if school_not_exist_in_db(school_entity):
        school_id = add_school(school_entity)
        if school_id is None:
            return "Failed to add school", 500
        return json.dumps({"school_id": school_id, "school_other_info": "ccdd"}) #WHAT
    else:
        return json.dumps({"error" : "The school already exists"})

@app.route('/school/query')
def Query_school():
    try:
        query_schoolID = int(request.args.get('school_id'))
    except ValueError:
        return "Only numeric school id is allowed", 400

    school: SchoolEntity = find_school(query_schoolID)

    if school is None:
        return "School not found", 404
    return json.dumps(school._asdict())


@app.route('/school/remove')
def Remove_school():
    school_id = int(request.args.get('school_id'))
    try:
        del_count = remove_school(school_id)
        return json.dumps({"removed_rows": del_count})
    except:
        return "Looks like something went wrong", 500

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

@app.route('/teacher/query') #what is this exactly
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
    app.run()
