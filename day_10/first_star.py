def import_data(path: str) -> list[list[int]]:
    result = []
    with open(path, 'r') as file:
        for line in file:
            result_line = []
            for num in line.strip():
                result_line.append(int(num))
            result.append(result_line)
    return result

def find_start(data: list[list[int]]) -> list[tuple[int, int]]:
    result = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 0:
                result.append((x, y))
    return result

def follow_trail(data: list[list[int]], start: tuple[int, int]) -> list[tuple[int, int, int]]:
    start_x,start_y = start
    trail = [(start_x, start_y, 0)]
    next_current = [(start_x, start_y)]
    for i in range(1, 10):
        current = next_current
        next_current = []
        for x, y in current:
            if 0 <= x - 1 < len(data[0]) and data[y][x-1] == i:
                if (x-1, y, i) not in trail:
                    trail.append((x-1, y, i))
                next_current.append((x-1, y))
            if 0 <= y - 1 < len(data) and data[y-1][x] == i:
                if (x, y-1, i) not in trail:
                    trail.append((x, y-1, i))
                next_current.append((x, y-1))
            if 0 <= x + 1 < len(data[0]) and data[y][x+1] == i:
                if (x+1, y, i) not in trail:
                    trail.append((x+1, y, i))
                next_current.append((x+1, y))
            if 0 <= y + 1 < len(data) and data[y+1][x] == i:
                if (x, y+1, i) not in trail:
                    trail.append((x, y+1, i))
                next_current.append((x, y+1))
    return trail

def calculate_trail_score(trail: list[tuple[int, int, int]]) -> int:
    result = 0
    for localisation in trail:
        if localisation[2] == 9:
            result += 1
    return result

def main():
    data = import_data('input.txt')
    starts = find_start(data)
    # print(data)
    # print(starts)
    trails = []
    for start in starts:
        trail = follow_trail(data, start)
        # print(f"Trail: {trail}")
        trails.append(trail)
    result = 0
    for trail in trails:
        trail_score = calculate_trail_score(trail)
        # print(f"Trail score: {trail_score}")
        result += trail_score
    print(f"The result is : {result}")

if __name__ == "__main__":
    main()