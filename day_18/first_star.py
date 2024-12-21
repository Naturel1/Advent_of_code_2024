from collections import deque

MAP_SIZE = 71

def import_data(path: str) -> list[tuple[int, int]]:
    with open(path, 'r') as file:
        result = []
        for line in file:
            coords = tuple(map(int, line.strip().split(',')))
            result.append(coords)
        return result

def create_map(data: list[tuple[int, int]], bytes_drop: int) -> list[list[str]]:
    map = [['.' for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]
    for i in range(bytes_drop):
        map[data[i][1]][data[i][0]] = '#'
    return map


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

def main():
    data = import_data('input.txt')
    memory_space = create_map(data, 1024)
    print('\n'.join([''.join(row) for row in memory_space]))

    shortest_path = find_shortest_path(memory_space)
    print(f"Le chemin le plus court est de {shortest_path} étapes.")

if __name__ == "__main__":
    main()