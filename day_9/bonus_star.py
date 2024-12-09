import re
from copy import deepcopy

from tqdm import tqdm


def import_data(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()

def convert_to_disk_space(data: str) -> list[str]:
    result  = []
    curent_number = 0
    for i in range(len(data)):
        if i % 2 == 0:
            for _ in range(int(data[i])):
                result.append(str(curent_number))
            curent_number += 1
        else:
            for _ in range(int(data[i])):
                result.append('.')
    return result

def convert_format(data: str) -> list[list[str, int]]:
    pattern = r'((.)\2*)'
    matches = re.findall(pattern, ''.join(data))
    result = [[match[1], len(match[0])] for match in matches]
    return result

def unconvert_format(data: list[list[str, int]]) -> list[str]:
    result = []
    for item in data:
        result += [item[0]] * item[1]
    return result

def optimize_space(disk_space: list[str]) -> list[str]:
    result = deepcopy(disk_space)
    for i in tqdm(range(len(result)-1, -1, -1)):
        if result[i]!= '.':
            count_i = result.count(result[i])
            for j in range(len(result)):
                if result[j] == '.' and i > j:
                    is_free = True
                    for k in range(j, j + count_i):
                        if result[k]!= '.':
                            is_free = False
                            break
                    if is_free:
                        result[j:j + count_i], result[(i+1)-count_i:i+1] = [result[i]] * count_i, [result[j]] * count_i
                        # print(''.join(result))
                        break
    return result

def calculate_checksum(disk_space: list[str]) -> int:
    result = 0
    for i in range(len(disk_space)):
        if disk_space[i]== '.':
            continue
        result += i * int(disk_space[i])
    return result

def main():
    data = import_data('input.txt')
    disk_space = convert_to_disk_space(data)
    print(data)
    print(''.join(disk_space))
    optimized_disk = optimize_space(disk_space)
    # print("\n" + ''.join(optimized_disk))
    print(f"Checksum : {calculate_checksum(optimized_disk)}")

if __name__ == "__main__":
    main()