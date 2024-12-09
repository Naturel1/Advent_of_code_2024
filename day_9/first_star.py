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

def is_optimized(disk_space: list[str]) -> bool:
    pattern = r'^\d+\.*$'
    return bool(re.match(pattern, ''.join(disk_space)))

def optimize_space(disk_space: list[str]) -> list[str]:
    result = deepcopy(disk_space)
    for i in tqdm(range(len(result)-1, -1, -1)):
        if result[i] != '.':
            for j in range(len(result)):
                if result[j] == '.':
                    result[j], result[i] = result[i], result[j]
                    # print(''.join(result))
                    break
            if is_optimized(result):
                break
    return result

def calculate_checksum(disk_space: list[str]) -> int:
    result = 0
    for i in range(len(disk_space)):
        if disk_space[i]== '.':
            break
        result += i * int(disk_space[i])
    return result

def main():
    data = import_data('input.txt')
    disk_space = convert_to_disk_space(data)
    print(data)
    print(''.join(disk_space))
    optimized_disk = optimize_space(disk_space)
    print("\n" + ''.join(optimized_disk))
    print(f"Checksum : {calculate_checksum(optimized_disk)}")

if __name__ == "__main__":
    main()