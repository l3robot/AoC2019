"""Script for day 4 of the 2019 Advent of Code"""

from collections import Counter
import operator as op

MIN_NUM = 265275
MAX_NUM = 781584


def check_passwd_validity(passwd):
    digits = list(map(int, list(str(passwd))))
    at_least_repeated = len(set(digits)) < len(digits)
    never_decrease = all(map(op.ge, digits[1:], digits[:-1]))
    # at least repeated number and never decrease mean two adjacents.
    return at_least_repeated and never_decrease


def check_passwd_validity_v2(passwd):
    digits = list(map(int, list(str(passwd))))
    counts = list(Counter(digits).values())
    at_least_pairs = 2 in counts
    never_decrease = all(map(op.ge, digits[1:], digits[:-1]))
    return at_least_pairs and never_decrease


if __name__ == '__main__':
    passwds = list(range(MIN_NUM, MAX_NUM+1))
    valid_passwds = list(filter(check_passwd_validity, passwds))
    num_valid_passwds = len(valid_passwds)
    print(f'There is {num_valid_passwds} different valid passwords')
    valid_passwds_v2 = list(filter(check_passwd_validity_v2, passwds))
    num_valid_passwds_v2 = len(valid_passwds_v2)
    print(f'There is {num_valid_passwds_v2} different valid v2 passwords')
