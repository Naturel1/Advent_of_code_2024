from tqdm import tqdm


def import_data(path: str) -> dict[str, int]:
    result = {}
    with open(path, 'r') as file:
        for x in file.read().strip().split(" "):
            if x in result:
                result[x] += 1
            else:
                result[x] = 1
        return result

def process_data(_data: dict[str, int], iteration: int) -> dict[str, int]:
    result = {}

    for key, item in tqdm(_data.items(), desc=f"Iteration {iteration + 1}"):
        if key == "0":
            if "1" in result:
                result["1"] += item
            else:
                result["1"] = item
        elif len(key) % 2 == 0:
            middle = len(key) // 2
            if key[:middle] in result:
                result[key[:middle]] += item
            else:
                result[key[:middle]] = item

            new_key = str(int(key[middle:]))
            if new_key in result:
                result[new_key] += item
            else:
                result[new_key] = item
        else:
            result[str(int(key) * 2024)] = item
    return result

def main():
    data = import_data("input.txt")
    print(data)
    next_data = data
    for i in range(75):
        next_data = process_data(next_data, i)
        # print(f"iteration {i+1} : {next_data}")
    result = sum(next_data.values())
    print(result)


if __name__ == "__main__":
    main()