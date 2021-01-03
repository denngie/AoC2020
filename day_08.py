#!/usr/bin/python3
""" Day 8: Handheld Halting """
from aocd import get_data


def parse_input(puzzle_data):
    """ Return puzzle in structured data form """
    structured_puzzle = list()
    for line in puzzle_data.split("\n"):
        structured_puzzle.append(line.split(" "))

    return structured_puzzle


def execute_instructions(code):
    """ Return accumulator after code has been executed """
    accumulator = 0
    parsed_instructions = list()
    iterator = 0
    previous_iterator = 0
    while iterator < len(code):
        argument = code[iterator][0]

        if iterator in parsed_instructions:
            print("Loop detected, changing previous step")
            if code[previous_iterator][0] == "jmp":
                argument = "nop"
            else:
                argument = "jmp"
            print("Current: {}, previous: {}".format(iterator, previous_iterator))
            break
            iterator = previous_iterator
        else:
            parsed_instructions.append(iterator)

        value = code[iterator][1]
        if argument == "jmp":
            previous_iterator = iterator
            iterator = eval("{} {}".format(iterator, value))
            continue
        if argument == "acc":
            accumulator = eval("{} {}".format(accumulator, value))
        if argument == "nop":
            previous_iterator = iterator
        iterator += 1
    return accumulator


def process_instructions(code):
    """ Execute instruction """
    accumulator = 0
    parsed_instructions = list()
    iterator = 0
    while iterator < len(code):
        argument = code[iterator][0]
        value = code[iterator][1]

        if iterator in parsed_instructions:
            print("Loop detected!")
            break
        else:
            parsed_instructions.append(iterator)

        if argument == "jmp":
            iterator = eval("{} {}".format(iterator, value))
            continue
        if argument == "acc":
            accumulator = eval("{} {}".format(accumulator, value))
        iterator += 1
    return accumulator


def main():
    """ Solve the puzzle """
    puzzle_input = parse_input("nop +0\n"
                               "acc +1\n"
                               "jmp +4\n"
                               "acc +3\n"
                               "jmp -3\n"
                               "acc -99\n"
                               "acc +1\n"
                               "jmp -4\n"
                               "acc +6")
    # puzzle_input = parse_input(get_data(day=8))
    print(process_instructions(puzzle_input))


if __name__ == "__main__":
    main()
