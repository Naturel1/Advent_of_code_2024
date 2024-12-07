from itertools import product

from tqdm import tqdm


def import_data(file_path: str) -> dict[str, list[str]]:
    result = {}
    with open(file_path, 'r') as file:
        for line in file:
            _line = line.strip().split(': ')
            _line[1] = _line[1].split(" ")
            result[_line[0]] = _line[1]
        return result

def generate_operator_combinations(length: int) -> list[list[str]]:
    combinations = []
    for binary_combination in product([0, 1], repeat=length):
        combination = ['*' if bit else '+' for bit in binary_combination]
        combinations.append(combination)
    return combinations

def verify_operation(key: str, value: list[str]) -> bool:
    operators = ["+"] * (len(value) -1)
    all_combinations = generate_operator_combinations(len(operators))
    for combination in all_combinations:
        result = int(value[0])
        expression = value[0]
        for i in range(len(combination)):
            expression += combination[i] + value[i+1]
            if combination[i] == '*':
                result *= int(value[i+1])
            elif combination[i] == '+':
                result += int(value[i+1])
        if result == int(key):
            # print(f"Found valid expression: {expression}")
            return True
        else:
            pass
            # print(f"Invalid expression: {expression}")
    return False

def count_result(data: dict[str, list[str]]) -> list[str]:
    result = []
    for key, value in tqdm(data.items()):
        if verify_operation(key, value):
            result.append(key)
    return result

def main():
    data = import_data('input.txt')
    print(data)
    correct_keys = count_result(data)
    print(f"The result is : {sum(map(int, correct_keys))}")

if __name__ == "__main__":
    main()