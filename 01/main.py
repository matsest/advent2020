#!/usr/bin/env python3
"https://adventofcode.com/2020/day/1"

def number_one():
    '''find two entries that sum up to 2020 and multiply them'''
    with open("input.txt", 'r') as input_file:
        numbers = [int(n) for n in input_file.readlines()]
    
    for i in numbers:
        for k in numbers:
            if i + k == 2020:
                return i*k

    return ans

def number_two():
    '''product of three entries that sum to 2020'''
    with open("input.txt", 'r') as input_file:
        numbers = [int(n) for n in input_file.readlines()]
    
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 2020:
                    return i*j*k

    return ans

print('Ans 1: ', number_one())
print('Ans 2: ', number_two())

