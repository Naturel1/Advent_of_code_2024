def import_data(path: str) -> list[list[str]]:
    with open(path, 'r') as file:
        result = []
        for line in file:
            result.append(list(line.strip()))
        return result

def is_adjacent(land1: set[tuple[int, int]], land2: set[tuple[int, int]]) -> bool:
    for land1_x, land1_y in land1:
        if (land1_x + 1, land1_y) in land2 \
            or (land1_x - 1, land1_y) in land2 \
            or (land1_x, land1_y + 1) in land2 or \
            (land1_x, land1_y - 1) in land2:
            return True
    return False

def organize_data(_data: list[list[str]]) -> dict[str, list[set[tuple[int, int]]]]:
    result = {}
    for i in range(len(_data)):
        for j in range(len(_data[i])):
            if _data[i][j] not in result:
                result[_data[i][j]] = [{(i, j)}]
            else:
                for land in result[_data[i][j]]:
                    if (i+1, j) in land or (i-1, j) in land or (i, j+1) in land or (i, j-1) in land:
                        land.add((i, j))
                        break
                else:
                    result[_data[i][j]].append({(i, j)})
    running = True
    while running:
        running = False
        for x in result:
            breaking = False
            if len(result[x]) > 1:
                for i in range(len(result[x])):
                    for j in range(len(result[x])):
                        if i == j:
                            continue
                        if is_adjacent(result[x][i], result[x][j]):
                            result[x][i] = result[x][i].union(result[x][j])
                            result[x].pop(j)
                            running = True
                            breaking = True
                            break
                    if breaking:
                        break
    return result



def calculate_air(_data: set[tuple[int, int]]) -> int:
    return len(_data)

def calculate_perimeter(_data: set[tuple[int, int]]) -> int:
    perimeter = 0
    for land in _data:
       for i, j in [(land[0]+1, land[1]), (land[0]-1, land[1]), (land[0], land[1]+1), (land[0], land[1]-1)]:
           if (i, j) not in _data:
               perimeter += 1
    return perimeter



def main():
    data = import_data("input.txt")
    organized_data = organize_data(data)
    print(organized_data)
    result = 0
    for type, lands in organized_data.items():
        for land in lands:
            result += calculate_air(land) * calculate_perimeter(land)
            print(f"Type: {type}, Air: {calculate_air(land)}, Perimeter: {calculate_perimeter(land)} total : {calculate_air(land) * calculate_perimeter(land)}")
    print(f"The result is : {result}")

if __name__ == "__main__":
    main()