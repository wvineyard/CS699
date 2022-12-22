from solution_checker import check_solution
from its_manager import parse

def test_7a():
    output = parse('7a', "def name_age(names: list, ages: list) -> dict:\n    name_age_dict = {}\n    for name, age in zip(names, ages):\n        # your code here\n        name_age_dict[name] = age\n    return name_age_dict")
    print(output)

if __name__ == '__main__':
    test_7a()