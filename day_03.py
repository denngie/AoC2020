#!/usr/bin/python3
""" Day 3: Toboggan Trajectory """
from aocd import get_data


def parse_input(puzzle_data):
    """ Return puzzle in structured data form """
    structured_puzzle = list()
    for line in puzzle_data.split("\n"):
        structured_puzzle.append(line)
    return structured_puzzle


def calculate_collisions(toboggan_map, step_x, step_y):
    """ Calculate amount of collisions with trees """
    count = 0
    posx = step_x
    for line in toboggan_map[1:]:
        if toboggan_map.index(line) % step_y == 0:
            if line[posx % len(line)] == "#":
                count += 1
            posx += step_x
    return count


def main():
    """ Solve the puzzle """
    puzzle_input = parse_input(get_data(day=3))
    answer = 1
    for step_x, step_y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        answer = answer * calculate_collisions(puzzle_input, step_x, step_y)
    print(answer)


if __name__ == "__main__":
    main()
