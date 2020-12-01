#!/usr/bin/env python3

numbers = open('input').read().splitlines()
for number in numbers:
    for number2 in numbers:
        for number3 in numbers:
            if int(number) + int(number2) + int(number3) == 2020:
                print(int(number) * int(number2) * int(number3))
                break
        else:
            continue
        break
    else:
        continue
    break
