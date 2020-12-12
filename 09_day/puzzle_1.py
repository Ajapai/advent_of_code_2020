#!/usr/bin/env python3

lines = open('input').read().splitlines()

def check(last_25_lines, current_line):
    return(any(
        int(line) + int(second_line) == int(current_line)
        for i, line in enumerate(last_25_lines)
        for second_line in last_25_lines[i+1:]
        ))

print(next(
        line
        for i, line in enumerate(lines)
        if i > 25 and not check(lines[i-25:i], lines[i])
        ))
