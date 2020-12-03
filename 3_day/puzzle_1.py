#!/usr/bin/env python3

lines = open('input').read().splitlines()
max_position = len(lines[0]) - 1
position = 0
count = 0
for line in lines:
    if line[position] == "#":
        count += 1
    position += 3
    if position > max_position:
        position -= max_position + 1
print(count)
