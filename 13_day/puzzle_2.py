#!/usr/bin/env python3
from math import gcd

busses = [[int(bus_id), i] for i, bus_id in enumerate(open('input').read().splitlines()[1].split(",")) if bus_id != "x"]
timestamp = 0

def get_lcm(number_list):
    lcm = 1
    for number in number_list:
        lcm = lcm * number // gcd(lcm, number)
    return lcm

def find_first_match(bus, lcm):
    global timestamp
    while timestamp % bus[0] != bus[0] - (bus[1] % bus[0]):
        timestamp += lcm

for i in range(len(busses) - 1):
    find_first_match(busses[i + 1], get_lcm([bus[0] for bus in busses][0:i + 1]))

print(timestamp)
