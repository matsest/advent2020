#!/usr/bin/env python3
"https://adventofcode.com/2020/day/9"

import itertools

def parse_input(inputfile: str):
    '''Parse input'''
    with open(inputfile, 'r') as input_file:
        lines = [int(line.rstrip("\n")) for line in input_file.readlines()]

    return lines 

def number_one() -> int:
    '''What is the first number that is not a combo of two numbers in the previous preamble-length numbers?'''
    nums = parse_input('input.txt')
    preamble = 25

    for i in range(preamble,len(nums)):
        prev_nums = nums[i-preamble:i]
        possible_pairs = list(itertools.combinations(prev_nums, 2))
        found = False

        for pair in possible_pairs:
            if pair[0] + pair[1] == nums[i]:
                found = True
        if not found: 
                break # we found the number

    return nums[i]

def number_two():
    target = number_one()
    nums = parse_input('input.txt')

    smallest, largest = 0, 0
    for i in range(len(nums)):
        smallest, largest = nums[i], nums[i]
        cont_set = [nums[i]]
        for j in range(i+1, len(nums)):
            cont_set.append(nums[j])
            if sum(cont_set) >= target:
                break
        if sum(cont_set) == target:
            largest = max(cont_set)
            smallest = min(cont_set)
            break

    return smallest + largest

print('Ans 1: ', number_one())
print('Ans 2: ', number_two())

