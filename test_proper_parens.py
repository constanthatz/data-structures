from __future__ import unicode_literals
from proper_parens import check_statement


def test_check_statement():

    # Edge cases of strings of length one
    value = ")"
    assert check_statement(value) == -1

    value = "("
    assert check_statement(value) == 1

    # Edge cases of strings of length two
    value = "()"
    assert check_statement(value) == 0

    # 'Balanced' but broken
    value = ")("
    assert check_statement(value) == -1

    # Broken beginnning, middle, and end
    value = ")()"
    assert check_statement(value) == -1

    value = "())()"
    assert check_statement(value) == -1

    value = "())"
    assert check_statement(value) == -1

    # Open beginnning, middle, and end
    value = "(()"
    assert check_statement(value) == 1

    value = "()(()"
    assert check_statement(value) == 1

    value = "()("
    assert check_statement(value) == 1


def test_characters_not_parens():
    # Edge cases of strings of length one
    value = "a + )"
    assert check_statement(value) == -1

    value = "(a +"
    assert check_statement(value) == 1

    # Edge cases of strings of length two
    value = "(a +)"
    assert check_statement(value) == 0

    # 'Balanced' but broken
    value = "a +)("
    assert check_statement(value) == -1

    # Broken beginnning, middle, and end
    value = ")(a +)"
    assert check_statement(value) == -1

    value = "()a +)()"
    assert check_statement(value) == -1

    value = "()a +)"
    assert check_statement(value) == -1

    # Open beginnning, middle, and end
    value = "((a +)"
    assert check_statement(value) == 1

    value = "(a +)(()"
    assert check_statement(value) == 1

    value = "(a +)("
    assert check_statement(value) == 1
