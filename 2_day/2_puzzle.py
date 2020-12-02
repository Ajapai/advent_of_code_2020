#!/usr/bin/env python3

lines = open('input').read().splitlines()
count = 0
for line in lines:
    r_a_p = line.split()
    min_max = r_a_p[0].split("-")
    letter = r_a_p[1][0]
    password = r_a_p[2]
    if (password[int(min_max[0]) - 1] == letter) != (password[int(min_max[1]) - 1] == letter):
        count += 1
print(count)
