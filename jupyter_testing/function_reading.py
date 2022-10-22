import json
import os

def read_json(): 
    """# read json file and return as dictionary"""
    with open('jupyter_testing\data.json', 'r') as outfile: 
        file_data = json.load(outfile)
    return file_data
    

def extract_code(code): 
    code = code.split("\n")
    comments = []
    code_data = []
    for line in code:
        if len(line) == 0: continue
        if line[0] == "#": 
            comments.append(line)
        else: 
            code_data.append(line)
    return comments, code_data
    
def main(): 
    data = read_json()
    comments, code_data = extract_code(list(data.values())[0])
    print(comments)
    print(code_data)
    varibles = {}
    for c in code_data:
        
        if "=" in c:
            varibles[c.split("=")[0].strip()] = c.split("=")[1].strip()
            
        elif "print" in c:
            varibles["output"] = c.split("(")[1].split(")")[0]
    
    print(varibles)

if __name__ == '__main__':
    main()