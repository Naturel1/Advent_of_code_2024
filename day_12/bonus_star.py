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

def calculate_perimeter(_data: set[tuple[int, int]]) -> set[tuple[int, int, str]]:
    perimeter = set()
    for land in _data:
        i, j = land
        if (i+1, j) not in _data:
           perimeter.add((i+1, j, "D"))
        if (i-1, j) not in _data:
            perimeter.add((i-1, j, "U"))
        if (i, j+1) not in _data:
            perimeter.add((i, j+1, "R"))
        if (i, j-1) not in _data:
            perimeter.add((i, j-1, "L"))
    return perimeter

def is_same_side(side1: set[tuple[int, int, str]], side2: set[tuple[int, int, str]]) -> bool:
    for side in side1:
        if side[2] == "U":
            if (side[0], side[1]-1, "U") in side2 or (side[0], side[1]+1, "U") in side2:
                return True
        if side[2] == "D":
            if (side[0], side[1]-1, "D") in side2 or (side[0], side[1]+1, "D") in side2:
                return True
        if side[2] == "L":
            if (side[0]-1, side[1], "L") in side2 or (side[0]+1, side[1], "L") in side2:
                return True
        if side[2] == "R":
            if (side[0]-1, side[1], "R") in side2 or (side[0]+1, side[1], "R") in side2:
                return True
    return False

def calculate_sides(perimeter: set[tuple[int, int, str]]) -> int:
    result = []
    for land in perimeter:
        result.append({land})
    running = True
    while running:
        running = False
        breaking = False
        for i in range(len(result)):
            for j in range(len(result)):
                if i == j:
                    continue
                if is_same_side(result[i], result[j]):
                    result[i] = result[i].union(result[j])
                    result.pop(j)
                    running = True
                    breaking = True
                    break
            if breaking:
                break
    return len(result)

def main():
    data = import_data("input.txt")
    organized_data = organize_data(data)
    print(organized_data)
    result = 0

    for type, lands in organized_data.items():
        for land in lands:
            perimeter = calculate_perimeter(land)
            air = calculate_air(land)
            sides = calculate_sides(perimeter)
            result += air * sides
            print(f"Type: {type}, Air: {air}, Perimeter: {sides} total : {air * sides}")
    print(f"The result is : {result}")

if __name__ == "__main__":
    main()