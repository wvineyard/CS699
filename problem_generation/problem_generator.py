import random
from io import StringIO
from contextlib import redirect_stdout

globals_param = {'__builtins__' : None}
locals_param = {'ans' : ""}
class generator_helper(): 
    
    def var_operator(var, value=None):
        op = random.choice(["+", "-", "*", "/", "**"])
        if value is None:
            value = random.randint(1, 10)
        exec(f"{var} = 0")
        # exec(f"out = {var}{op}{value}")
        # print(out)
        return f"{var}{op}{value}"

def gen_algorithm(vars: dict): 
    noVals = False
    out = ""
    for i, var in enumerate(vars.keys()):
        if vars[var] is None: 
            noVals = True
        out += "(" + generator_helper.var_operator(var, vars[var]) + ")"
        if i != len(vars.keys()) - 1:
            out += random.choice(["+", "-"])
        exec(f"{var} = {vars[var]}")
    loc = {}
    if not noVals:
        f = StringIO()
        with redirect_stdout(f): 
            exec(f"print({out})")  
        s = f.getvalue() 
        print(s)
        return out, float(s.strip())
    else: 
        return out, "Null"    

if __name__ == '__main__':
    vars = {'x': 1, 'y': 2, 'z': 3}
    vars2 = {'x': None, 'y': None}
    # print(generator_helper.var_operator('x'))
    print(gen_algorithm(vars))  
    print(gen_algorithm(vars2))  