def import_data(path_move: str, path_map: str) -> tuple[list[str], list[list[str]]]:
    with open(path_move, 'r') as file_move, open(path_map, 'r') as file_map:
        move_data = list(file_move.read())
        map_data = [list(line.strip().replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")) for line in file_map]
    return move_data, map_data

def print_map(map_data: list[list[str]]) -> None:
    for row in map_data:
        print(''.join(row))

def find_robot_position(map_data: list[list[str]]) -> list[int, int]:
    for y, row in enumerate(map_data):
        for x, cell in enumerate(row):
            if cell == '@':
                return [x, y]
    raise ValueError("No robot found in the map")

def can_move(robot: list[int, int], direction: str, map_data: list[list[str]]) -> list[tuple[int, int, str]] | None:
    x, y = robot
    check = [(x, y)]
    result = []
    if direction == "<":
        while len(check) > 0:
            x, y = check.pop()
            if map_data[y][x] == "@":
                check.append((x-1, y))
                result.append((x, y, "@"))
            elif map_data[y][x] == "#":
                return
            elif map_data[y][x] == "]" or map_data[y][x] == "[":
                check.append((x-1, y))
                result.append((x, y, map_data[y][x]))
        return result
    elif direction == ">":
        while len(check) > 0:
            x, y = check.pop()
            if map_data[y][x] == "@":
                check.append((x+1, y))
                result.append((x, y, "@"))
            elif map_data[y][x] == "#":
                return
            elif map_data[y][x] == "]" or map_data[y][x] == "[":
                check.append((x+1, y))
                result.append((x, y, map_data[y][x]))
        return result
    elif direction == "^":
        while len(check) > 0:
            x, y = check.pop()
            if map_data[y][x] == "@":
                check.append((x, y-1))
                result.append((x, y, "@"))
            elif map_data[y][x] == "#":
                return
            elif map_data[y][x] == "]":
                check.append((x, y-1))
                if (x-1, y, "[") not in result:
                    check.append((x-1, y))
                result.append((x, y, map_data[y][x]))
            elif map_data[y][x] == "[":
                check.append((x, y-1))
                if (x + 1, y, "]") not in result:
                    check.append((x+1, y))
                result.append((x, y, map_data[y][x]))
        return result
    elif direction == "v":
        while len(check) > 0:
            x, y = check.pop()
            if map_data[y][x] == "@":
                check.append((x, y+1))
                result.append((x, y, "@"))
            elif map_data[y][x] == "#":
                return
            elif map_data[y][x] == "]":
                check.append((x, y + 1))
                if (x-1, y, "[") not in result:
                    check.append((x - 1, y))
                result.append((x, y, map_data[y][x]))
            elif map_data[y][x] == "[":
                check.append((x, y + 1))
                if (x + 1, y, "]") not in result:
                    check.append((x + 1, y))
                result.append((x, y, map_data[y][x]))
        return result
    else:
        raise ValueError("Invalid direction")


def process_moves(_moves: list[str], _robot: list[int, int], _map_data: list[list[str]]) -> list[list[str]]:
    for move in _moves:
        end = can_move(find_robot_position(_map_data), move, _map_data)
        print(end)
        if end is not None:
            if move == "<":
                for cell in end:
                    _map_data[cell[1]][cell[0]] = "."
                for cell in end:
                    _map_data[cell[1]][cell[0]-1] = cell[2]
            elif move == ">":
                for cell in end:
                    _map_data[cell[1]][cell[0]] = "."
                for cell in end:
                    _map_data[cell[1]][cell[0]+1] = cell[2]
            elif move == "^":
                for cell in end:
                    _map_data[cell[1]][cell[0]] = "."
                for cell in end:
                    _map_data[cell[1]-1][cell[0]] = cell[2]
            elif move == "v":
                for cell in end:
                    _map_data[cell[1]][cell[0]] = "."
                for cell in end:
                    _map_data[cell[1]+1][cell[0]] = cell[2]
        print(move)
        print_map(_map_data)
    return _map_data

def calculate_result(map_data: list[list[str]]) -> int:
    result = 0
    for y, row in enumerate(map_data):
        for x, cell in enumerate(row):
            if cell == "[":
                result += 100 * y + x
    return result

def main():
    moves, map_data = import_data('input_moves.txt', 'input_map.txt')
    print_map(map_data)
    print(moves)
    robot = find_robot_position(map_data)
    print(f"Robot starts at position: {robot}")
    processed_map = process_moves(moves, robot, map_data)
    result = calculate_result(processed_map)
    print(f"The result is : {result}")

if __name__ == "__main__":
    main()