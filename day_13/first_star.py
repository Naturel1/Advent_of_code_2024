import re

MAX_PUSH = 100
A_PRICE = 3
B_PRICE = 1

def import_data(path: str) -> list[dict[str: dict[str, int]]]:
    result = []
    with open(path, 'r') as file:
        index = 0
        for line in file:
            index += 1
            if index % 4 == 1:
                x_regex = r'X([+-]\d+)'
                y_regex = r'Y([+-]\d+)'
                x = re.search(x_regex, line)
                y = re.search(y_regex, line)
                result.append({
                    "a" : {'x': int(x.group(1)), 'y': int(y.group(1))}
                })
            elif index % 4 == 2:
                x_regex = r'X([+-]\d+)'
                y_regex = r'Y([+-]\d+)'
                x = re.search(x_regex, line)
                y = re.search(y_regex, line)
                result[-1]["b"] = {'x': int(x.group(1)), 'y': int(y.group(1))}
            elif index % 4 == 3:
                x_regex = r'X([=-]\d+)'
                y_regex = r'Y([=-]\d+)'
                x = re.search(x_regex, line)
                y = re.search(y_regex, line)
                result[-1]["prize"] = {'x': int(x.group(1)[1:]), 'y': int(y.group(1)[1:])}
    return result

def find_best_play(machine: dict[str: dict[str, int]]) -> int:
    x_result = []
    y_result = []
    for a in range(MAX_PUSH+1):
        for b in range(MAX_PUSH+1):
            # print(f"Trying {a} for A and {b} for B")
            if (a * machine["a"]["x"] + b * machine["b"]["x"]) == machine["prize"]["x"]:
                x_result.append((a, b, (a*A_PRICE)+(b*B_PRICE)))
    for a in range(MAX_PUSH):
        for b in range(MAX_PUSH):
            if (a * machine["a"]["y"] + b * machine["b"]["y"]) == machine["prize"]["y"]:
                y_result.append((a, b, (a*A_PRICE)+(b*B_PRICE)))
    possible_wins = []
    for x in x_result:
        if x in y_result:
            possible_wins.append(x)
    if len(possible_wins) == 0:
        return 0
    return sorted(possible_wins, key=lambda x: x[2], reverse=True)[0][2]


def process_data(data: list[dict[str: dict[str, int]]]) -> int:
    total_tickets = 0
    for machine in data:
        total_tickets += find_best_play(machine)
    return total_tickets

def main():
    data = import_data("input.txt")
    print(data)
    result = process_data(data)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()