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
            if not 1920 <= int(passport["byr"]) <= 2002:
                continue
            if not 2010 <= int(passport["iyr"]) <= 2020:
                continue
            if not 2020 <= int(passport["eyr"]) <= 2030:
                continue
            if not passport["hgt"][-2:] in ["cm", "in"]:
                continue
            if ("cm" in passport["hgt"][-2:] and
                    not 150 <= int(passport["hgt"][:-2]) <= 193):
                continue
            if ("in" in passport["hgt"][-2:] and
                    not 59 <= int(passport["hgt"][:-2]) <= 76):
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
