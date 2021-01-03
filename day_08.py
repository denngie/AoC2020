#!/usr/bin/python3
""" Day 8: Handheld Halting """
from aocd import get_data


def parse_input(puzzle_data):
    """ Return puzzle in structured data form """
    structured_puzzle = list()
    for line in puzzle_data.split("\n"):
        structured_puzzle.append(line.split(" "))

    return structured_puzzle


def fix_instruction(code):
    """ Try to fix the broken code """
    iterator = 0
    accumulator = 0
    while iterator < len(code):
        argument = code[iterator][0]
        if argument == "jmp":
            code[iterator][0] = "nop"
        elif argument == "nop":
            code[iterator][0] = "jmp"
        try:
            accumulator = process_instructions(code)
            break
        except SystemError:
            # Reset changed argument and continue
            code[iterator][0] = argument
            iterator += 1
            continue
    return accumulator


def process_instructions(code):
    """ Execute instruction """
    iterator = 0
    accumulator = 0
    parsed_instructions = list()
    while iterator < len(code):
        argument = code[iterator][0]
        value = code[iterator][1]

        if iterator in parsed_instructions:
            # print("Loop detected! Last value was {}".format(accumulator))
            raise SystemError
        parsed_instructions.append(iterator)

        operation = value[0]
        number = int(value[1:])
        if operation == "+":
            if argument == "jmp":
                iterator += number
            elif argument == "acc":
                accumulator += number
        elif operation == "-":
            if argument == "jmp":
                iterator -= number
            elif argument == "acc":
                accumulator -= number
        if argument != "jmp":
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
    puzzle_input = parse_input(get_data(day=8))
    print(fix_instruction(puzzle_input))


if __name__ == "__main__":
    main()
