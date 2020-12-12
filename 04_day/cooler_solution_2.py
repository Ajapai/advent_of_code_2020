#!/usr/bin/env python3
import re

patterns = [
        "^byr:(19[2-9][0-9]|200[0-2])$",
        "^iyr:(201[0-9]|2020)$",
        "^eyr:(202[0-9]|2030)$",
        "^hgt:((1[5-8][0-9]|19[0-3])cm$|(59|6[0-9]|7[0-6])in$)",
        "^hcl:#[0-9a-f]{6}$",
        "^ecl:(amb|blu|brn|gry|grn|hzl|oth)$",
        "^pid:\d{9}$"
        ]

print(sum(
    1
    for passport in open('input').read().split("\n\n")
    if sum(
        1
        for split in passport.split()
        if any(re.match(pattern, split) for pattern in patterns)
        ) == 7
    ))
