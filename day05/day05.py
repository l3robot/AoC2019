"""Script for day 5 of the 2019 Advent of Code"""


with open('day05/data.csv', 'r') as f:
    DATA = f.read()


def print_instruction(ptr, mem, op_length):
    instruction_print = ' '.join(map(str, mem[ptr:ptr+op_length]))
    print(f'* Running instruction {instruction_print}')


def add(ptr, mem):
    op_length = 4
    print_instruction(ptr, mem, op_length)
    modes, param1, param2, retaddr = mem[ptr:ptr+op_length]
    value1 = mem[param1] if not bool(modes // 100 % 2) else param1
    value2 = mem[param2] if not bool(modes // 1000 % 2) else param2
    mem[retaddr] = value1 + value2
    return ptr + op_length


def mult(ptr, mem):
    op_length = 4
    print_instruction(ptr, mem, op_length)
    modes, param1, param2, retaddr = mem[ptr:ptr+op_length]
    value1 = mem[param1] if not bool(modes // 100 % 2) else param1
    value2 = mem[param2] if not bool(modes // 1000 % 2) else param2
    mem[retaddr] = value1 * value2
    return ptr + op_length


def io_in(ptr, mem):
    op_length = 2
    print_instruction(ptr, mem, op_length)
    _, addr = mem[ptr:ptr+op_length]
    req = input(f'< Request for input to address {addr}: ')
    mem[addr] = int(req)
    return ptr + op_length


def io_out(ptr, mem):
    op_length = 2
    print_instruction(ptr, mem, op_length)
    modes, param = mem[ptr:ptr+op_length]
    value = mem[param] if not bool(modes // 100 % 2) else param
    print(f'> Value to print {value}')
    return ptr + op_length


def jump_if_true(ptr, mem):
    op_length = 3
    modes, param1, param2 = mem[ptr:ptr+op_length]
    value1 = mem[param1] if not bool(modes // 100 % 2) else param1
    value2 = mem[param2] if not bool(modes // 1000 % 2) else param2
    return value2 if value1 != 0 else ptr + op_length


def jump_if_false(ptr, mem):
    op_length = 3
    modes, param1, param2 = mem[ptr:ptr+op_length]
    value1 = mem[param1] if not bool(modes // 100 % 2) else param1
    value2 = mem[param2] if not bool(modes // 1000 % 2) else param2
    return value2 if value1 == 0 else ptr + op_length


def less_than(ptr, mem):
    op_length = 4
    modes, param1, param2, retaddr = mem[ptr:ptr+op_length]
    value1 = mem[param1] if not bool(modes // 100 % 2) else param1
    value2 = mem[param2] if not bool(modes // 1000 % 2) else param2
    mem[retaddr] = 1 if value1 < value2 else 0
    return ptr + op_length


def equal(ptr, mem):
    op_length = 4
    modes, param1, param2, retaddr = mem[ptr:ptr+op_length]
    value1 = mem[param1] if not bool(modes // 100 % 2) else param1
    value2 = mem[param2] if not bool(modes // 1000 % 2) else param2
    mem[retaddr] = 1 if value1 == value2 else 0
    return ptr + op_length


instructions = {
    1: add,
    2: mult,
    3: io_in,
    4: io_out,
    5: jump_if_true,
    6: jump_if_false,
    7: less_than,
    8: equal,
}


def run(mem, ptr):
    opcode = mem[ptr]
    if opcode == 99:
        return
    op = instructions[opcode % 10]
    return run(mem, op(ptr, mem))


if __name__ == '__main__':
    mem = [int(c) for c in DATA.split(',')]
    run(mem, 0)
