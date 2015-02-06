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
    output = 0
    while output >= 0:
        for item in value:
                if item == ")":
                    output -= 1
                    if output == -1:
                        return -1
                elif item == "(":
                    output += 1
        if output == 0:
            return 0
        elif output > 1:
            return 1
