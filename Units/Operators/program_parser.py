import json
import time
from os.path import exists


def parse(id: str, code: str, debug=False):
    """ Parses the code from the jupyter notebook and (for the type being)
    prints if '1a' is correct or not

    Args:
        id (str): string representing the id of the problem
        code (str): string representation of the code
        debug (bool, optional): if debug is true, print out extra stuff. Defaults to False.
    """
    globals_param = {"__builtins__": None}
    locals_param = {"print": print}
    # pylint disable=exec-used
    exec(code, globals_param, locals_param)
    if debug:
        print(f"{id}\n,locals: {locals_param}")
    types = {"<class 'int'>": 0, "<class 'float'>": 0, "<class 'str'>": 0}
    for var in locals_param.items():
        try: 
            if str(type(locals_param[var[0]])) in types:
                types[str(type(locals_param[var[0]]))] += 1
        except KeyError:
            pass
    out = ""
    for t in types: 
        if types[t] < 1:
            out += "Did you make sure to add a variable of type " + t + "?\n"
        elif types[t] > 1:
            out += f"You have too many of type {t} in your code!\n"
    if out != "":
        print(out)
    else: 
        print("All good!")

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


def main():
    id = "1a"
    code = 'a = 1\nb = 2.0\nc = "3"\n'
    parse(id, code, debug=True)


if __name__ == "__main__":
    main()
