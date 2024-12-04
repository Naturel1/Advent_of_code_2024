import re

def import_data(path: str) -> str:
    with open(path, 'r') as file:
        return file.read()

def find_mul(data: str) -> list[str]:
    return re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)

def clear_data(data: list[str]) -> list[tuple[int, int]]:
    result = []
    for mul in data:
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