def import_input(path: str) -> list[list[str]]:
    with open(path, 'r') as file:
        result = []
        for line in file:
            result.append(list(line.strip()))
        return result

def visualize_data(data: list[list[str]]) -> str:
    result = ""
    for row in data:
        result += "".join(row) + "\n"
    return result

def search_antenna(data: list[list[str]]) -> dict[str, list[tuple[int, int]]]:
    result = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != '.':
                if data[i][j] not in result:
                    result[data[i][j]] = [(i, j)]
                else:
                    result[data[i][j]].append((i, j))
    return result

def calculate_distance(antenna1: tuple[int, int], antenna2: tuple[int, int]) -> tuple[int, int]:
    return antenna1[0] - antenna2[0], antenna1[1] - antenna2[1]

def is_in_table(coord: tuple[int, int], table_max: tuple[int, int]) -> bool:
    return 0 <= coord[0] < table_max[0] and 0 <= coord[1] < table_max[1]

def count_antinode(antennas: dict[str, list[tuple[int, int]]], table_max: tuple[int, int]) -> list[tuple[int, int]]:
    result = []
    _data = []
    for i in range(table_max[0]):
        _data.append(['.'] * table_max[1])
    for x in antennas:
        for antenna in antennas[x]:
            _data[antenna[0]][antenna[1]] = x
            for antenna2 in antennas[x]:
                if antenna not in result:
                    result.append(antenna)
                dx, dy = calculate_distance(antenna, antenna2)
                if dx == dy == 0:
                    continue
                antinode = antenna[0] + dx, antenna[1] + dy
                while is_in_table(antinode, table_max):
                    if antinode not in result:
                        # print(antinode)
                        result.append(antinode)
                        _data[antinode[0]][antinode[1]] = '#'

                    antinode = antinode[0] + dx, antinode[1] + dy
    print(visualize_data(_data))
    return result


def main():
    data = import_input('input.txt')
    table_max = (len(data[0]), len(data))
    antennas = search_antenna(data)
    result = count_antinode(antennas, table_max)
    print(f"The result is : {len(result)}")
if __name__ == "__main__":
    main()