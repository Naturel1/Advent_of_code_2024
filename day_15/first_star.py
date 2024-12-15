def import_data(path_move: str, path_map: str) -> tuple[list[str], list[list[str]]]:
    with open(path_move, 'r') as file_move, open(path_map, 'r') as file_map:
        move_data = list(file_move.read())
        map_data = [list(line.strip()) for line in file_map]
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

def can_move(robot: list[int, int], direction: str, map_data: list[list[str]]) -> tuple[int, int] | None:
    x, y = robot
    if direction == "<":
        while map_data[y][x] != "#":
            if map_data[y][x] == ".":
                return x, y
            x = x - 1
    elif direction == ">":
        while map_data[y][x] != "#":
            if map_data[y][x] == ".":
                return x, y
            x = x + 1
    elif direction == "^":
        while map_data[y][x] != "#":
            if map_data[y][x] == ".":
                return x, y
            y = y - 1
    elif direction == "v":
        while map_data[y][x] != "#":
            if map_data[y][x] == ".":
                return x, y
            y = y + 1
    else:
        raise ValueError("Invalid direction")


def process_moves(_moves: list[str], _robot: list[int, int], _map_data: list[list[str]]) -> list[list[str]]:
    for move in _moves:
        end = can_move(_robot, move, _map_data)
        if end is not None:
            if move == "<":
                _map_data[_robot[1]][_robot[0]-1], _map_data[end[1]][end[0]] = _map_data[end[1]][end[0]] , _map_data[_robot[1]][_robot[0]-1]
                _map_data[_robot[1]][_robot[0]], _map_data[_robot[1]][_robot[0]-1] = _map_data[_robot[1]][_robot[0]-1], _map_data[_robot[1]][_robot[0]]
                _robot[0] -= 1
            elif move == ">":
                _map_data[_robot[1]][_robot[0]+1], _map_data[end[1]][end[0]] = _map_data[end[1]][end[0]] , _map_data[_robot[1]][_robot[0]+1]
                _map_data[_robot[1]][_robot[0]], _map_data[_robot[1]][_robot[0]+1] = _map_data[_robot[1]][_robot[0]+1], _map_data[_robot[1]][_robot[0]]
                _robot[0] += 1
            elif move == "^":
                _map_data[_robot[1]-1][_robot[0]], _map_data[end[1]][end[0]] = _map_data[end[1]][end[0]] , _map_data[_robot[1]-1][_robot[0]]
                _map_data[_robot[1]][_robot[0]], _map_data[_robot[1]-1][_robot[0]] = _map_data[_robot[1]-1][_robot[0]], _map_data[_robot[1]][_robot[0]]
                _robot[1] -= 1
            elif move == "v":
                _map_data[_robot[1]+1][_robot[0]], _map_data[end[1]][end[0]] = _map_data[end[1]][end[0]] , _map_data[_robot[1]+1][_robot[0]]
                _map_data[_robot[1]][_robot[0]], _map_data[_robot[1]+1][_robot[0]] = _map_data[_robot[1]+1][_robot[0]], _map_data[_robot[1]][_robot[0]]
                _robot[1] += 1
        print(move)
        print_map(_map_data)
    return _map_data

def calculate_result(map_data: list[list[str]]) -> int:
    result = 0
    for y, row in enumerate(map_data):
        for x, cell in enumerate(row):
            if cell == "O":
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