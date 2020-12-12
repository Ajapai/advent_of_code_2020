#!/usr/bin/env python3

lines = open('input').read().splitlines()
rows = len(lines) - 1
columns = len(lines[0]) - 1
directions = [[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1]]

def count_seats_in_directions(seat_x, seat_y):
    seat_list = []
    for direc_x, direc_y in directions:
        x = seat_x + direc_x
        y = seat_y + direc_y
        while 0 <= x <= rows and 0 <= y <= columns:
            if lines[x][y] != ".":
                seat_list.append(lines[x][y])
                break
            x += direc_x
            y += direc_y
    return seat_list.count("#")

def is_toggle_worthy(row, column):
    amount = count_seats_in_directions(row, column)
    return lines[row][column] == "L" and amount == 0 or lines[row][column] == "#" and amount >= 5

def create_toggle_matrix():
    return [[is_toggle_worthy(i,j) for j in range(columns + 1)] for i in range(rows + 1)]

def toggle(row, column):
    if lines[row][column] == "#":
        lines[row] = lines[row][:column] + "L" + lines[row][column + 1:]
    elif lines[row][column] == "L":
        lines[row] = lines[row][:column] + "#" + lines[row][column + 1:]

def toggle_all(matrix):
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            if column:
                toggle(i, j)

toggle_matrix = create_toggle_matrix()
while any(any(bools) for bools in toggle_matrix):
    toggle_all(toggle_matrix)
    toggle_matrix = create_toggle_matrix()

print(sum(line.count("#") for line in lines))
