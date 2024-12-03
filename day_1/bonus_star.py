def import_problem_input(path: str) -> list[list]:
    with open(path, 'r') as file:
        listes = [[], []]
        for line in file:
            split_line = line.split()
            listes[0].append(int(split_line[0]))
            listes[1].append(int(split_line[1]))
    return listes

def process_lists(listes: list) -> list:
    result = []
    for i in range(len(listes[0])):
        result.append(listes[0][i] * listes[1].count(listes[0][i]))
    return result

def main():
    listes = import_problem_input('input.txt')
    processed_lists = process_lists(listes)
    print(sum(processed_lists))

if __name__ == "__main__":
    main()