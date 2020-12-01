#!/usr/bin/env python3

numbers = open('input').read().splitlines()
for number in numbers:
    for number2 in numbers:
        if int(number) + int(number2) == 2020:
            print(int(number) * int(number2))
            break
    else:
        continue
    break

