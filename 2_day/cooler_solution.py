#!/usr/bin/env python3
import sys

# Needs argumet if puzzle '1' or '2' should be solved
puzzle = int(sys.argv[1])

# Good luck deciphering this code
print(len([
    x[2]
    for x in (
        [[int(x) for x in s[0].split("-")], s[1][0], s[2]]
        for s in [l.split() for l in open('input').read().splitlines()]
        )
    if puzzle == 1 and x[0][0] <= x[2].count(x[1]) <= x[0][1]
    or puzzle == 2 and (x[2][x[0][0] - 1] == x[1]) != (x[2][x[0][1] - 1] == x[1])
    ]))
