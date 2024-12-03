def import_problem_input(path: str) -> list[list]:
    with open(path, 'r') as file:
        listes = [[], []]
        for line in file:
            split_line = line.split()
            listes[0].append(int(split_line[0]))
            listes[1].append(int(split_line[1]))
    return listes

def sort_lists(listes: list) -> list:
    liste_1 = sorted(listes[0])
    liste_2 = sorted(listes[1])
    return [liste_1, liste_2]

def calculate_distance(listes: list) -> list[int]:
    distances = []
    for a, b in zip(listes[0], listes[1]):
        distances.append(abs(a - b))
    return distances

def main():
    listes = import_problem_input('input.txt')
    distances = calculate_distance(sort_lists(listes))
    print(sum(distances))

if __name__ == "__main__":
    main()