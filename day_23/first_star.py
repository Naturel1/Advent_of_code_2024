from tqdm import tqdm


def import_data(path: str) -> tuple[list[tuple[str, str]], dict[str, list[str]]]:
    connections = []
    computers = {}
    with open(path, 'r') as file:
        for line in file:
            p1, p2 = line.strip().split('-')
            if p1 not in computers: computers[p1] = [p2]
            else:computers[p1].append(p2)
            if p2 not in computers:computers[p2] = [p1]
            else:computers[p2].append(p1)
            connections.append((p1, p2))
    return connections, computers

def find_three_computers(connections: dict[str, list[str]]) -> list[set[str]]:
    result = []
    for c1 in tqdm(connections):
        for c2 in connections:
            for c3 in connections:
                if (c1 in connections[c2] and c1 in connections[c3]) and\
                    (c2 in connections[c3]  and c2 in connections[c1]) and\
                    (c3 in connections[c1] and c3 in connections[c2]) and\
                    c1 != c2 != c3:
                        if {c1, c2, c3} not in result:
                            result.append({c1, c2, c3})
    return result

def find_t_computer(three_computers: list[set[str]]) -> list[set[str]]:
    result = []
    for group in three_computers:
        for computer in group:
            if computer[0] == 't':
                result.append(group)
                break
    return result


def main():
    data, connections = import_data('input.txt')
    print(len(data))
    print(connections)
    three_computers = find_three_computers(connections)
    print(three_computers)
    t_computer = find_t_computer(three_computers)
    print(f"the result is : {len(t_computer)}")

if __name__ == "__main__":
    main()