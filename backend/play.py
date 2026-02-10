from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world() -> str:
    return "Hello, World!"


"""
Example:
http://127.0.0.1:5000/teacher/aaa?id=bbb&key=value

function argument id will be 'aaa'
request.args will be a map {'id': 'bbb', 'key': 'value'}

request.data can only be populated when using POST method.
The advantage of POST method is that the body is not subjust to URL length limitation 
"""
@app.route("/teacher/<id>", methods=['GET', 'POST'])
def query_teacher(id: str) -> str:
    
    response = app.make_response(f"""
    You are quering teacher: <br>
    using method {request.method} <br>
    function argument {id} <br>
    request.args {request.args.get("id")} <br>
    request.data {request.data} <br>
""")
    
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == "__main__":
    app.run(debug=True)