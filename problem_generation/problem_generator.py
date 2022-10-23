import random

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
    out = ""
    for i, var in enumerate(vars.keys()): 
        out += "(" + generator_helper.var_operator(var, vars[var]) + ")"
        if i != len(vars.keys()) - 1:
            out += random.choice(["+", "-"])
        exec(f"{var} = {vars[var]}")
    loc = {}
    exec(f"{out}", loc)
    print(ans)
    return out, ans

if __name__ == '__main__':
    vars = {'x': 1, 'y': 2, 'z': 3}
    # print(generator_helper.var_operator('x'))
    print(gen_algorithm(vars))  