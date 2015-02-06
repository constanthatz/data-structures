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
    where_open = value.find("(")
    where_close = value.find(")")

    if ((where_open == -1) and where_close != -1) or (where_open > where_close):
        return -1
   
