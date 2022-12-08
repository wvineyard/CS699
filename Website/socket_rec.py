from flask import Flask, request
import json
import sqlite3
from sqlite3 import Error
import sys


app = Flask(__name__)
connection = None
@app.route('/query-example')
def query_example():
    language = request.args.get('language')
    #if key doesn't exist, returns None
    return '''<h1>The language value is: {}</h1>'''.format(language)

@app.route('/form-example')
def form_example():
    return 'Form Data Example'

# GET requests will be blocked
# GET requests will be blocked
@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']

        if 'framework' in request_data:
            framework = request_data['framework']

        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']

        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                example = request_data['examples'][0]

        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)
           
           
@app.route('/upload', methods=['POST'])
def upload():
    request_data = request.get_json()
    status = True
    for items in request_data.keys(): 
        status = db_entry(request_data[items])
        if status != True: 
            return str(status) + " " + str(items)
    return str(status)
    

def db_entry(entry):
    try:
        key = entry["key"]
        
        name = entry["name"]
        email = entry["email"]
        id = entry["id"]
        input = entry["input"]
        correct = entry["correct"]
        feedback = entry["feedback"]
        print(key, name, email, id, input, correct, feedback, file=sys.stderr)
    
        print("Attempting to add entry to database", file=sys.stderr)
        connection = sqlite3.connect("solutions.db")
        print("Failed Here 1", file=sys.stderr)
        cursor = connection.cursor()
        sql = f"""
            INSERT INTO data(date_name_id, name, email, problem_id, submitted_code, correct, feedback) 
            VALUES('{key}', '{name}','{email}', '{id}', '{input}', {correct}, '{feedback}');
        """
        print("Failed Here 2", file=sys.stderr)
        print(sql, file=sys.stderr)
        count = cursor.execute(sql)
        print("Failed Here 3", file=sys.stderr)
        connection.commit()
        print("Entry added", file=sys.stderr)
        cursor.close()
        return True
    except Error as e:
        print(f"Failed to add entry to database with error {e}", file=sys.stderr)
        return False
    
    
    
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

if __name__ == '__main__':
    # run app in debug mode on port 5000
    # connection = create_connection("solutions.db")
    # print("Connection created", file=sys.stderr)
    app.run(debug=True, port=5000)