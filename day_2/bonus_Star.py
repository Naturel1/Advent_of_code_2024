import os

DATA_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

def import_data(path: str) -> list[list[int]]:
    result = []
    with open(path, 'r') as file:
        for line in file:
            result.append([int(x) for x in line.split()])
        return result

def check_asc_or_desc(row: list[int]) -> bool:
    asc_or_desc = [0, 0]
    for i in range(len(row) - 1):
        if row[i] < row[i + 1]:
            asc_or_desc[0] += 1
        else:
            asc_or_desc[1] += 1
    if asc_or_desc[0] > asc_or_desc[1]:
        return True
    else:
        return False

def safety_check(row: list[int]) -> tuple[bool, int]:
    for i in range(len(row) - 1):
        if abs(row[i] - row[i + 1]) > 3 or abs(row[i] - row[i + 1]) == 0:
            return False, i
        if check_asc_or_desc(row):
            if row[i] > row[i + 1]:
                return False, i
        else:
            if row[i] < row[i + 1]:
                return False, i
    return True, -1

def main():
    data: list[list[int]] = import_data(DATA_PATH)
    solution = 0
    for row in data:
        print(f"Row: {row}")
        result, index = safety_check(row)
        if result:
            solution += 1
            print(f"Row {row} is safe.")
        else:
            print(f"row {row} is not safe. Swapping elements {row[index]} and {row[index+1]} will make it safe.")
            row_2 = row.copy()
            row_3 = row.copy()
            row_2.pop(index)
            row_3.pop(index+1)
            result_2, index = safety_check(row_2)
            result_3, index = safety_check(row_3)
            if result_2 or result_3:
                solution += 1
                print(f"Row become safe is safe.")
    print(f"The solution is: {solution}")

if __name__ == "__main__":
    main()