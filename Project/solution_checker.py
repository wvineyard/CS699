from contextlib import redirect_stdout
import io
import random
import string
import subprocess

def check_solution(code, globals_param, locals_param, id):
    out = ""
    if id == "1a":
        # check to see if they have the right variables
        exec(code, globals_param, locals_param)
        types = {"<class 'int'>": 0, "<class 'float'>": 0, "<class 'str'>": 0}
        for var in locals_param.items():
            try: 
                
                if str(type(locals_param[var[0]])) in types:
                    types[str(type(locals_param[var[0]]))] += 1
                else:
                    if out == "" and not str(type(locals_param[var[0]])) in ("<class 'builtin_function_or_method'>", "<class 'function'>", "<class 'module'>", "<class 'range'>", "<class 'zip'>", "<class 'type'>"):
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
        # check to see if they performed the correct operations
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
    elif id == "2a":
        # Check to see if the function is correct through 10000 iterations
        exec(code, globals_param, locals_param)
        func = locals_param["calculate_area"]
        status = True
        for i in range(10000): 
            status = func(i) == i**2 * 3.14
            if not status:
                return f"Tried computing for {i}, but got {func(i)} instead of {i**2 * 3.14}"
        return "All Good!"
        # print(locals_param)
    elif id == "2b":
        exec(code, globals_param, locals_param)
        func = locals_param["calculate_force"]
        for _ in range(10000): 
            val1, val2, r = random.randint(100, 10000), random.randint(100, 10000), random.randint(100, 10000)
            val1, val2, r = val1*1000, val2*1000, r*1000
            G = 6.67408 * 10**-11
            status = abs(func(val1, val2, r) - G * (val1 * val2) / r**2) <= 0.01
            if not status:
                return f"Tried computing for m1={val1}, m2={val2}, r={r}, but got {func(val1, val2, r)} instead of {G * (val1 * val2) / r**2}"
        return "All Good!"
    elif id == "2c":
        exec(code, globals_param, locals_param)
        func = locals_param["calculate_y"]
        for i in range(10000):
            val1, val2, val3 = random.randint(1, 10000), random.randint(1, 10000), random.randint(1, 10000)
            status = func(val1, val2, val3) == val1 * val2 + val3
            if not status:
                return f"Tried computing for a={val1}, b={val2}, c={val3}, but got {func(val1, val2, val3)} instead of {val1 * val2 + val3}"
        return "All Good!"
    elif id == "3a":
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
    elif id == "3b":
        # Check to see if the function is correct through 10000 iterations randomly. 
        exec(code, globals_param, locals_param)
        func = locals_param["maximum"]
        seed = 11272022
        random.seed(seed)
        status = True
        for i in range(0, 10000, 500): 
            val1, val2 = random.randint(0, i), random.randint(0, i+1)
            status = func(val1, val2) == max(val1, val2)
            if not status:
                return f"Tried computing for a={val1} and b={val2}, but got {func(val1, val2)} instead of {max(val1, val2)}"
        return "All Good!"
    elif id == "3c": 
        exec(code, globals_param, locals_param)
        func = locals_param['check_letter']
        status = True
        upperLetters = string.ascii_uppercase
        lowerLetters = string.ascii_lowercase
        all_chars = string.printable
        for c in all_chars: 
            if c in upperLetters:
                status = func(c) == "upper"
            elif c in lowerLetters:
                status = func(c) == "lower"
            else: 
                status = func(c) == "other"
            if not status:
                return f"Tried computing for {c}, but got {func(c)} instead of {func(c)}"
        return "All Good!"
    elif id == "4a": 
        with redirect_stdout(io.StringIO()) as f:
            exec(code, globals_param, locals_param)
        ans = list(range(0, 101, 5))
        c = list(f.getvalue().splitlines())
        c = [int(i) for i in c]
        diff = list(set(ans) - set(c))
        if not diff:
            return "All Good!"
        else:
            return f"There was some numbers that didn't match up! Your function produced {str(diff)} values that didn't match up."
    elif id == "4b": 
        # TODO: Complete
        exec(code, globals_param, locals_param)
        func = locals_param['check_letter']
        status = True
    elif id == "4c":
        # TODO: Complete this. Will need to redirect stdout for this.
        pass
    elif id == "5a":
        exec(code, globals_param, locals_param)
        func = locals_param['capitalize_first']
        status = True
        strings = ["the quick brown fox", "jumps over the lazy dog", "hello world", "goodbye moon"]
        capitalized_strings = ["The Quick Brown Fox", "Jumps Over The Lazy Dog", "Hello World", "Goodbye Moon"]
        for i, s in enumerate(strings): 
            status = func(s) == capitalized_strings[i]
            if not status: 
                if func(s) is None: 
                    return "Your function returned None, did you forget to return something?"
                return f"Ran your function on {s}, but got {func(s)} instead of {capitalized_strings[i]}"
        return "All Good!"
    elif id == "5b":
        exec(code, globals_param, locals_param)
        func = locals_param['remove_vowels']
        status = True
        strings = ["the quick brown fox", "jumps over the lazy dog", "hello world", "goodbye moon"]
        solutions = ["th qck brwn fx", "jmps vr th lzy dg", "hll wrld", "gdby mn"]
        for i, s in enumerate(strings): 
            status = func(s) == solutions[i]
            if not status: 
                if func(s) is None: 
                    return "Your function returned None, did you forget to return something?"
                return f"Ran your function on {s}, but got {func(s)} instead of {solutions[i]}"
        return "All Good!"
    elif id == "5c":
        exec(code, globals_param, locals_param)
        func = locals_param['remove_spaces']
        status = True
        strings = ["the quick brown fox", "jumps over the lazy dog", "hello world", "goodbye moon"]
        solutions = ["thequickbrownfox", "jumpsoverthelazydog", "helloworld", "goodbyemoon"]
        for i, s in enumerate(strings): 
            status = func(s) == solutions[i]
            if not status:
                if func(s) is None: 
                    return "Your function returned None, did you forget to return something?"
                return f"Ran your function on {s}, but got {func(s)} instead of {solutions[i]}"
        return "All Good!"
    elif id == "6a":
        exec(code, globals_param, locals_param)
        func = locals_param['sum_elements']
        status = True
        for _ in range(100): 
            length = random.randrange(10)
            random_list = [random.randint(1, 101) for _ in range(length)]
            ret = func(random_list)
            if ret is None: 
                return "Your function returned None, did you forget to return something?"
            status = ret == sum(random_list)
            if not status: 
                return f"Ran your function on {random_list}, but got {ret} instead of {sum(random_list)}"
        return "All Good!"
    elif id == "6b":
        exec(code, globals_param, locals_param)
        func = locals_param['max_in_list']
        status = True
        for _ in range(100): 
            length = random.randrange(10)
            random_list = [random.randint(1, 101) for _ in range(length)]
            ret = func(random_list)
            if ret is None: 
                return "Your function returned None, did you forget to return something?"
            status = ret == max(random_list)
            if not status: 
                return f"Ran your function on {random_list}, but got {ret} instead of {sum(random_list)}"
    elif id == "6c":
        exec(code, globals_param, locals_param)
        func = locals_param['make_list']
        status = True
        for _ in range(100): 
            a = random.randrange(1, 101)
            b = random.randrange(1, 101)
            c = random.randrange(1, 101)
            ret = func(a, b, c)
            if ret is None: 
                return "Your function returned None, did you forget to return something?"
            status = ret == [a, b, c, a+b+c]
            if not status:
                if len(ret) == 3: 
                    return f"Did you make sure to append the sum at the end of the list?"
                return f"Ran your function on {a}, {b}, {c}, but got {ret} instead of {[a, b, c, a+b+c]}"
    elif id == "6d":
        exec(code, globals_param, locals_param)
        func = locals_param['max_in_list']
        status = True
        for _ in range(100): 
            length = random.randrange(10)
            random_list = [random.randint(1, 101) for _ in range(length)]
            ret = func(random_list)
            if ret is None: 
                return "Your function returned None, did you forget to return something?"
            status = ret == [sum(random_list), sum(random_list) / len(random_list)]
            if not status: 
                if len(ret) != 2: 
                    f"The length doesn't seem to be correct, is the list both the sum and the average, and nothing else?"
                return f"Ran your function on {random_list}, but got {ret} instead of {[sum(random_list), sum(random_list) / len(random_list)]}"
    elif id == "7a":
        exec(code, globals_param, locals_param)
        func = locals_param['name_age']
        status = True
        names = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank', 'Gary', 'Holly', 'Igor', 'Joan',
         'Kim', 'Laura', 'Mike', 'Nick', 'Olivia', 'Pat', 'Qing', 'Rachel', 'Sam', 'Tina',
         'Ursula', 'Violet', 'Wendy', 'Xander', 'Yvette', 'Zach']

        for _ in range(100):
            name = random.sample(names, k=5)
            age = [random.randint(15, 80) for _ in range(5)]
            ret = func(name, age)
            if ret is None: 
                return "Your function returned None, did you forget to return something?"
            status = ret == {name[i]: age[i] for i in range(5)}
            if not status: 
                return f"Ran your function on {name}, {age}, but got {ret} instead of {dict(zip(name, age))}"
        return "All Good!"
    
    
    