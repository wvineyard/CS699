from its_manager import parse


def test_1a_1(): 
    # Test Correct Input
    output = parse("1a", "a = 1\nb = 2.0\nc = '3'\n", debug=True)
    assert output == "All Good!"

def test_1a_2():
    # Test all Int
    output = parse("1a", "a = 1\nb = 2\nc= 3\n", debug=True)
    assert output == "You have too many of type <class 'int'> in your code!\nDid you make sure to add a variable of type <class 'float'>?\nDid you make sure to add a variable of type <class 'str'>?\n"
    

def test_1a_3():
    # Test a variable type that isn't a int, float, or string
    output = parse("1a", "a = 1\nb = 2.0\nc = [1, 2, 3]\n", debug=True)
    assert output == "You seem to have a variable type that isn't a float, int, or string.\nDid you make sure to add a variable of type <class 'str'>?\n"

def test_1b_1():
    output = parse("1b", "x, y, z = 4, 5, 6\n# Assign the sum of x, y, and z to a\na1 = x + y + z\n# Assign the product of x and y to a2\na2 = x * y\n# Assign the difference between y and z to a3\na3 = y - z\n# Find the quotient of z and x, and assign the result to y, then print y\ny = z / x", debug=True)
    assert output == "All Good!"
    
def test_1b_2():
    output = parse("1b", "x, y, z = 4, 5, 6\n# Assign the sum of x, y, and z to a\na1 = x + y + z\n# Assign the product of x and y to a2\na2 = x ** y\n# Assign the difference between y and z to a3\na3 = y - z\n# Find the quotient of z and x, and assign the result to y, then print y\ny = z / x", debug=True)
    assert output == "Did you make sure to assign the value of a2 correctly?\n"  

def test_1b_3():
    output = parse("1b", "x, y, z = 4, 5, 6\n# Assign the sum of x, y, and z to a1\na1 = x + y + z\n# Assign the product of x and y to a2\na4 = x * y\n# Assign the difference between y and z to a3\na3 = y - x\n# Find the quotient of z and x, and assign the result to y, then print y\ny = z / x\n", debug=True)
    assert output == "Couldn't find a2, Did you change a1, a2, a3 or y?"
    
      
def main():
    test_1a_1()
    test_1a_2()
    test_1a_3()
    test_1b_1()
    test_1b_2()
    test_1b_3()

if __name__ == "__main__":
    main()