#!/usr/bin/env python3

seats = list(range(1024))
found_seats = []
lines = open('input').read().splitlines()
for line in lines:
    row = int(line[0:7].replace("B", "1").replace("F", "0"), 2)
    column = int(line[7:10].replace("R", "1").replace("L", "0"), 2)
    found_seats.append(row * 8 + column)
empty_seats = list(set(seats).difference(found_seats))
print(next(
    x
    for i, x
    in enumerate(empty_seats)
    if 0 < i < len(empty_seats)
    and x - 1 != empty_seats[i-1]
    and x + 1 != empty_seats[i+1]
))
