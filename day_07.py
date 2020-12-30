#!/usr/bin/python3
""" Day 7: Handy Haversacks """
from re import compile as re_compile
from aocd import get_data


class Bag():
    """ Bag object for a given colour with outer and inner references """
    def __init__(self, colour):
        self.colour = colour
        self.outer = list()
        self.inner = list()

    def add_outer(self, outer):
        """ Add outer bag to self """
        self.outer.append(outer)

    def add_inner(self, inner, amount):
        """ Add inner bag to self """
        self.inner.append([inner, amount])

    def count_outer_bag(self):
        """ Return count of all unique outer bags """
        possible_bags = self.find_outer_bag()
        return len(dict.fromkeys(possible_bags))

    def find_outer_bag(self):
        """ Find all possible outer bags """
        count = list()
        for bag in self.outer:
            count.append(bag)
            recursive = bag.find_outer_bag()
            count += recursive

        return count

    def total_bags(self):
        """ Get total amount of bags needed """
        count = 0
        for bag, amount in self.inner:
            recursive = bag.total_bags()
            count += amount + amount * recursive

        return count


def parse_input(puzzle_data):
    """ Return puzzle in structured data form """
    structured_puzzle = dict()
    for line in puzzle_data.split("\n"):
        outer_line, inner_line = line.split(" bags contain ")

        if outer_line not in structured_puzzle:
            outer_bag = Bag(outer_line)
            structured_puzzle[outer_line] = outer_bag
        else:
            outer_bag = structured_puzzle[outer_line]

        for inner_part in inner_line.split(", "):
            if "no other bags." in inner_part:
                continue

            pattern = re_compile(r"^(?P<amount>\d)+\s(?P<colour>\w+\s\w+).*$")
            matches = pattern.search(inner_part)
            amount = matches.group("amount")
            colour = matches.group("colour")

            if colour not in structured_puzzle:
                inner_bag = Bag(colour)
                structured_puzzle[colour] = inner_bag
            else:
                inner_bag = structured_puzzle[colour]

            inner_bag.add_outer(outer_bag)
            outer_bag.add_inner(inner_bag, int(amount))

    return structured_puzzle


def main():
    """ Solve the puzzle """
    puzzle_input = parse_input(get_data(day=7))
    print(puzzle_input["shiny gold"].count_outer_bag())
    print(puzzle_input["shiny gold"].total_bags())


if __name__ == "__main__":
    main()
