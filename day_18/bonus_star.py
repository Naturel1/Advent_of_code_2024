from collections import deque

from tqdm import tqdm

MAP_SIZE = 71

def import_data(path: str) -> list[tuple[int, int]]:
    with open(path, 'r') as file:
        result = []
        for line in file:
            coords = tuple(map(int, line.strip().split(',')))
            result.append(coords)
        return result

def find_shortest_path(map_data: list[list[str]]) -> int:
    rows, cols = len(map_data), len(map_data[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)

    queue = deque([(start, 0)])
    visited = set([start])

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        (x, y), dist = queue.popleft()

        if (x, y) == end:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and map_data[nx][ny] != '#' and (nx, ny) not in visited:
                queue.append(((nx, ny), dist + 1))
                visited.add((nx, ny))

    return -1

def create_map(data: list[tuple[int, int]]) -> list[list[str]] | tuple[int, int]:
    map_memory = [['.' for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]
    for x, y in tqdm(data):
        map_memory[y][x] = '#'
        path = find_shortest_path(map_memory)
        if path == -1:
            return x,y
    return map_memory

def main():
    data = import_data('input.txt')
    memory_space = create_map(data)
    print(memory_space)
if __name__ == "__main__":
    main()