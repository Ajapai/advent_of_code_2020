#!/usr/bin/env python3

# This solution is slow..
# like really slow..
# like three days or more slow...


lines = sorted(int(x) for x in open('input_medium').read().splitlines())

possible_lines = []
count = 0

def get_possible_combinations(number_list):
    if number_list in possible_lines:
        return
    possible_lines.append(number_list)

    global count
    count = count + 1
    if count % 1000 == 0:
        print(count)

    for i in range(len(number_list) - 2):
        if number_list[i+1] - number_list[i] < 3 and number_list[i+2] - number_list[i] <= 3:
            copy = number_list.copy()
            del copy[i+1]
            get_possible_combinations(copy)

get_possible_combinations(lines)
print(count)



