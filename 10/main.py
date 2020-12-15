#!/usr/bin/env python3
"https://adventofcode.com/2020/day/10"

def parse_input(inputfile: str):
    '''Parse input'''
    with open(inputfile, 'r') as input_file:
        lines = [int(line.rstrip("\n")) for line in input_file.readlines()]

    return lines

def number_one() -> int:
    nums = parse_input('input.txt')
    nums.sort()
    nums.append(max(nums) + 3)

    diff_counts = {1:0, 2:0, 3: 0}

    current_rating = 0
    for v in nums:
        diff_counts[v-current_rating] += 1
        current_rating = v
    #print(diff_counts)

    return diff_counts[1] * diff_counts[3]


def number_two() -> int:
    nums = [0] + parse_input('input.txt')
    nums.sort()
    nums.append(max(nums) + 3)

    factors = {0:1}
    for n in nums[1:]: # check each number
        factors[n] = 0
        for m in range(1,4): # check -1, -2, -3 from current number
            if n-m in nums:
                factors[n] += factors[n-m]

    return factors[max(nums)]

print('Ans 1: ', number_one())
print('Ans 2: ', number_two())
