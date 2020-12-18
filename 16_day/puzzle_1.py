#!/usr/bin/env python3

document = open('input').read().split("\n\n")
other_tickets = document[2].splitlines()[1:]
valid_numbers = set(
        int(number)for numbers in (
            range(int(first), int(last) + 1) for first, last in (
                range_.split("-") for ranges in (
                    rule.split(" or ") for rule in (
                        line.split(": ")[1] for line in document[0].splitlines()))
                for range_ in ranges))
        for number in numbers)

print(sum(
    int(number)
    for number_list in (ticket.split(",") for ticket in other_tickets)
    for number in number_list
    if int(number) not in valid_numbers
    ))
