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

def find_lan(connections: dict[str, list[str]]) -> list(set[str]):
    result = []
    for c1 in connections:
        lan = {c1}
        for c2 in connections[c1]:
            for l in lan:
                if l not in connections[c2]:
                    break
            else:
                lan.add(c2)
        result.append(lan)
    return result


def main():
    data, connections = import_data('input.txt')
    print(len(data))
    print(connections)
    three_computers = find_lan(connections)
    print(three_computers)
    lans = find_lan(connections)
    bigger_lan = max(lans, key=len)
    print(f"The bigger lan is : {bigger_lan}")
    result = ""
    for x in sorted(bigger_lan):
        result += x + ","
    print(f"The password of the lan is : {result}")

if __name__ == "__main__":
    main()