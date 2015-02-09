#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals


def check_statement1(value):
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
