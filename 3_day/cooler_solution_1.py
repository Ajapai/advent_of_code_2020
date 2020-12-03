#!/usr/bin/env python3
print(sum(
    1
    for i, line in enumerate(open('input').read().splitlines())
    if line[i * 3 % len(line)] == "#"
    ))
