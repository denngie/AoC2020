#!/usr/bin/python3
""" Day 4: Passport Processing """
from re import split as re_split, search as re_search
from aocd import get_data


def parse_input(puzzle_data):
    """ Return puzzle in structured data form """
    structured_puzzle = list()
    for line in puzzle_data.split("\n\n"):
        passport = dict()
        for data in re_split(r"\s|\\n", line):
            key, value = data.split(":")
            passport[key] = value
        structured_puzzle.append(passport)

    return structured_puzzle


def count_valid_passports(passports):
    """ Validate passports based on number of fields with cid optional """
    count = 0
    for passport in passports:
        if (len(passport) == 8 or
                (len(passport) == 7 and "cid" not in passport)):
            if int(passport["byr"]) not in range(1920, 2003):
                continue
            if int(passport["iyr"]) not in range(2010, 2021):
                continue
            if int(passport["eyr"]) not in range(2020, 2031):
                continue
            if ("cm" in passport["hgt"][-2:] and
                    int(passport["hgt"][:-2]) not in range(150, 194)):
                continue
            if ("in" in passport["hgt"][-2:] and
                    int(passport["hgt"][:-2]) not in range(59, 77)):
                continue
            if not passport["hgt"][-2:] in ["cm", "in"]:
                continue
            if not re_search(r"^#[0-9a-f]{6}$", passport["hcl"]):
                continue
            if not passport["ecl"] in ["amb", "blu", "brn", "gry",
                                       "grn", "hzl", "oth"]:
                continue
            if not re_search(r"^[0-9]{9}$", passport["pid"]):
                continue
            count += 1

    return count


if __name__ == "__main__":
    PUZZLE_INPUT = parse_input(get_data(day=4))
    print(count_valid_passports(PUZZLE_INPUT))
