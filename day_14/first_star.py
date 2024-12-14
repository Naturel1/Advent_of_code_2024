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

def visualize_grid(robots: list[list[list[int, int], tuple[int, int]]]) -> None:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            nbr_robots = 0
            for robot in robots:
                if robot[0][0] % WIDTH == x and robot[0][1] % HEIGHT == y:
                    nbr_robots += 1
            else:
                if nbr_robots == 0:
                    print('.', end=' ')
                else:
                    print(nbr_robots, end=' ')
        print()

def move_robots(_robots: list[list[list[int, int] | tuple[int, int]]]) -> list[list[list[int, int] | tuple[int, int]]]:
    result = []
    for robot in _robots:
        new_pos = robot
        new_pos[0][0] += robot[1][0]
        new_pos[0][1] += robot[1][1]
        result.append(new_pos)
    print(result)
    return result

def calculate_safty(robots: list[list[list[int, int] | tuple[int, int]]]) -> int:
    robots_per_zone = [0, 0, 0, 0]
    mid_width = (WIDTH // 2)
    mid_height = (HEIGHT // 2)
    for robot in robots:
        if robot[0][0] % WIDTH < mid_width and robot[0][1] % HEIGHT < mid_height:
            robots_per_zone[0] += 1
        elif robot[0][0] % WIDTH > mid_width and robot[0][1] % HEIGHT < mid_height:
            robots_per_zone[1] += 1
        elif robot[0][0] % WIDTH < mid_width and robot[0][1] % HEIGHT > mid_height:
            robots_per_zone[2] += 1
        elif robot[0][0] % WIDTH > mid_width and robot[0][1] % HEIGHT > mid_height:
            robots_per_zone[3] += 1
    print(robots_per_zone)
    return robots_per_zone[0] * robots_per_zone[1] * robots_per_zone[2] * robots_per_zone[3]



def main():
    robots = import_data('input.txt')
    visualize_grid(robots)
    for i in range(100):
        robots = move_robots(robots)
        print(f"After move {i+1}:")
        # visualize_grid(robots)
    print(f"The number of safe zones: {calculate_safty(robots)}")
if __name__ == "__main__":
    main()