#!/usr/bin/env python3
import sys

last_number = [int(number) for number in open('input').read().split(",")][-1]
last_occurences = {number:i + 1 for i, number in enumerate(int(number) for number in open('input').read().split(",")[:-1])}

for i in range(len(last_occurences) + 1, int(sys.argv[1])):
    current_number = 0 if last_number not in last_occurences else i - last_occurences[last_number]
    last_occurences[last_number] = i
    last_number = current_number

print(last_number)
