from flask import request, render_template

from _app import app

@app.route('/school')
def School():    
    return render_template('school.html')

@app.route('/teacher')
def Teacher():
    school_id = request.args.get('school_id')
    print(f"/teacher?school_id={school_id}")
    return render_template('teacher.html', school_id = school_id if school_id is not None else "null")
