"""Script for day 1 of the 2019 Advent of Code"""

import math


with open('day01/data.txt', 'r') as f:
    DATA = f.read()


def compute_fuel(mass):
    """Computes the fuel needed for a certain mass without considering
    the needed fuel mass.
    """
    return mass // 3 - 2


def compute_adjusted_fuel(mass):
    """Computes the fuel needed for a certain mass, adjusting for the
    needed fuel mass.
    """
    fuel = compute_fuel(mass)
    return 0 if fuel < 0 else fuel + compute_adjusted_fuel(fuel)



if __name__ == '__main__':
    total_fuel = sum(map(
        lambda x: compute_fuel(int(x)), DATA.split('\n')))
    print(f'The total fuel mass needed is {total_fuel}')

    adj_total_fuel = sum(map(
        lambda x: compute_adjusted_fuel(int(x)), DATA.split('\n')))
    print(f'The total adjusted fuel mass needed is {adj_total_fuel}')