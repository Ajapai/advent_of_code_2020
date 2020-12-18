#!/usr/bin/env python3
import math

document = open('input').read().split("\n\n")
rules = document[0].splitlines()
my_ticket = document[1].splitlines()[1]
rules_dict = {
        line.split(":")[0]:set(
            number for numbers in (
                range(int(first), int(last) + 1) for first, last in (
                    range_.split("-") for range_ in line.split(": ")[1].split(" or ")))
            for number in numbers)
        for line in rules
        }

valid_numbers = set(
        number
        for numbers in (rules_dict[key] for key in rules_dict)
        for number in numbers
        )

valid_tickets = [
        ticket
        for ticket in document[2].splitlines()[1:]
        if all(
            int(number) in valid_numbers
            for number in ticket.split(",")
        )]

truth_matrix = [
        [all(int(number) in rules_dict[key] for number in number_list) for key in rules_dict]
        for number_list in [
            [line.split(",")[i] for line in valid_tickets]
            for i in range(len(my_ticket.split(",")))]
        ]

allocated_indexes = {}
for field_index, bools in sorted(enumerate(truth_matrix), key=lambda x:x[1]):
    for rule_index, match in enumerate(bools):
        if match and rule_index not in allocated_indexes:
            allocated_indexes[rule_index] = field_index

print(math.prod(
    int(my_ticket.split(",")[allocated_indexes[i]])
    for i in range(6)
    ))
