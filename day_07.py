#!/usr/bin/python3
""" Day 7: Handy Haversacks """
from re import compile as re_compile
from aocd import get_data


def parse_input(puzzle_data):
    """ Return puzzle in structured data form """
    structured_puzzle = dict()
    # pattern = re_compile(r"^(\w+\s\w+)\sbags\scontain\s(?:(\d)\s(\w+\s\w+)\sbags?(?:,\s)?)+\.$")
    for line in puzzle_data.split("\n"):
        parent, children = line.split(" bags contain ")
        structured_puzzle[parent] = dict()
        structured_puzzle[parent]["children"] = list()
        # print(parent)
        for child in children.split(", "):
            if "no other bags." in child:
                structured_puzzle[parent]["children"] = None
            else:
                structured_puzzle[parent]["children"].append(child)
    return structured_puzzle


def main():
    """ Solve the puzzle """
    # puzzle_input = parse_input(get_data(day=7))
    puzzle_input = ("light red bags contain 1 bright white bag, 2 muted yellow bags.\n"
                    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n"
                    "bright white bags contain 1 shiny gold bag.\n"
                    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n"
                    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n"
                    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n"
                    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n"
                    "faded blue bags contain no other bags.\n"
                    "dotted black bags contain no other bags.")
    print(parse_input(puzzle_input))


if __name__ == "__main__":
    main()
