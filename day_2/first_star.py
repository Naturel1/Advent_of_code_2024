import os

DATA_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

def import_data(path: str) -> list[list[int]]:
    result = []
    with open(path, 'r') as file:
        for line in file:
            result.append([int(x) for x in line.split()])
        return result

def safety_check_count(data: list[list[int]]) -> int:
    result = 0
    for row in data:
        if row == sorted(row) or row == sorted(row, reverse=True):
            good_row = True
            for x in range(len(row) - 1):
                if abs(row[x] - row[x+1]) > 3 or abs(row[x] - row[x+1]) == 0:
                    good_row = False
                    break
            if good_row:
                result += 1
        else:
            continue
    return result

def main():
    data = import_data(DATA_PATH)
    solution = safety_check_count(data)
    print(f"the solution is : {solution}")

if __name__ == "__main__":
    main()