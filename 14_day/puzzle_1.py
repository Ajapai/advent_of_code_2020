#!/usr/bin/env python3

lines = open('input').read().splitlines()

memory = {}
bitmask = None

for line in lines:
    if "mask" in line:
        bitmask = line.replace("mask = ", "")
    else:
        key_value = line.replace("mem[", "").split("] = ")
        value_as_int = int(key_value[1])
        value_as_bit = f'{value_as_int:036b}'

        for i, char in enumerate(bitmask):
            if char != "X":
                value_as_bit = value_as_bit[:i] + char + value_as_bit[i+1:]

        memory[key_value[0]] = int(value_as_bit, 2)

print(sum(int(memory[key]) for key in memory))
