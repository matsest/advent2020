#!/usr/bin/env python3
"https://adventofcode.com/2020/day/7"

import re

def parse_input(inputfile: str):
    '''Returns the number of possible bags that contain a shiny gold bag'''
    '''This is really badly implemented'''
    with open(inputfile, 'r') as input_file:
        lines = [line.rstrip("\n") for line in input_file.readlines()]
  
    nodes = ["shiny gold"]
    i_last, i_current = 0, 0

    # Checks all possible parents for node in nodes. Adds parents to nodes and continue until no other parents are found.
    while True:
        i_last = i_current
        for line in lines:
            bag, rest = (line.split(" bags contain "))
            if not "no other bag" in rest:
                for node in nodes:
                    if node in rest and bag not in nodes:
                        #print("PARENT", bag, "-->", rest)
                        nodes.append(bag)
                        #print(nodes)
                        i_current += 1
        if i_current == i_last: # nothing added
            break
    return len(nodes)-1 # remove initial shiny gold bag

def number_one() -> int:
    '''How many bag colors contain at least one shiny gold bag?'''
    bags = parse_input('input.txt')
    return bags

def number_two():
    '''There is only one 1 shiny gold bag occurance. How many bags does it contain?'''

    'bahhh'

    return 'Not completed'

print('Ans 1: ', number_one())
print('Ans 2: ', number_two())

