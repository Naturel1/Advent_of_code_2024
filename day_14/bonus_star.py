WIDTH = 101
HEIGHT = 103

def import_data(path: str) -> list[list[list[int, int] | tuple[int, int]]]:
    with open(path, 'r') as file:
        result = []
        for line in file:
            line_parts = line.strip().split(' ')
            robot = [[int(part) for part in line_parts[0][2:].split(',')], tuple(int(part) for part in line_parts[1][2:].split(','))]
            result.append(robot)
        return result

def visualize_grid(robots_map: list[list[str]]) -> None:
    result = ""
    #print(robots_map)
    for tile in robots_map:
        result += "".join(tile) + "\n"

    print(result)

def move_robots(_robots: list[list[list[int, int] | tuple[int, int]]]) -> list[list[list[int, int] | tuple[int, int]]]:
    result = []
    for robot in _robots:
        new_pos = robot
        new_pos[0][0] += robot[1][0]
        new_pos[0][1] += robot[1][1]
        result.append(new_pos)
    return result

def create_robots_map(robots: list[list[list[int, int] | tuple[int, int]]]) -> list[list[str]]:
    robots_map = [[". "] * WIDTH for _ in range(HEIGHT)]
    for robot in robots:
        x, y = robot[0][0]% WIDTH, robot[0][1]%HEIGHT
        robots_map[y][x] = "# "
    return robots_map

def find_easter_egg(robots_map: list[list[str]]) -> bool:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            try:
                if (robots_map[y][x] == "# "
                        and robots_map[y-1][x] == "# "
                        and robots_map[y+1][x] == "# "
                        and robots_map[y][x-1] == "# "
                        and robots_map[y][x+1] == "# "
                        and robots_map[y-1][x-1] == "# "
                        and robots_map[y-1][x+1] == "# "
                        and robots_map[y+1][x-1] == "# "
                        and robots_map[y+1][x+1] == "# "):
                    return True
            except IndexError:
                continue
    return False

def main():
    robots = import_data('input.txt')
    # visualize_grid(robots)
    for i in range(100000):
        robots = move_robots(robots)
        robots_map = create_robots_map(robots)
        if find_easter_egg(robots_map):
            print(f"After move {i+1}:")
            visualize_grid(robots_map)

if __name__ == "__main__":
    main()