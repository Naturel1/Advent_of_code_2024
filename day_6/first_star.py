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

def simulate_movement(pointer: list[int | str], data: list[list[str]]) -> list[tuple[int, int]]:
    result = []
    x, y, direction = pointer
    while 0 <= x < len(data[0]) and 0 <= y < len(data):
        if (x, y) not in result:
            result.append((x, y))
        if direction == "^" and data[y-1][x] != '#':
            y -= 1
        elif direction == "v" and data[y+1][x] != '#':
            y += 1
        elif direction == "<" and data[y][x-1] != '#':
            x -= 1
        elif direction == ">" and data[y][x+1] != '#':
            x += 1
        if direction == "^" and data[y-1][x] == '#':
            direction = ">"
        elif direction == "v" and data[y+1][x] == '#':
            direction = "<"
        elif direction == "<" and data[y][x-1] == '#':
            direction = "^"
        elif direction == ">" and data[y][x+1] == '#':
            direction = "v"
    return result

def main():
    data: list[list[str]] = import_data('input.txt')
    pointer: list[int | str] | None = find_pointer(data)
    print(data)
    print(pointer)
    result: list[tuple[int, int]] = simulate_movement(pointer, data)
    print(f"The result is : {len(result)}")

if __name__ == "__main__":
    main()