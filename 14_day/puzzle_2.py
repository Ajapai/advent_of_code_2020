#!/usr/bin/env python3

lines = open('input').read().splitlines()

memory = {}
bitmask = None

def create_variations(memory_adress):
    adress_variations = []
    x_count = memory_adress.count("X")

    for i in range(2**x_count):
        i_as_bit = bin(i)[2:].zfill(x_count)
        adress_variation = memory_adress

        for j in range(x_count):
            adress_variation = adress_variation.replace("X", i_as_bit[j], 1)

        adress_variations.append(int(adress_variation, 2))
    return adress_variations

for line in lines:
    if "mask" in line:
        bitmask = line.replace("mask = ", "")
    else:
        key_value = line.replace("mem[", "").split("] = ")
        key_as_int = int(key_value[0])
        key_as_bit = f'{key_as_int:036b}'

        for i, char in enumerate(bitmask):
            if char != "0":
                key_as_bit = key_as_bit[:i] + char + key_as_bit[i+1:]

        for key in create_variations(key_as_bit):
            memory[key] = key_value[1]

print(sum(int(memory[key]) for key in memory))
