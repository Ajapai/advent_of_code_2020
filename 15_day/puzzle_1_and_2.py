#!/usr/bin/env python3
import sys

numbers = [int(number) for number in open('input').read().split(",")]
last_occurence = {number:i + 1 for i, number in enumerate(numbers[:-1])}

for i in range(len(numbers), int(sys.argv[1])):
    if numbers[-1] not in last_occurence:
        numbers.append(0)
    else:
        numbers.append(i - last_occurence[numbers[-1]])
    last_occurence[numbers[-2]] = i

print(numbers[-1])
