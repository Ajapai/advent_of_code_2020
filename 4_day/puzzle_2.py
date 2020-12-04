#!/usr/bin/env python3
import re

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
        for split in line.split():
            if pat in split:
                value = split[split.index(pat) + len(pat):]
                if i == 0 and 1920 <= int(value) <= 2002:
                    pattern_bool[i] = True
                if i == 1 and 2010 <= int(value) <= 2020:
                    pattern_bool[i] = True
                if i == 2 and 2020 <= int(value) <= 2030:
                    pattern_bool[i] = True
                if i == 3:
                    if value.endswith("cm") and 150 <= int(value.split("cm")[0])  <= 193:
                        print(value)
                        pattern_bool[i] = True
                    if value.endswith("in") and 59 <= int(value.split("in")[0]) <= 76:
                        print(value)
                        pattern_bool[i] = True
                if i == 4 and re.match("^#[0-9a-f]{6}", value) and len(value) == 7:
                    pattern_bool[i] = True
                if i == 5 and value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth":
                    pattern_bool[i] = True
                if i == 6 and re.match("^[0-9]{9}", value) and len(value) == 9:
                    pattern_bool[i] = True
if(all(pattern_bool)):
    count += 1
print(count)
