#!/usr/bin/env python3
import re

pattern = lambda x : "^([a-z]+ [a-z]+) bag[s]* contain " + ("(?:(\d) ([a-z]+ [a-z]+) bag[s]*, )" * x) + "(?:(?:(\d) ([a-z]+ [a-z]+) bag[s]*.)|(?:no other bags.))"

def find_bags_inside_bag(bag_name):
    return sum(
            amount + amount * find_bags_inside_bag(bag)
            for amount, bag in (
                [int(match.group((i+1)*2)), match.group((i+1)*2+1)]
                for match in (
                    re.match(pattern(line.count(',')), line)
                    for line in open('input').read().splitlines()
                    if re.match("^" + bag_name, line)
                    )
                for i in range(int((len(match.groups()) - 1) / 2))
                if match.group((i+1)*2) and match.group((i+1)*2+1)
                )
            )

print(find_bags_inside_bag("shiny gold"))
