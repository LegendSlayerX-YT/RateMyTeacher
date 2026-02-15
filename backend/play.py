from flask import Flask, request

schools = []
schools_counter = 0
app = Flask(__name__)

@app.route('/schools/add')
def Add_school():
    global schools_counter
    school_id = str(schools_counter)
    schools_counter += 1
    school_name = request.args.get('school_name')
    school_state = request.args.get('school_state')
    school_city = request.args.get('school_city')
    school_street_address = request.args.get('school_street_address')
    school_phone= request.args.get('school_phone')
    map = {
        "school_name" : school_name,
        'school_state' : school_state,
        'school_city' : school_city,
        'school_street_address' : school_street_address,
        'school_phone' : school_phone,
        'school_id' : school_id
    }
    schools.append(map)
    return str(school_id)

@app.route('/schools/query')
def Query_school():
    query_schoolID = request.args.get('school_id')
    for school in schools:
        if query_schoolID == school["school_id"]:
            return '<h1>' + str(school) + '</h1>'
    return 'No school found. Imagine'

@app.route('/schools/remove')
def Remove_school():
    remove = request.args.get('school_id')
    for school_remove in schools:
        if school_remove["school_id"] == remove:
            schools.remove(school_remove)
            return '<h1>You removed'+ school_remove["school_id"] +'</h1>'  
    return '<h1>Imaging trying to remove something that doesn''t exist.</h1>'


if __name__ == '__main__':
    app.run(host='192.168.86.26')
