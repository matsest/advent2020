#!/usr/bin/env python3
"https://adventofcode.com/2020/day/14"

from itertools import product

def parse_input(inputfile: str):
    '''Parse input'''
    with open(inputfile, 'r') as input_file:
        lines = [line.strip() for line in input_file.readlines()]

    return lines

def modify_bit(number, position, bit): 
    mask = 1 << position 
    return (number & ~mask) | ((bit << position) & mask) 

def number_one() -> int:
    programs = parse_input('input.txt')

    masks = []
    memories = {}
    for prog in programs:
        arg, val = prog.split(' = ')
        if arg == 'mask':
            masks.append(val)
            significant_mask = [[int(35 - i[0]), int(i[1])] for i in enumerate(masks[-1]) if i[1] != 'X']
        else:
            mem = int(arg.lstrip('mem[').rstrip(']'))
            ans = int(val)
            
            for pos, bit in significant_mask:
                ans = modify_bit(ans, pos, bit)

            memories[mem] = ans

    return sum(memories.values())

def number_two() -> int:
    programs = parse_input('input.txt')

    masks = []
    memories = {}
    for prog in programs:
        arg, val = prog.split(' = ')
        if arg == 'mask':
            masks.append(val)
            significant_ones = [[int(35 - i[0]), int(i[1])] for i in enumerate(masks[-1]) if i[1] == '1']
            # find positions with X (fluctuating bits)
            fluctuating = [int(35 - i[0]) for i in enumerate(masks[-1]) if i[1] == 'X']
            # create all combinations of 0,1 for the fluctating bits
            combos = [seq for seq in product("01", repeat=len(fluctuating))]
            # generate a list of all the combinations
            possible_masks = [list(zip(fluctuating,i)) for i in combos]
        else:
            mem = int(arg.lstrip('mem[').rstrip(']'))
            ans = int(val)
           
            # do initial masking
            for pos, bit in significant_ones:
                mem = modify_bit(mem, pos, bit)

            # generate all possible memory addresses based on fluctuating bits
            for mask in possible_masks:
                for pos,bit in mask:
                    mem = modify_bit(mem,pos,int(bit))
                memories[mem] = ans

    return sum(memories.values())


print('Ans 1: ', number_one())
print('Ans 2: ', number_two())
