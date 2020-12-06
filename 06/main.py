#!/usr/bin/env python3
"https://adventofcode.com/2020/day/6"

from typing import List

def parse_answers(inputfile: str) -> List[dict]:
    '''Parse answers'''
    with open(inputfile, 'r') as input_file:
        lines = [line.rstrip("\n") for line in input_file.readlines()]

    # Transform input to dictionary 
    answers = []
    group_answers = {}
    group_sizes = []
    group_size = 0
    #print(lines)
    for line in lines:
        if line != '':
            for k in line:
                if k not in group_answers.keys():
                    group_answers[k] = 1
                else:
                    group_answers[k] += 1
            group_size += 1
        else:
            answers.append(group_answers)
            group_sizes.append(group_size)
            group_answers = {}
            group_size = 0
        #print('group: ', group_answers)

    # add last
    answers.append(group_answers)
    group_sizes.append(group_size)
    #print(answers)

    return answers, group_sizes


def number_one() -> int:
    '''Check for sum of counts of number of questions answered'''
    answers, _ = parse_answers('input.txt')

    ans_counts = 0
    for ans in answers:
        ans_counts += len(ans.keys())
    return ans_counts

def number_two():
    '''Check for sum of counts of number of questions where everyone answered yes'''
    answers, group_sizes = parse_answers('input.txt')

    ans_counts = 0
    for i in range(len(answers)):
        for ans in answers[i].values():
            if ans == group_sizes[i]:
                ans_counts += 1
    return ans_counts

print('Ans 1: ', number_one())
print('Ans 2: ', number_two())

