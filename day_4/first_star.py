

def import_data(path: str) -> list[list[str]]:
    with open(path, 'r') as file:
        result = []
        for line in file:
            result.append(list(line.strip()))
        return result


def xmas_count(data: list[list[str]]) -> int:
    result: int = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "X":
                result += xmas_find(data, x, y)
    return result

def xmas_find(data: list[list[str]], x: int, y: int) -> int:
    count: int = 0
    word: str = "XMAS"
    for dx, dy in [(1, 1), (-1, -1), (0, 1), (0, -1), (1, -1), (-1, 1), (-1, 0), (1, 0)]:
        for i in range(0, len(word)):
            nx: int = x + dx * i
            ny: int = y + dy * i
            if 0 > ny or ny >= len(data) or 0 > nx or nx >= len(data[0]) or data[ny][nx] != word[i]:
                break
        else:
            count += 1
            print(f"Found {word} at ({x}, {y})")
    return count


def main():
    data: list[list[str]] = import_data('input.txt')
    result: int = xmas_count(data)
    print(f"the result is : {result}")


if __name__ == "__main__":
    main()