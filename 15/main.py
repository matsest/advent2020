#!/usr/bin/env python3
"https://adventofcode.com/2020/day/10"

test_inp = "0,3,6"
inp = "9,19,1,6,0,5,4"

def number_one() -> int:
    start_nums = [int(i) for i in inp.split(',')]
    nums_said = start_nums.copy()
    i = len(nums_said)

    while i < 2020:
        last_num = nums_said[-1]
        if nums_said.count(last_num) == 1:
            nums_said.append(0)
        elif nums_said.count(last_num) > 1:
            indexes = [i for i,v in enumerate(nums_said) if v == last_num]
            diff = indexes[-1] - indexes[-2]
            nums_said.append(diff)
            #print(nums_said[-1])
        i += 1
    #print(nums_said)
    #print(len(nums_said))
    return nums_said[-1]

def number_two_d() -> int:
    start_nums = [int(i) for i in inp.split(',')]
    nums_said = {}
    for i,v in enumerate(start_nums):
        nums_said[v] = i + 1 # turns starts with 1
    current =  start_nums[-1]
    i = len(start_nums)

    while i < 30000000:
        if current not in nums_said:
            previous = None
        else:
            previous = nums_said[current]
        nums_said[current] = i
        current = i-previous if previous else 0
        i += 1
    return current

def number_two() -> int:
    start_nums = [int(i) for i in inp.split(',')]
    nums_said = {}
    for i,v in enumerate(start_nums):
        nums_said[v] = [i]
    last =  start_nums[-1]
    i = len(nums_said)

    while i < 30000000:
        #last_num = last
        last_num_turns = nums_said[last]
        if len(last_num_turns) == 1:
            num = 0
        #elif len(last_num_turns) > 1:
        else:
            #indexes = [i for i,v in enumerate(nums_said) if v == last_num]
            diff = last_num_turns[-1] - last_num_turns[-2]
            num = diff
            #print(nums_said[-1])
        if num not in nums_said:
            nums_said[num] = [i]
        else:
            nums_said[num].extend([i])
        last = num
        i += 1
    #print(nums_said)
    print(len(nums_said))
    return last


    return 0

print('Ans 1: ', number_one())
print('Ans 2: ', number_two_d())
