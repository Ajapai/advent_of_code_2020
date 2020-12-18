#!/usr/bin/env python3

pocket_galaxy = {(x,y,0):char
        for x, line in enumerate(open('input').read().splitlines())
        for y, char in enumerate(line)}

shell = {"x":(-1,8), "y":(-1,8), "z":(-1,1)}
cubes_within = lambda : [
        (x,y,z)
        for x in range(shell["x"][0], shell["x"][1] + 1)
        for y in range(shell["y"][0], shell["y"][1] + 1)
        for z in range(shell["z"][0], shell["z"][1] + 1)
        ]

active_neighbours = lambda cube: sum(
        1
        for x in range(cube[0] - 1, cube[0] + 2)
        for y in range(cube[1] - 1, cube[1] + 2)
        for z in range(cube[2] - 1, cube[2] + 2)
        if cube != (x,y,z)
        and pocket_galaxy.get((x,y,z), ".") == "#"
        )

is_toggle_worthy = lambda cube: pocket_galaxy.get(cube, ".") == "." and active_neighbours(cube) == 3 or pocket_galaxy.get(cube, ".") == "#" and not 2 <= active_neighbours(cube) <= 3
create_pocket_matrix = lambda : {cube:is_toggle_worthy(cube) for cube in cubes_within()}

def toggle(core):
    global pocket_galaxy
    if pocket_galaxy.get(core, ".") == ".":
        pocket_galaxy[core] = "#"
    else:
        pocket_galaxy[core] = "."

def toggle_all(pocket_matrix):
    for key in pocket_matrix:
        if pocket_matrix[key]:
            toggle(key)

def expand_shell():
    global shell
    shell["x"] = (shell["x"][0] - 1, shell["x"][1] + 1)
    shell["y"] = (shell["y"][0] - 1, shell["y"][1] + 1)
    shell["z"] = (shell["z"][0] - 1, shell["z"][1] + 1)

for i in range(6):
    for x in range(shell["x"][0], shell["x"][1] + 1):
        line = ""
        for y in range(shell["y"][0], shell["y"][1] + 1):
            line += pocket_galaxy.get((x,y,0), ".") if x != 0 or y != 0 else "0"
        print(line)
    toggle_all(create_pocket_matrix())
    expand_shell()

print(sum(1 for key in pocket_galaxy if pocket_galaxy[key] == "#"))
