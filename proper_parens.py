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
    ''' Return 1, 0, or -1 is input is open, balanced, or broken. '''
    output = 0
    index = 0
    while index < len(value) or output < 0:
        # If the count is ever < 0, statement must be -1 (broken), end loop
        # If the index is out of range, end loop
        if value[index] == ")":
            # Subtract 1 for every close paren
            output -= 1
        elif value[index] == "(":
            # Add 1 for every close paren
            output += 1

        index += 1

    if not output:
        # Check if ouput is 0 (balanced)
        return output
    else:
        # Must be 1 (open) if it makes it to here
        return 1
