#!/usr/bin/env python3

lines = open('input').read().splitlines()
rows = len(lines) - 1
columns = len(lines[0]) - 1

def is_toggle_worthy(row, column):
    # lambdas to get count of adjacent seats
    adjacent_row = lambda x, y: sum(
        1
        for seat in lines[x][y-1 if y > 0 else 0:y+2 if y < columns + 1 else columns + 1]
        if seat == "#"
        )
    current_row = lambda x, y: [lines[x][y-1] if y > 0 else 0,lines[x][y+1] if y < columns else 0].count("#")

    # summs up all seated seats
    amount = current_row(row, column)
    if row > 0:
        amount += adjacent_row(row - 1, column)
    if row < rows:
        amount += adjacent_row(row + 1, column)
    return lines[row][column] == "L" and amount == 0 or lines[row][column] == "#" and amount >= 4

def create_toggle_matrix():
    return [[is_toggle_worthy(i,j) for j in range(columns + 1)] for i in range(rows + 1)]

def toggle_all(matrix):
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            if column:
                toggle(i, j)

def toggle(row, column):
    if lines[row][column] == "#":
        lines[row] = lines[row][:column] + "L" + lines[row][column + 1:]
    elif lines[row][column] == "L":
        lines[row] = lines[row][:column] + "#" + lines[row][column + 1:]

while True:
    toggle_matrix = create_toggle_matrix()

    if any([any(bools) for bools in toggle_matrix]):
        toggle_all(toggle_matrix)
    else:
        print(sum(line.count("#") for line in lines))
        break
