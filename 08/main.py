#!/usr/bin/env python3
"https://adventofcode.com/2020/day/8"

from typing import List
import time
import copy

def parse_input(inputfile: str):
    '''Parse answers'''
    with open(inputfile, 'r') as input_file:
        lines = [line.rstrip("\n") for line in input_file.readlines()]

    instructions = []
    for line in lines:
        parts = line.split()
        instruction, val = parts[0], int(parts[1])
        instructions.append([instruction, val])
    return instructions

def number_one() -> int:
    '''What is the value in the acumulator before any instruction is executed a second time?'''
    instructions = parse_input('input.txt')
    #print(instructions)

    current = 0
    accumulator = 0
    visited = [current]

    while len(visited) == len(set(visited)):
        inst, val = instructions[current]
        #print(inst,val)
        if inst == 'nop':
            current += 1
        elif inst == 'acc':
            accumulator += val
            current += 1
        elif inst == 'jmp':
            current += val
        visited.append(current)
    return accumulator

def find_accumulated2(instructions):
    current = 0
    accumulator = 0
    visited = [current]

    timeout = time.time() + 0.001 # give up rather fast

    while len(visited) == len(set(visited)):
        #print(visited)
        inst, val = instructions[current]
        #print(inst,val)
        if inst == 'nop':
            current += 1
        elif inst == 'acc':
            accumulator += val
            current += 1
        elif inst == 'jmp':
            current += val

        if current == len(instructions): # we reached the end
            break

        if time.time() > timeout: # indifinite loop, return 0
            accumulator = 0
            break

        if current not in visited:
            visited.append(current)
 
    return accumulator

def number_two():
    instructions_origin = parse_input('input.txt')
    #print(instructions_origin)

    for i in range(len(instructions_origin)):
        acc = 0
        val = ''
        if instructions_origin[i][0] == 'nop':
            val = 'jmp'
        elif instructions_origin[i][0] == 'jmp':
            val = 'nop'

        if val == 'jmp' or val == 'nop':
            temp_list = copy.deepcopy(instructions_origin)
            temp_list[i][0] = val
            acc = (find_accumulated2(temp_list))

        if acc > 0: # we found a valid acc
            break
 
    return acc

print('Ans 1: ', number_one())
print('Ans 2: ', number_two())

