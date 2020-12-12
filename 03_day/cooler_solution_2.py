#!/usr/bin/env python3
import math

print(math.prod(
    sum(
        1
        for i, line in enumerate(open('input').read().splitlines())
        if i % x == 0 and line[i // x * y % len(line)] == "#"
        )
    for x, y in [(1,1),(1,3),(1,5),(1,7),(2,1)]
    ))
