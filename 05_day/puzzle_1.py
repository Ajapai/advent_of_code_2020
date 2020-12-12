#!/usr/bin/env python3

highest_id = 0
lines = open('input').read().splitlines()
for line in lines:
    row = int(line[0:7].replace("B", "1").replace("F", "0"), 2)
    column = int(line[7:10].replace("R", "1").replace("L", "0"), 2)
    seat_id = row * 8 + column
    highest_id = seat_id if highest_id < seat_id else highest_id
print(highest_id)
