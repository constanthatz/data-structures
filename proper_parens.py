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

prompt = "Input a Lisp style string '(test)': "
reply = safe_input(prompt)
