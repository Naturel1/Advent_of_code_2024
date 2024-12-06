def import_rule(path: str) -> dict[str, list[str]]:
    result = {}
    with open(path, 'r') as file:
        for line in file:
            _line = line.strip().split('|')
            if _line[0] in result:
                result[_line[0]].append(_line[1])
            else:
                result[_line[0]] = [_line[1]]
    return result

def import_data(path: str) -> list[list[str]]:
    result = []
    with open(path, 'r') as file:
        for line in file:
            result.append([x for x in line.strip().split(',')])
    return result

def check_if_correct(rule: dict[str, list[str]], line: list[str]) -> bool:
    for index in range(1, len(line)):
        for i in range(0, index):
            if line[index] in rule:
                if line[i] in rule[line[index]]:
                    return False
    return True

def find_correct_line(rules: dict[str, list[str]], data: list[list[str]]) -> list[list[str]]:
    result = []
    for line in data:
        if check_if_correct(rules, line):
            result.append(line)
    return result

def count_result(correct_lines: list[list[str]]) -> int:
    result = 0
    for x in correct_lines:
        result += int(x[(len(x)//2)])
    return result


def main():
    rules = import_rule('input_rule.txt')
    data = import_data('input_data.txt')
    print(f"rules : {rules}")
    print(f"data : {data}")
    correct_lines = find_correct_line(rules, data)
    print(f"Correct lines : {correct_lines}")
    result = count_result(correct_lines)
    print(f"The result is : {result}")

if __name__ == "__main__":
    main()