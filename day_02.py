#!/usr/bin/python3
""" Day 2: Password Philosophy """
from re import compile as re_compile
from common import read_input


def format_puzzle(unstructured_puzzle):
    """ Return puzzle in structured data form """
    structured_puzzle = list()
    pattern = re_compile(r"^(?P<min>\d+)-(?P<max>\d+)\s"
                         r"(?P<char>\w):\s(?P<password>\w+)$")
    for line in unstructured_puzzle:
        matches = pattern.search(line)
        structured_puzzle.append({"min": int(matches.group("min")),
                                  "max": int(matches.group("max")),
                                  "char": matches.group("char"),
                                  "password": matches.group("password")})
    return structured_puzzle


def validate_passwords(password_list):
    """ Find valid passwords with min and max count """
    count = 0
    for password in password_list:
        if (password["min"] <= password["password"].count(password["char"]) <=
                password["max"]):
            count += 1
    return count


def validate_passwords2(password_list):
    """ Find valid passwords with min and max as char positions """
    count = 0
    for password in password_list:
        if ((password["password"][password["min"]-1] == password["char"]) !=
                (password["password"][password["max"]-1] == password["char"])):
            count += 1
    return count


if __name__ == "__main__":
    PUZZLE_INPUT = read_input("day_02.txt")
    PUZZLE_INPUT = format_puzzle(PUZZLE_INPUT)
    print(validate_passwords(PUZZLE_INPUT))
    print(validate_passwords2(PUZZLE_INPUT))
