#!/usr/bin/env python3
"https://adventofcode.com/2020/day/3"

def find_trees(xslope, yslope) -> int:
    '''How many trees would you encounter'''
    with open("input.txt", 'r') as input_file:
        lines = [line.rstrip("\n") for line in input_file.readlines()]
    
    x, y = 0, 0
    ylim = len(lines)
    xlim = len(lines[0])
    tree_count = 0

    while y < ylim:
        row = lines[y]
        if row[x] == "#":
            tree_count += 1
        if x + xslope  >= xlim:
            x = x + xslope - xlim
        else:
            x += xslope
        y += yslope
    
    return tree_count


def number_one() -> int:
    return find_trees(3,1)

def number_two() -> int:
    slopes = [(1,1),(3,1), (5,1), (7,1), (1,2)]
    multiply_count = 1

    for slope in slopes:
        a = (find_trees(slope[0], slope[1]))
        multiply_count = multiply_count * a

    return multiply_count

print('Ans 1: ', number_one())
print('Ans 2: ', number_two())

