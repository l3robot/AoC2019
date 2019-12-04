"""Script for day 3 of the 2019 Advent of Code"""

import itertools


with open('day03/data.csv', 'r') as f:
    DATA = f.read()


def decode_direction(direction):
    direction, step = direction[0], int(direction[1:])
    sign = -1 if direction in ['L', 'D'] else 1
    idx = 1 if direction in ['R', 'L'] else 0
    return idx, sign, step


def walk(directions):
    total = [0, 0]
    for direction in iter(directions):
        idx, sign, step = decode_direction(direction)
        for _ in range(step):
            total[idx] += sign
            yield tuple(total)


def manhattan(pts0, pts1):
    return abs(pts1[0] - pts0[0]) + abs(pts1[1] - pts0[1])


def manhattan_from_origin(pts):
    return manhattan(pts, [0, 0])


def reduce_distance(pts_list):
    if len(pts_list) == 1:
        return manhattan_from_origin(pts_list[0])
    else:
        sub_distance = reduce_distance(pts_list[:-1])
        return manhattan(pts_list[-1], pts_list[-2]) + sub_distance


if __name__ == '__main__':
    wire0, wire1 = map(lambda x: x.split(','), DATA.split('\n'))
    wire0_walk, wire1_walk = list(walk(wire0)), list(walk(wire1))
    intersec = list(set(wire0_walk) & set(wire1_walk))
    min_distance = min(map(manhattan_from_origin, intersec))
    print(f'The minimal distance for interesections is {min_distance}')
    wire0_intersec_idx = list(map(wire0_walk.index, intersec))
    wire1_intersec_idx = list(map(wire1_walk.index, intersec))
    sum_idx = list(map(lambda x, y: x + y, wire0_intersec_idx, wire1_intersec_idx))
    argmin = sum_idx.index(min(sum_idx))
    min_delay = 2 + wire0_intersec_idx[argmin] + wire1_intersec_idx[argmin]
    print(f'The minimal delay for interesections is {min_delay}')

