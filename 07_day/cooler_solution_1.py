#!/usr/bin/env python3
import re

pattern = lambda x : "^([a-z]+ [a-z]+) bag[s]* contain " + ("(?:(\d) ([a-z]+ [a-z]+) bag[s]*, )" * x) + "(?:(?:(\d) ([a-z]+ [a-z]+) bag[s]*.)|(?:no other bags.))"

def find_bags_that_contain_bag(bag_name):
    return [
            bag
            for baglist in (
                [found_bag] + find_bags_that_contain_bag(found_bag)
                for found_bag in (
                    match.group(1)
                    for match in (
                        re.match(pattern(line.count(',')), line)
                        for line in open('input').read().splitlines()
                        )
                    if bag_name != match.group(1) and bag_name in match.groups()
                    )
                )
            for bag in baglist
            ]
print(len(list(set(find_bags_that_contain_bag("shiny gold")))))
