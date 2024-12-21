KEYPAD = {'7':(0,0),'8':(0,1),'9':(0,2),
          '4':(1,0),'5':(1,1),'6':(1,2),
          '1':(2,0), '2':(2,1),'3':(2,2),
          '0':(3,1), 'A':(3,2)}
KEYPAD_2 = [['7','8','9'],
            ['4','5','6'],
            ['1','2','3'],
            [None,'0','A']]
ROBOT_KEYPAD = {'^':(0,1),'<':(1,0),'>':(1,2),'v':(1,1), 'A':(0,2)}
ROBOT_KEYPAD_2 = [[None, '^', 'A'],
                ['<', 'v', '>']]

def import_data(path: str) -> list[list[str]]:
    result = []
    with open(path, 'r') as file:
        for line in file:
            result.append(list(line.strip()))
        return result

def find_moves(code: list[str]) -> list[str]:
    result = []
    if code[0].isdigit():
        pad = KEYPAD
    else:
        pad = ROBOT_KEYPAD
    y, x = pad['A']
    for digit in code:
        ay, ax = pad[digit]
        if  ay < y:
            result.extend(['^'] * abs(ay-y))
        elif ay > y:
            result.extend(['v'] * abs(ay-y))
        if ax > x:
            result.extend(['>'] * abs(ax-x))
        elif ax < x:
            result.extend(['<'] * abs(ax-x))
        result.append('A')
        if digit != 'A':
            y, x = ay, ax
    return result

def main():
    data = import_data('input.txt')
    print(data)
    final = {}
    for code in data:
        print(''.join(code))
        robot_1 = find_moves(code)
        print(''.join(robot_1))
        robot_2 = find_moves(robot_1)
        print(''.join(robot_2))
        final[''.join(code)] = find_moves(robot_2)
        print(''.join(final[''.join(code)]))
    result = 0
    for key, value in final.items():
        print(f"{int(key[0:-1])}: {len(value)} = {len(value) * int(key[0:-1])}")
        result += len(value) * int(key[0:-1])
    print(f"Part 1: {result}")
if __name__ == "__main__":
    main()