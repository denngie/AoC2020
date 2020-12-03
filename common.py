#!/usr/bin/python3
""" Common functions needed every day """


def read_input(file):
    """ Read file and return list of lines """
    content = list()
    with open(file) as file_handle:
        for line in file_handle:
            content.append(line.rstrip())
    return content
