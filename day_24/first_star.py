def import_data(path: str) -> tuple[dict[str, bool], list[list[str]]]:
    memory = {}
    instructions = []
    with open(path, 'r') as file:
        raw = file.read().split("\n\n")
        for line in raw[0].split("\n"):
            data = line.strip().split(": ")
            memory[data[0]] = bool(int(data[1]))
        for line in raw[1].split("\n"):
            instructions.append(line.strip().split(" "))
    return memory, instructions

def process_instruction(instruction: list[str], memory: dict[str, bool]) -> dict[str, bool]:
    result = {}
    input_1, input_2 = instruction[0], instruction[2]
    gate = instruction[1]
    output = instruction[4]
    if gate == "AND":
        result[output] = memory[input_1] and memory[input_2]
    elif gate == "OR":
        result[output] = memory[input_1] or memory[input_2]
    elif gate == "XOR":
        result[output] = memory[input_1] ^ memory[input_2]
    return result

def main():
    memory, instructions = import_data("input.txt")
    print(memory)
    print(instructions)
    while len(instructions) > 0:
        instruction = instructions.pop(0)
        if instruction[0] in memory and instruction[2] in memory:
            memory.update(process_instruction(instruction, memory))
        else:
            instructions.append(instruction)
    print(memory)
    result = ""
    temp_result = []
    for key, value in memory.items():
        if key.startswith("z"):
            temp_result.append((key, value))
    temp_result.sort(key=lambda x: int(x[0][1:]), reverse=True)
    for key, value in temp_result:
        result += str(int(value))
    print(temp_result)
    print(result)
    print(int(result, 2))

if __name__ == "__main__":
    main()