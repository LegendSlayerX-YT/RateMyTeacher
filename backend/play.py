import json
from flask import Flask, request
from dotenv import load_dotenv
from dataclasses import asdict

from db.school import find_school, add_school, remove_school
from db.teacher import find_teacher, add_teacher, remove_teacher
from db.vocab import SchoolEntity, SchoolQueryCondition, TeacherEntity, TeacherQueryCondition

load_dotenv()

app = Flask(__name__)

# http://127.0.0.1:5000/school/add?school_name=aabbcc&school_country=kkddd
@app.route('/school/add')
def Add_school():
    school_condition = SchoolQueryCondition(
        id=None,
        name=request.args.get('name'),
        country=request.args.get('country'),
        state=request.args.get('state'),
        city=request.args.get('city'),
        zip_code=request.args.get('zip_code'),
        address=request.args.get('address'),
        grade_level=request.args.get('grade_level'),
    )
    if len(find_school(school_condition)) == 0:
        school_id = add_school(school_condition)
        if school_id is None:
            return "Failed to add school", 500
        return json.dumps({"school_id": school_id, "school_other_info": "ccdd"}) #WHAT
    else:
        return json.dumps({"error" : "The school already exists"})

@app.route('/school/query')
def Query_school():
    school_condition = SchoolQueryCondition(
        id=request.args.get('id'),
        name=request.args.get('name'),
        country=request.args.get('country'),
        state=request.args.get('state'),
        city=request.args.get('city'),
        zip_code=request.args.get('zip_code'),
        address=request.args.get('address'),
        grade_level=request.args.get('grade_level'),
    )

    school_list: list[SchoolEntity] = find_school(school_condition)
    return json.dumps([
        asdict(school)
        for school in school_list
    ])

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
    teacher_condition = TeacherQueryCondition(
        id=None,
        school_id = request.args.get('school_id'),
        name = request.args.get('teacher_name'),
        email = request.args.get('teacher_email')
    )
    if len(find_teacher(teacher_condition)) == 0:
        teacher_id = add_teacher(teacher_condition)
        if teacher_id is None:
            return "Failed to add teacher", 500
        return json.dumps({"teacher_id": teacher_id, "teacher_other_info": "ccdd"})
    else:
        return json.dumps({"error" : "The teacher already exists"})

@app.route('/teacher/query')
def Query_teacher():
    teacher_condition = TeacherQueryCondition(
        id = request.args.get('teacher_id'),
        school_id = request.args.get('school_id'),
        name = request.args.get('teacher_name'),
        email = request.args.get('teacher_email')
    )
    valid_teachers = find_teacher(teacher_condition)
    return json.dumps([
        asdict(teacher)
        for teacher in valid_teachers
    ])


@app.route('/teacher/remove')
def Remove_teacher():
    teacher_id = int(request.args.get('teacher_id'))
    try:
        del_count = remove_teacher(teacher_id)
        return json.dumps({"removed_rows": del_count})
    except:
        return "Looks like something went wrong", 500
    

if __name__ == '__main__':
    app.run()
