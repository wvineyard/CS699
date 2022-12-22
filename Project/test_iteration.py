from solution_checker import check_solution
from its_manager import parse
def test_4a():
    # Test to see if the function is correct through 10000 iterations
    output = parse('4a', "for i in range(0, 101, 5):\n    print(i)")
    assert output == "All Good!"

if __name__ == '__main__':
    test_4a()
    