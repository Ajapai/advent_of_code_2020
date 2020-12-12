#!/usr/bin/env python3
import re

lines = open('input').read().splitlines()
visited_lines = []
current_line = accumulator = 0

while current_line not in visited_lines:
    visited_lines.append(current_line)
    if "acc" in lines[current_line]:
        accumulator += int(lines[current_line].split(" ")[1])
    elif "jmp" in lines[current_line]:
        current_line += int(lines[current_line].split(" ")[1]) - 1
    current_line += 1
print(accumulator)
