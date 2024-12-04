import re

def import_data(path: str) -> str:
    with open(path, 'r') as file:
        return file.read()

def find_mul(data: str) -> list[str]:
    pattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
    return re.findall(pattern, data)

def clear_data(data: list[str]) -> list[tuple[int, int]]:
    result = []
    do = True
    print(f"Original data: {data}")
    for mul in data:
        if not do and mul == 'do()':
            do = True
        elif do and mul == "don't()":
            do = False
        if do and mul.startswith('mul('):
            result.append(tuple(int(x) for x in mul[4:-1].split(',')))
    return result

def calculate_mul(value_mul: list[tuple[int, int]]) -> int:
    result = 0
    for a, b in value_mul:
        result += a * b
    return result

def main():
    data: str = import_data('input.txt')
    mul: list[str] = find_mul(data)
    value_mul: list[tuple[int, int]] = clear_data(mul)
    print(f"The result is : {calculate_mul(value_mul)}")

if __name__ == "__main__":
    main()