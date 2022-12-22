import json
import time
import requests
import sys
from os.path import exists
from math import sqrt
import random
from builtins import zip 
from solution_checker import check_solution
# Global Variables
URL = "http://127.0.0.1:5000/upload"


def parse(id: str, code: str, debug=False) -> str:
    """ Parses the code from the jupyter notebook and (for the type being)
    prints if '1a' is correct or not

    Args:
        id (str): string representing the id of the problem
        code (str): string representation of the code
        debug (bool, optional): if debug is true, print out extra stuff. Defaults to False.
    """
    globals_param = {"zip": zip}
    locals_param = {"print": print, "sqrt": sqrt, "range": range, "zip": zip}
    # pylint disable=exec-used
    
    imports = code.split("\n")
    # Removes import statements, and checks to see if the import statements are authorized. 
    # If they are authorized, it should be imported in this file. 
    for i in imports: 
        if i.startswith("from") or i.startswith("import"):
            if i[i.find("import") + 7:] not in locals_param.keys():
                return "ERROR: Unauthorized Import"
            else: 
                code = code.replace(i, "")
    out = check_solution(code, globals_param, locals_param, id)
    return out
    
                


def add_to_json(id, input, name, email) -> None:
    """ Adds the input to the json file

    Args:
        id (str): id of the problem. 
        input (str): code to add to json file
    """
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # check to see if data.json exists
    feedback = parse(id, input)
    correct = feedback == "All Good!"
    
    key = name.replace(" ", "") + "+" + current_time
    # if bufferID == 'z':
    #     bufferID = 'a'
    # else:
    #     bufferID = chr(ord(bufferID) + 1)
    if not exists("./data.json"):
        data = {}
        
        o = {
            "key": key, 
            "name": name,
            "email": email,
            "id": id,
            "input": input,
            "correct": correct, 
            "feedback": feedback, 
        }
        data[key] = o
        json_out = json.dumps(data, indent=4)
        with open("data.json", "w") as outfile:
            outfile.write(json_out)
            try:
                requests.post(URL, json=data)    
            except: 
                print("Error: Could not connect to server")
    else:
        with open("data.json", "r+") as outfile:
            data = {}
            o = {
                "key": key,
                "name": name,
                "email": email,
                "id": id,
                "input": input,
                "correct": correct, 
                "feedback": feedback, 
            }
            file_data = json.load(outfile)
            file_data[key] = o
            data[key] = o
            outfile.seek(0)
            json.dump(file_data, outfile, indent=4)
            json_out = json.dumps(file_data, indent=4)
            try:
                requests.post(URL, json=data)
            except: 
                print("Error: Could not connect to server")



def main():
    id = "1a"
    code = 'a = 1\nb = 2.0\nc = "3"\n'
    parse(id, code, debug=True)


if __name__ == "__main__":
    main()
