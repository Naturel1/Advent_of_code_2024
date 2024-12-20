from collections import deque
from copy import deepcopy

from tqdm import tqdm


def import_data(path: str) -> list[list[str]]:
    result = []
    with open(path, 'r') as file:
        for line in file:
            result.append(list(line.strip()))
    return result

def find_start_and_end(data: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
    start = end = None
    for y, row in enumerate(data):
        for x, value in enumerate(row):
            if value == 'S':
                start = (x, y)
            elif value == 'E':
                end = (x, y)
    return start, end

def bfs_shortest_path(data: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> int:
    queue = deque([(start, 0)])
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        (x, y), distance = queue.popleft()
        if (x, y) == end:
            return distance
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(data[0]) and 0 <= ny < len(data) and data[ny][nx] != '#':
                queue.append(((nx, ny), distance + 1))
    return -1

def main():
    data = import_data("input.txt")
    start, end = find_start_and_end(data)
    shortest_path_length = bfs_shortest_path(data, start, end)
    print(f"The shortest path length is: {shortest_path_length}")

    short_path_liste: dict[str, int] = {}

    for i in tqdm(range(1, len(data)-1)):
        for j in range(1, len(data[0])-1):
            if data[i][j] == '#':
                new_data = deepcopy(data)
                new_data[i][j] = '.'
                new_shortest_path_length = bfs_shortest_path(new_data, start, end)
                if new_shortest_path_length != -1 and new_shortest_path_length < shortest_path_length:
                    # print(f"new path length is : {new_shortest_path_length} shorter of {shortest_path_length - new_shortest_path_length}")
                    if shortest_path_length - new_shortest_path_length >= 100:
                        if str(shortest_path_length - new_shortest_path_length) in short_path_liste:
                            short_path_liste[str(shortest_path_length - new_shortest_path_length)] += 1
                        else:
                            short_path_liste[str(shortest_path_length - new_shortest_path_length)] = 1
    print(f"Shortest path lengths that are one step shorter than the shortest path length: {short_path_liste}")
    print(f"Total count of these shortest path lengths: {sum(short_path_liste.values())}")

if __name__ == "__main__":
    main()