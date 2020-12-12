#!/usr/bin/env python3
import re

lines = open('input').read().splitlines()
bags = []
def find_bags_inside_bag(bag_name):
    count = 0
    for line in lines:
        amount = line.count(',')
        pattern = "^([a-z]+ [a-z]+) bag[s]* contain "
        for x in range(amount):
            pattern += "(?:(\d) ([a-z]+ [a-z]+) bag[s]*, )"
        pattern += "(?:(?:(\d) ([a-z]+ [a-z]+) bag[s]*.)|(?:no other bags.))"
        match = re.match(pattern, line)
        if bag_name == match.group(1):
            for i in range(amount + 1):
                if match.group(i+1*2) and match.group(i+1*2+1):
                    count += int(match.group((i+1)*2))  + int(match.group((i+1)*2)) * find_bags_inside_bag(match.group((i+1)*2+1))
    return count
print(find_bags_inside_bag("shiny gold"))

