import json
import time
from os.path import exists
from math import sqrt

def parse(id: str, code: str, debug=False) -> str:
    """ Parses the code from the jupyter notebook and (for the type being)
    prints if '1a' is correct or not

    Args:
        id (str): string representing the id of the problem
        code (str): string representation of the code
        debug (bool, optional): if debug is true, print out extra stuff. Defaults to False.
    """
    globals_param = {"__builtins__": None}
    locals_param = {"print": print, "sqrt": sqrt}
    # pylint disable=exec-used
    
    # if debug:
    #     print(f"{id}\n,locals: {locals_param}")
    imports = code.split("\n")
    # Removes import statements, and checks to see if the import statements are authorized. 
    # If they are authorized, it should be imported in this file. 
    for i in imports: 
        if i.startswith("from") or i.startswith("import"):
            if i[i.find("import") + 7:] not in locals_param.keys():
                return "ERROR: Unauthorized Import"
            else: 
                code = code.replace(i, "")
    out = ""
    if id == "1a":
        exec(code, globals_param, locals_param)
        types = {"<class 'int'>": 0, "<class 'float'>": 0, "<class 'str'>": 0}
        for var in locals_param.items():
            try: 
                
                if str(type(locals_param[var[0]])) in types:
                    types[str(type(locals_param[var[0]]))] += 1
                else:
                    if out == "" and not str(type(locals_param[var[0]])) == "<class 'builtin_function_or_method'>":
                        out += "You seem to have a variable type that isn't a float, int, or string.\n"
                        break
            except KeyError:
                pass
    
        for t in types: 
            if types[t] < 1:
                out += "Did you make sure to add a variable of type " + t + "?\n"
            elif types[t] > 1:
                out += f"You have too many of type {t} in your code!\n"
        
        if out != "":
            return out
        else: 
            return "All Good!"
    elif id == "1b":
        exec(code, globals_param, locals_param)
        problem_vars = ["a1", "a2", "a3", "y"]
        answer_vars = [15, 20, -1, 1.5] 
        passed = True
        for i, var in enumerate(problem_vars):
            try:
                passed = locals_param[var] == answer_vars[i]
                if not passed: 
                    out += f"Did you make sure to assign the value of {var} correctly?\n"
            except KeyError:
                print(var)
                return f"Couldn't find {var}, Did you change a1, a2, a3 or y?"
        if out == "":
            return "All Good!"
        else: 
            return out
    elif id == "1c":
        try: 
            exec(code, globals_param, locals_param)
        except TypeError: 
            return "Did you edit the variables correctly, or are they still none?"
        problem_vars = ["a", "b"]
        answer_vars = [None, None]
        passed = True
        for i, var in enumerate(problem_vars):
            answer_vars[i] = locals_param[var]
        if answer_vars[0] > answer_vars[1]: 
            return "All Good!" 
        else: 
            return "a doesn't seem to be greater than b, did you edit them correctly?"
    elif id == "2a": 
        exec(code, globals_param, locals_param)
        
        print(locals_param)
                

def add_to_json(id, input):
    """ Adds the input to the json file

    Args:
        id (str): id of the problem. 
        input (str): code to add to json file
    """
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # check to see if data.json exists
    if not exists("./data.json"):
        data = {}
        data[current_time] = id, input
        json_out = json.dumps(data, indent=4)
        with open("data.json", "w") as outfile:
            outfile.write(json_out)
    else:
        with open("data.json", "r+") as outfile:
            file_data = json.load(outfile)
            file_data[current_time] = id, input
            outfile.seek(0)
            json.dump(file_data, outfile, indent=4)

# create a method that takes a function and a list of arguments and returns the output of the function with the arguments


def main():
    id = "1a"
    code = 'a = 1\nb = 2.0\nc = "3"\n'
    parse(id, code, debug=True)


if __name__ == "__main__":
    main()
