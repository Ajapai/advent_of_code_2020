#!/usr/bin/env python3
import re

lines = open('input').read().splitlines()
def toggle(i):
    if "nop" in lines[i]:
        lines[i] = lines[i].replace("nop", "jmp")
    elif "jmp" in lines[i]:
        lines[i] = lines[i].replace("jmp", "nop")

for i in range(len(lines)):
    toggle(i)
    visited_lines = []
    current_line = accumulator = 0

    while current_line not in visited_lines and current_line < len(lines) - 1:
        visited_lines.append(current_line)
        if "acc" in lines[current_line]:
            accumulator += int(lines[current_line].split(" ")[1])
        elif "jmp" in lines[current_line]:
            current_line += int(lines[current_line].split(" ")[1]) - 1
        current_line += 1

    if current_line == len(lines) - 1:
        print(accumulator)
        break
    toggle(i)
