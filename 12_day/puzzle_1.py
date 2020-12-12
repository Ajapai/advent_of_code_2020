#!/usr/bin/env python3

lines = ((line[0:1], int(line[1:])) for line in open('input').read().splitlines())

compass = {0:"N", 90:"E", 180:"S", 270:"W"}

position = {"N":0, "E":0, "S":0, "W":0}
rotation = 90



for char, num in lines:
    if char == "R":
        rotation += num
    elif char == "L":
        rotation -= num
    elif char == "F":
        position[compass[rotation % 360]] += num

    else:
        position[char] += num

print(abs(position["N"] - position["S"]) + abs(position["E"] - position["W"]))
