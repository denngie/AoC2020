#!/usr/bin/python3
""" Day 10: Adapter Array """
from aocd import get_data


def parse_input(puzzle_data):
    """ Return puzzle in structured data form """
    structured_puzzle = list()
    for line in puzzle_data.split("\n"):
        structured_puzzle.append(int(line))

    return structured_puzzle


def calculate_deltajoltage(adapters):
    """ Find the number of deltas and multiply them """
    diff = {"1": 0, "3": 0}
    adapters.sort()
    prev_jolt = 0
    for adapter in adapters:
        if adapter - prev_jolt == 1:
            diff["1"] += 1
        elif adapter - prev_jolt == 3:
            diff["3"] += 1
        prev_jolt = adapter
    # Device is always +3 compared to last adapter
    diff["3"] += 1

    return diff["1"] * diff["3"]


def calculate_combos(adapters):
    """ Calculate number of combos to last adapter """
    adapters.append(0)
    adapters.sort()
    combinations = dict.fromkeys(adapters, 0)
    combinations[0] = 1
    for adapter in adapters:
        for diff in range(1, 4):
            if adapter + diff in adapters:
                combinations[adapter + diff] += combinations[adapter]

    return combinations[adapters[-1]]


def main():
    """ Solve the puzzle """
    puzzle_input = parse_input(get_data(day=10))
    print(calculate_deltajoltage(puzzle_input))
    print(calculate_combos(puzzle_input))


if __name__ == "__main__":
    main()
