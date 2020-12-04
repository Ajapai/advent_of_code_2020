#!/usr/bin/env python3
import re

patterns = ["^byr:", "^iyr:", "^eyr:", "^hgt:", "^hcl:", "^ecl:", "^pid:"]

print(sum(
    1
    for passport in open('input').read().split("\n\n")
    if sum(
        1
        for line in passport.splitlines()
        for split in line.split()
        for pattern in patterns
        if re.match(pattern, split)
        ) == 7
    ))

