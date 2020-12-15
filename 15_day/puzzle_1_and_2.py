#!/usr/bin/env python3
import sys

numbers = [int(number) for number in open('input').read().split(",")]
last_occurence = {number:i + 1 for i, number in enumerate(int(number) for number in open('input').read().split(",")[:-1])}

for i in range(len(last_occurence) + 1, int(sys.argv[1])):
    numbers.append(0 if numbers[-1] not in last_occurence else i - last_occurence[numbers[-1]])
    last_occurence[numbers[-2]] = i

print(numbers[-1])
