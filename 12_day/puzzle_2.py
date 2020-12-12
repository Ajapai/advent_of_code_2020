#!/usr/bin/env python3

lines = ((line[0:1], int(line[1:])) for line in open('input').read().splitlines())

compass = {0:"N", 90:"E", 180:"S", 270:"W"}
waypoint = {"N":1, "E":10, "S":0, "W":0}
position = {"N":0, "E":0, "S":0, "W":0}
rotation = 0

da_wae = lambda char : compass[(next(key for key in compass if compass[key] == char) - rotation) % 360]

for char, num in lines:
    if char == "R":
        rotation += num
    elif char == "L":
        rotation -= num
    elif char == "F":
        for letter in ["N", "E", "S", "W"]:
            position[letter] += waypoint[da_wae(letter)] * num
    else:
        waypoint[da_wae(char)] += num

print(abs(position["N"] - position["S"]) + abs(position["E"] - position["W"]))
