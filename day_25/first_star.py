def import_data(path: str) -> tuple[list[list[int]], list[list[int]]]:
    keys = []
    locks = []
    with open(path, 'r') as file:
        for pattern in file.read().split("\n\n"):
            element = [-1, -1, -1, -1, -1]
            for row in pattern.strip().split("\n"):
                for i in range(len(row)):
                    if row[i] == '#':
                        element[i] += 1
            if all(x == '#' for x in pattern[0].strip()):
                locks.append(element)
            else:
                keys.append(element)
    return keys, locks

def can_unlock(key: list[int], lock: list[int]) -> bool:
    combo = [x + y for x, y in zip(key, lock)]
    if max(combo) <= 5:
        return True
    return False

def try_keys(keys: list[list[int]], locks: list[list[int]]) -> int:
    result = 0
    for lock in locks:
        for key in keys:
            if can_unlock(key, lock):
                result += 1
    return result

def main():
    keys, locks = import_data('input.txt')
    print(f"Keys: {keys}, Locks: {locks}")
    result = try_keys(keys, locks)
    print(f"The result is : {result}")

if __name__ == "__main__":
    main()