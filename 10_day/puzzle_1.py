#!/usr/bin/env python3

lines = sorted(int(x) for x in open('input').read().splitlines())

jump_1 = 1
jump_3 = 1

for i, line in enumerate(lines[1:]):
    if line == lines[i] + 1:
        jump_1 += 1
    if line == lines[i] + 3:
        jump_3 += 1

print(jump_1 * jump_3)
