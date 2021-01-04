#!/usr/bin/python3
""" Day 9: Encoding Error """
from aocd import get_data


def parse_input(puzzle_data):
    """ Return puzzle in structured data form """
    structured_puzzle = list()
    for line in puzzle_data.split("\n"):
        structured_puzzle.append(int(line))

    return structured_puzzle


def validate_xmas(numbers, preamble=25):
    """ Validate XMAS numbers """
    for index, number in enumerate(numbers[preamble:], preamble):
        terms = [i for i in numbers[index-preamble:index] if i < number]
        for term in terms:
            if number - term in terms and term + term != number:
                break
        else:
            return number

    return False


def break_xmas(numbers, invalid_number):
    """ Find XMAS weakness """
    for index, number in enumerate(numbers):
        smallest = number
        largest = number
        total = number
        try:
            for term in numbers[index+1:]:
                if total + term <= invalid_number:
                    if term < smallest:
                        smallest = term
                    elif term > largest:
                        largest = term
                    if total + term == invalid_number:
                        break
                    if total + term < invalid_number:
                        total += term
                else:
                    # Total is to big, continue to next number in outer loop
                    raise IndexError
            break
        except IndexError:
            continue

    return smallest + largest


def main():
    """ Solve the puzzle """
    puzzle_input = parse_input(get_data(day=9))
    invalid_number = validate_xmas(puzzle_input)
    print(break_xmas(puzzle_input, invalid_number))


if __name__ == "__main__":
    main()
