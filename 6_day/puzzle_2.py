#!/usr/bin/env python3
letters = list(map(chr, range(97, 123)))

print(sum(
    sum(
        1
        for letter in letters
        if all(
            letter in line
            for line in passport.splitlines()
            )
    )
    for passport in open('input').read().split("\n\n")
))
