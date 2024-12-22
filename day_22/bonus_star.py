from tqdm import tqdm


def import_data(path: str) -> list[int]:
    return list(map(int, open(path, 'r').read().split()))

def step_1(number: int) -> int:
    return ((number * 64) ^ number) % 16777216

def step_2(number: int) -> int:
    return ((number // 32) ^ number) % 16777216

def step_3(number: int) -> int:
    return ((number * 2048) ^ number) % 16777216

def pseudorandom(seed: int, iterations: int) -> list[tuple[int, int]]:
    result = []
    start = seed

    temp_1 = step_1(start)
    temp_2 = step_2(temp_1)
    temp_3 = step_3(temp_2)
    result.append((temp_3, int(str(temp_3)[-1])-int(str(seed)[-1])))
    start = result[-1][0]
    # print(f"Iteration 1: {result[0]}")

    for i in range(1, iterations-1):
        temp_1 = step_1(start)
        temp_2 = step_2(temp_1)
        temp_3 = step_3(temp_2)
        result.append((temp_3, int(str(temp_3)[-1])-int(str(result[-1][0])[-1])))
        start = result[-1][0]
        # print(f"Iteration {i+1}: {result[-1]}")
    return result

def find_best_sequence() -> list[int]:
    for i in range(-6, 6):
        for j in range(-6, 6):
            for k in range(-6, 6):
                for l in range(-6, 6):
                    sequence = [i, j, k, l]
                    yield sequence

def calculate_result(echanges: dict[int, list[tuple[int, int]]], sequence: list[int]) -> int:
    result = 0
    for echange in echanges.values():
        for i in range(3, len(echange)):
            if echange[i][1]!= sequence[3] or echange[i-1][1]!= sequence[2] or echange[i-2][1]!= sequence[1] or echange[i-3][1]!= sequence[0]:
                continue
            else:
                result += int(str(echange[i][0])[-1])
                break
    return result

def main():
    data = import_data('input.txt')
    echanges = {}
    for seed in tqdm(data, desc="Importing data" ):
        pseudorandom_result = pseudorandom(seed, 2000)
        # print(f"{seed}: {pseudorandom_result}")
        echanges[seed] = pseudorandom_result
        # result += pseudorandom_result
    best_sequence = (None, 0)
    for sequence in tqdm(find_best_sequence(), total=20736, desc="Finding best sequence"):
        temp_result = calculate_result(echanges, [-2,1,-1,3])
        if temp_result > best_sequence[1]:
            best_sequence = (sequence, temp_result)
    result = temp_result
    print()
    print(f"Final result: {result}")


if __name__ == "__main__":
    main()