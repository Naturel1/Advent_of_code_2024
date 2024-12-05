def import_data(path: str) -> list[list[str]]:
    with open(path, 'r') as file:
        result = []
        for line in file:
            result.append(list(line.strip()))
        return result


def xmas_count(data: list[list[str]]) -> int:
    result = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "A":
                result += xmas_find(data, x, y)
    return result

def xmas_find(data: list[list[str]], x: int, y: int) -> int:
    if 1 <= y < len(data) - 1 and 1 <= x < len(data[0]) - 1:
        if data[y-1][x-1] == "M" and data[y+1][x+1] == "S" and data[y-1][x+1] == "S" and data[y+1][x-1] == "M" or \
           data[y-1][x-1] == "S" and data[y+1][x+1] == "M" and data[y-1][x+1] == "M" and data[y+1][x-1] == "S" or \
           data[y-1][x-1] == "M" and data[y+1][x+1] == "S" and data[y-1][x+1] == "M" and data[y+1][x-1] == "S" or \
           data[y-1][x-1] == "S" and data[y+1][x+1] == "M" and data[y-1][x+1] == "S" and data[y+1][x-1] == "M":
            print(f"""{data[y-1][x-1]}.{data[y-1][x+1]}
.{data[y][x]}.
{data[y+1][x-1]}.{data[y+1][x+1]}""")
            return 1
    return 0


def main():
    data: list[list[str]] = import_data('input.txt')
    result: int = xmas_count(data)
    print(f"the result is : {result}")


if __name__ == "__main__":
    main()