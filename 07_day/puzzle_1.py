#!/usr/bin/env python3
import re

lines = open('input').read().splitlines()
bags = []
def find_bags_that_contain_bag(bag_name):
    for line in lines:
        amount = line.count(',')
        pattern = "^([a-z]+ [a-z]+) bag[s]* contain "
        for x in range(amount):
            pattern += "(?:(\d) ([a-z]+ [a-z]+) bag[s]*, )"
        pattern += "(?:(?:(\d) ([a-z]+ [a-z]+) bag[s]*.)|(?:no other bags.))"
        match = re.match(pattern, line)
        if bag_name != match.group(1) and bag_name in match.groups():
            if match.group(1) not in bags:
                bags.append(match.group(1))
            find_bags_that_contain_bag(match.group(1))
find_bags_that_contain_bag("shiny gold")
print(len(bags))
