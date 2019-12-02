"""Script for day 2 of the 2019 Advent of Code"""


with open('day02/data.csv', 'r') as f:
    DATA = f.read()


def add(mem, addr1, addr2, retaddr):
    mem[retaddr] = mem[addr1] + mem[addr2]


def mult(mem, addr1, addr2, retaddr):
    mem[retaddr] = mem[addr1] * mem[addr2]


lookup_table = {
    1: add,
    2: mult,
}


def run(mem):
    mem = list(mem)
    for i in range(0, len(mem), 4):
        opcode, param1, param2, param3 = mem[i:i+4]
        if opcode == 99:
            break
        op = lookup_table[opcode]
        op(mem, param1, param2, param3)
    return mem[0]


if __name__ == '__main__':
    init_mem = [int(c) for c in DATA.split(',')]
    ret = run(init_mem)
    print('The value at addr 0 is', ret)

    for i in range(100):
        for j in range(100):
            mem = init_mem
            mem[1], mem[2] = i, j
            ret = run(mem)
            if ret == 19690720:
                print('The good pair yields', 100 * i + j)
                break