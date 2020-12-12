#!/usr/bin/env python3

lines = open('input').read().splitlines()
max_position = len(lines[0]) - 1
position = 0
count = 0
counts = []
jumps = [1,3,5,7]
for jump in jumps:
    for line in lines:
        if line[position] == "#":
            count += 1
        position += jump
        if position > max_position:
            position -= max_position + 1
    print(count)
    counts.append(count)
    position = 0
    count = 0

toggle = 0
for line in lines:
    if toggle:
        toggle = 0
        continue
    if line[position] == "#":
        count += 1
    position += 1
    if position > max_position:
        position -= max_position + 1
    toggle = 1
print(count)
counts.append(count)

product = counts[0] * counts[1] * counts[2] * counts[3] * counts[4]
print(product)
