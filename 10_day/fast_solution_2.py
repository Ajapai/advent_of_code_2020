#!/usr/bin/env python3

lines = sorted(int(x) for x in open('input').read().splitlines())

possible_ways_to_step = {0:1}
def get_value(key):
    if key in possible_ways_to_step:
        return possible_ways_to_step[key]
    return 0

for number in lines:
    possible_ways_to_step[number] = get_value(number - 1) + get_value(number - 2) + get_value(number - 3)

print(possible_ways_to_step[lines[-1]])
