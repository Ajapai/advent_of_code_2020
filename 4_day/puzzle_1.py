#!/usr/bin/env python3

pattern = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
pattern_bool = [False, False, False, False, False, False, False]
count = 0

lines = open('input').read().splitlines()
for line in lines:
    if line == "":
        if all(pattern_bool):
            count += 1
        for i, b in enumerate(pattern_bool):
            pattern_bool[i] = False
        continue

    for i, pat in enumerate(pattern):
        if pat in line:
            pattern_bool[i] = True
if all(pattern_bool):
    count += 1
print(count)
