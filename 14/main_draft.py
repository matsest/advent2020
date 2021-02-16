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
            #print(significant_mask)
            #print(masks[-1])
            #print('zero: ', zeroes_pos,'\n', 'one: ', ones_pos)
        else:
            mem = int(arg.lstrip('mem[').rstrip(']'))
            dec = int(val)
            ans = dec
            #print('before: ', bin(ans).zfill(35))
            for pos, bit in significant_mask:
                ans = modify_bit(ans, pos, bit)
            #print('after: ', bin(ans).zfill(35))

            memories[mem] = ans
            #print(mem, dec, memories[mem])
       
        #print(memories)

    #print('masks: ', masks)
    #print('memories: ', memories)

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
            fluctuating = [int(35 - i[0]) for i in enumerate(masks[-1]) if i[1] == 'X']
            combos = [seq for seq in product("01", repeat=len(fluctuating))]
            possible_masks = [list(zip(fluctuating,i)) for i in combos]
            #print(significant_mask)
            #print(masks[-1])
            #print('zero: ', zeroes_pos,'\n', 'one: ', ones_pos)
        else:
            mem = int(arg.lstrip('mem[').rstrip(']'))
            ans = mem
            #print('before: ', bin(ans).zfill(35))
            #print('before: ', ans)
            for pos, bit in significant_ones:
                ans = modify_bit(ans, pos, bit)

            #print('after: ', bin(ans).zfill(35))
            #print('after: ', ans)

            for mask in possible_masks:
                #print('to change: ', mask)
                #tmp_mask = int(masks[-1].replace('X','0'),2)
                #print('tmp_mask before: ', bin(ans).zfill(35))
                for pos,bit in mask:
                    ans = modify_bit(ans,pos,int(bit))
                
                #print(ans)
                #print('val after: ', ans )
                #print('val after: ', bin(ans ).zfill(35))
                memories[ans] = int(val)

            #print('after: ', bin(ans).zfill(35))
       
        #print(memories)

    #print('masks: ', masks)
    #print('memories: ', memories)

    return sum(memories.values())


print('Ans 1: ', number_one())
print('Ans 2: ', number_two())
