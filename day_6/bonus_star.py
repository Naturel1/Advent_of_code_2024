import copy

from tqdm import tqdm


def import_data(path: str) -> list[list[str]]:
    result = []
    with open(path, 'r') as file:
        for line in file:
            result.append(list(line.strip()))
    return result

def find_pointer(data: list[list[str]]) -> list[int | str]|None:
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '^':
                return [x, y, "^"]
            elif data[y][x] == 'v':
                return [x, y, "v"]
            elif data[y][x] == '<':
                return [x, y, "<"]
            elif data[y][x] == '>':
                return [x, y, ">"]
    return None

def visualize_data(__data: list[list[str]], pointer: tuple[int, int, str]) -> str:
    mapper = ""
    #
    # data[pointer[1]][pointer[0]] = pointer[2]
    for i in range(len(__data)):
        for j in range(len(__data[i])):
            mapper += str(__data[i][j])
        mapper += "\n"
    return mapper

def simulate_movement(pointer: list[int | str], _data: list[list[str]]) -> bool:
    x, y, direction = pointer
    max_step = 50000
    steps = 0
    while steps <= max_step:
        try:
            if _data[y][x] == '.':
                _data[y][x] = 'X'

            if direction == "^" and _data[y - 1][x] == '#':
                direction = ">"
            elif direction == "v" and _data[y + 1][x] == '#':
                direction = "<"
            elif direction == "<" and _data[y][x - 1] == '#':
                direction = "^"
            elif direction == ">" and _data[y][x + 1] == '#':
                direction = "v"
            if direction == "^" and _data[y-1][x] != '#':
                y -= 1
            elif direction == "v" and _data[y+1][x] != '#':
                y += 1
            elif direction == "<" and _data[y][x-1] != '#':
                x -= 1
            elif direction == ">" and _data[y][x+1] != '#':
                x += 1
            steps += 1
        except IndexError:
            return False
    # print(visualize_data(_data, pointer))
    return True

def main():
    data: list[list[str]] = import_data('input.txt')
    pointer: list[int | str] | None = find_pointer(data)
    result = 0
    for i in tqdm(range(len(data))):
        for j in range(len(data[i])):
            if data[i][j] == '.':
                data2 = copy.deepcopy(data)
                data2[i][j] = '#'
                if simulate_movement(pointer, data2):
                    #print(f"({i},{j}) is True")
                    result += 1
                else:
                    pass
                    #print(f"({i},{j}) is False")

    # 2176
    # result: list[tuple[int, int]] = simulate_movement(pointer, data)
    print(f"The result is : {result}")

if __name__ == "__main__":
    main()