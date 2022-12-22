from its_manager import parse

def test_2a_1(): 
    output = parse('2a', "from math import sqrt\n\ndef quadratic_formula(a, b, c): \n    x1 = -b + (sqrt(b^2 - 4 * a * c) / (2*a))#insert code here\n    x2 = -b - (sqrt(b^2 - 4 * a * c) / (2*a))\n    return x1, x2\n")
    assert output == "All Good!"

def main(): 
    test_2a_1()
    
if __name__ == "__main__": 
    main() 