#!/usr/bin/python3
""" Day 5: Binary Boarding """
from aocd import get_data


def parse_input(puzzle_data):
    """ Return puzzle in structured data form """
    structured_puzzle = list()
    for line in puzzle_data.split("\n"):
        row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
        column = int(line[7:].replace("L", "0").replace("R", "1"), 2)
        seat_id = row * 8 + column
        structured_puzzle.append(seat_id)
    return structured_puzzle


def highest_seat_id(seat_list):
    """ Find highest seat ID from binary form """
    highest_id = 0
    for seat_id in seat_list:
        if highest_id < seat_id:
            highest_id = seat_id

    return highest_id


def find_missing_id(seat_list):
    """ Find missing ID by looking for gap """
    highest_id = highest_seat_id(seat_list)
    print(highest_id)
    possible_id = list(set(range(1, highest_id)) - set(seat_list))
    for seat_id in possible_id:
        if seat_id - 1 not in seat_list:
            continue
        if seat_id + 1 not in seat_list:
            continue
        return seat_id


def main():
    """ Solve the puzzle """
    puzzle_input = parse_input(get_data(day=5))
    print(find_missing_id(puzzle_input))


if __name__ == "__main__":
    main()
