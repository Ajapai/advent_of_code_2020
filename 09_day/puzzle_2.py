#!/usr/bin/env python3

NUMBER = 69316178

lines = open('input').read().splitlines()

for i in range(len(lines) - 1):
    current_sum = y = 0
    while current_sum < NUMBER:
        current_sum += int(lines[i+y])
        y += 1

    if current_sum == NUMBER:
        sorted_list = sorted(lines[i:i+y])
        print(int(sorted_list[0]) + int(sorted_list[-1]))
        break
