#!/usr/bin/python3
""" Day 6: Custom Customs """
from aocd import get_data


def parse_input(puzzle_data):
    """ Return puzzle in structured data form """
    structured_puzzle = list()
    for line in puzzle_data.split("\n\n"):
        structured_puzzle.append(line)
    return structured_puzzle


def calculate_answers(puzzle_data):
    """ Calculate the number of unique answers per group """
    group_answers = list()
    for group in puzzle_data:
        group_answers.append(len("".join(set(group.replace("\n", "")))))
    return sum(group_answers)


def calculate_correct_answers(puzzle_data):
    """ Calculate the number of questions everyone answered in the group """
    group_answers = list()
    for group in puzzle_data:
        answers = group.split("\n")
        group_answers.append(len(list(set(answers[0]).intersection(*answers))))
    return sum(group_answers)


if __name__ == "__main__":
    PUZZLE_INPUT = parse_input(get_data(day=6))
    # PUZZLE_INPUT = parse_input("abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb")
    print(calculate_answers(PUZZLE_INPUT))
    print(calculate_correct_answers(PUZZLE_INPUT))
