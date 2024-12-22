def import_data(path: str) -> list[int]:
    return list(map(int, open(path, 'r').read().split()))

def step_1(number: int, seed: int) -> int:
    return ((number * 64) ^ number) % 16777216

def step_2(number: int, seed: int) -> int:
    return ((number // 32) ^ number) % 16777216

def step_3(number: int, seed: int) -> int:
    return ((number * 2048) ^ number) % 16777216

def pseudorandom(seed: int, iterations: int) -> int:
    result = -1
    start = seed
    for i in range(iterations):
        temp_1 = step_1(start, seed)
        temp_2 = step_2(temp_1, seed)
        result = step_3(temp_2, seed)
        start = result
        # print(f"Iteration {i+1}: {result}")
    return result

def main():
    data = import_data('input.txt')
    result = 0
    for seed in data:
        pseudorandom_result = pseudorandom(seed, 2000)
        print(f"{seed}: {pseudorandom_result}")
        result += pseudorandom_result
    print()
    print(f"Final result: {result}")


if __name__ == "__main__":
    main()