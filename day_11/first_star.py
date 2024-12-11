def import_data(path: str) -> list[str]:
    with open(path, 'r') as file:
        return list(file.read().strip().split(" "))

def blinking(data: list[str]) -> list[str]:
    result = []
    for stone in data:
        if len(stone) % 2 == 0:
            middle = len(stone) // 2
            result.append(str(int(stone[:middle])))
            result.append(str(int(stone[middle:])))
        elif stone == "0":
            result.append("1")
        else:
            result.append(str(int(stone) * 2024))
    return result

def main():
    data = import_data("input.txt")
    print(f"Initial arrangement: \n{data}\n")
    next_blink = data
    for i in range(25):
        blinking_stones = blinking(next_blink)
        next_blink = blinking_stones
        print(f"After {i+1} blinks: \n{blinking_stones}\n")
    print(f"The final result is : {len(blinking_stones)} stones")


if __name__ == "__main__":
    main()