from itertools import combinations
from collections import defaultdict
from functools import reduce

gWires = dict()
get_wire_cache = dict()


def get_wire(wire):
    if wire in get_wire_cache:
        return get_wire_cache[wire]

    if wire in gWires:
        result = gWires[wire]()
        get_wire_cache[wire] = result

        return result

    raise Exception('FUCK')


def do_and(wire_a, wire_b):
    return lambda: get_wire(wire_a) & get_wire(wire_b)


def do_or(wire_a, wire_b):
    return lambda: get_wire(wire_a) | get_wire(wire_b)


def do_xor(wire_a, wire_b):
    return lambda: get_wire(wire_a) ^ get_wire(wire_b)


def add_wire(wire):
    parts = wire.split(':')
    wire_name = parts[0]

    gWires[wire_name] = lambda: int(parts[1].strip())


def get_wire_number(wire):
    total = 0
    for entry in sorted(filter(lambda x: x[0] == wire, gWires.keys()), reverse=True):
        total <<= 1
        total |= gWires[entry]()
    return total


def zero_bit():
    return lambda: 0


def one_bit():
    return lambda: 1


def validate_full_adder(num):
    clear_all_inputs()

    x_wire = f'x{num:02d}'
    y_wire = f'y{num:02d}'
    z_wire = f'z{num:02d}'

    gWires[x_wire] = zero_bit()
    gWires[y_wire] = zero_bit()

    get_wire_cache.clear()
    if get_wire(z_wire) != 0:
        return False

    gWires[x_wire] = one_bit()
    gWires[y_wire] = zero_bit()

    get_wire_cache.clear()
    if get_wire(z_wire) != 1:
        return False

    gWires[x_wire] = zero_bit()
    gWires[y_wire] = one_bit()

    get_wire_cache.clear()
    if get_wire(z_wire) != 1:
        return False

    gWires[x_wire] = one_bit()
    gWires[y_wire] = one_bit()

    get_wire_cache.clear()
    if get_wire(z_wire) != 0:
        return False

    if num > 0:
        prev_x_wire = f'x{num - 1:02d}'
        prev_y_wire = f'y{num - 1:02d}'

        gWires[prev_x_wire] = one_bit()
        gWires[prev_y_wire] = one_bit()
        gWires[x_wire] = zero_bit()
        gWires[y_wire] = zero_bit()

        get_wire_cache.clear()
        if get_wire(z_wire) != 1:
            return False

        gWires[prev_x_wire] = one_bit()
        gWires[prev_y_wire] = one_bit()
        gWires[x_wire] = one_bit()
        gWires[y_wire] = zero_bit()

        get_wire_cache.clear()
        if get_wire(z_wire) != 0:
            return False

        gWires[prev_x_wire] = one_bit()
        gWires[prev_y_wire] = one_bit()
        gWires[x_wire] = zero_bit()
        gWires[y_wire] = one_bit()

        get_wire_cache.clear()
        if get_wire(z_wire) != 0:
            return False

        gWires[prev_x_wire] = one_bit()
        gWires[prev_y_wire] = one_bit()
        gWires[x_wire] = one_bit()
        gWires[y_wire] = one_bit()

        get_wire_cache.clear()
        if get_wire(z_wire) != 1:
            return False

    for entry in get_prev_wires(num):
        if entry not in get_wire_cache:
            return False

    for entry in get_next_wires(num):
        if entry in get_wire_cache:
            return False

    return True


def clear_all_inputs():
    get_wire_cache.clear()
    for key in gWires.keys():
        if key[0] == 'x' or key[0] == 'y':
            gWires[key] = zero_bit()


def get_prev_wires(num):
    while num > 0:
        yield f'x{num:02d}'
        yield f'y{num:02d}'
        num -= 1


def get_next_wires(num):
    while num > 45:
        yield f'x{num:02d}'
        yield f'y{num:02d}'
        num += 1


def exchange_wires(wire_a, wire_b):
    tmp = gWires[wire_a]
    gWires[wire_a] = gWires[wire_b]
    gWires[wire_b] = tmp


def find_full_adder_fix(current_bit, max_bit, valid_wires, current_solution):
    if current_bit >= max_bit:
        return True, current_solution

    res = validate_full_adder(current_bit)

    if res:
        return find_full_adder_fix(current_bit + 1, max_bit, valid_wires - set(get_wire_cache.keys()), current_solution)

    if len(current_solution) >= 4:
        return (False, None)

    for combo in combinations(valid_wires, 2):

        exchange_wires(*combo)
        try:
            if validate_full_adder(current_bit):

                new_valid_wires = valid_wires - {*combo}
                success, pairs = find_full_adder_fix(current_bit + 1, max_bit, new_valid_wires,
                                                     current_solution + [combo])

                if success is True:
                    return (success, pairs)

        except RecursionError:
            pass

        exchange_wires(*combo)

    return (False, None)


def main():
    data = None
    with open('input.txt', 'r') as fp:
        data = fp.readlines()
        data = map(lambda x: x.strip(), data)
        data = list(data)

    split_index = data.index('')

    wires = data[:split_index]

    for wire in wires:
        add_wire(wire)

    x_num = get_wire_number('x')
    y_num = get_wire_number('y')

    operations = data[split_index + 1:]

    for operation in operations:
        parts = operation.split('->')

        end_wire = parts[1].strip()

        wire_a, op, wire_b = tuple(parts[0].split())

        res_op = None
        if op == 'AND':
            res_op = do_and(wire_a, wire_b)
        elif op == 'OR':
            res_op = do_or(wire_a, wire_b)
        elif op == 'XOR':
            res_op = do_xor(wire_a, wire_b)

        if res_op is None:
            raise Exception('Forgot')

        gWires[end_wire] = res_op

    output_wires = set(filter(lambda x: x[0] != 'x' and x[0] != 'y', gWires.keys()))

    max_z_bit = max(map(lambda y: int(y.strip('z')), filter(lambda x: x[0] == 'z', gWires.keys())))

    success, pairs = find_full_adder_fix(0, max_z_bit, output_wires, [])

    if not success:
        print('Failed')
        return

    entries = reduce(lambda x, y: x + y, pairs)
    print(','.join(sorted(entries)))


if __name__ == '__main__':
    main()