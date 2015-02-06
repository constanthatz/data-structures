#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


def safe_input(prompt):
    """Return user input after catching KeyboardInterrupt and EOFError"""
    try:
        reply = raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        quit()
    else:
        return reply.decode('utf-8')  # Convert input to unicode

prompt = "Input a Lisp style statement '(test)': "
reply = safe_input(prompt)


def check_statement(value):
    # open_index = [i for i, val in enumerate(reply) if val == "("]
    # close_index = [i for i, val in enumerate(reply) if val == ")"]

    # if min(open_index) > min(close_index):
    #         return -1
    # elif len(open_index) == len(close_index):
    #     paren_total_broken = [a < b for a, b in zip(open_index, close_index)]
    #     if False not in paren_total_broken:
    #         return 0
    # else:
    #     return 0

    output = 0
    for x in value:
        if x == "(":
            output += 1
        elif x == ")":
            output -= 1
