#!/usr/bin/env python3
import sys

# Needs argumet if puzzle '1' or '2' should be solved

# x equals one line and is structured like this:
# x = [[min, max], letter, password]
print(sum(
    1
    for (lower, higher), letter, password in (
        [[int(x) for x in s[0].split("-")], s[1][0], s[2]]
        for s in [l.split() for l in open('input').read().splitlines()]
        )
    if int(sys.argv[1]) == 1 and lower <= password.count(letter) <= higher
    or int(sys.argv[1]) == 2 and (password[lower - 1] == letter) != (password[higher - 1] == letter)
    ))
