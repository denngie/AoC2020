#!/usr/bin/python3
""" Day 1: Report Repair """
from aocd import get_data


def parse_input(puzzle_data):
    """ Format the data from aocd """
    output = list()
    for line in puzzle_data.split("\n"):
        output.append(int(line))
    return output


def find_two_expenses(expenses, year):
    """ Find two expenses """
    for expense in expenses:
        if year - expense in expenses:
            return expense * (year - expense)
    return None


def find_three_expenses(expenses, year):
    """ Find three expenses """
    for exp_index, expense in enumerate(expenses):
        potential_expenses = [i for i in expenses[exp_index+1:] if i < year]
        for expence2 in potential_expenses:
            if year - expense - expence2 in expenses:
                return expense * (expence2) * (year - expense - expence2)
    return None


if __name__ == "__main__":
    PUZZLE_INPUT = parse_input(get_data(day=1))
    print(find_two_expenses(PUZZLE_INPUT, 2020))
    print(find_three_expenses(PUZZLE_INPUT, 2020))
