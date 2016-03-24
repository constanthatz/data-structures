#!/usr/bin/env python
from __future__ import unicode_literals
from stack import Element, Stack


def check_statement(value):
    ''' Return 1, 0, or -1 if input is open, balanced, or broken. '''
    S = Stack()
    index = 0
    while index < len(value):
        character = value[index]
        if character == "(" or character == ")":
            if character == "(":
                S.push(Element(character))
            else:
                if not S.top:
                    return -1
                else:
                    S.pop()

        index = index + 1

    if not S.top:
        return 0
    else:
        return 1
