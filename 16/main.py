#!/usr/bin/env python3
"https://adventofcode.com/2020/day/16"

def parse_input(inputfile: str):
    '''Parse input'''
    with open(inputfile, 'r') as input_file:
        lines = [line.rstrip("\n") for line in input_file.readlines()]
  
    valid_ranges = []
    for line in lines:
        parts = line.split(': ')
        if len(parts) > 1:
            ranges = parts[1].split(' or ')
            first_start, first_end = ranges[0].split('-')
            second_start, second_end = ranges[1].split('-')
            valid_ranges.extend([i for i in range(int(first_start), int(first_end)+1)])
            valid_ranges.extend([i for i in range(int(second_start), int(second_end)+1)])
        if line == 'nearby tickets:':
            nearby = lines[lines.index(line)+1:]

        if line == 'your ticket:':
            your = lines[lines.index(line)+1]

    nearby_tickets = []
    for  i in nearby:
        vals = i.split(',')
        for v in vals:
            nearby_tickets.append(int(v))
    #nearby_tickets = [i.split(',') for i in nearby]

    your_t = your.split(',')
    your_tickets = [int(t) for t in your_t]

    #print(nearby_tickets)
    valid_tickets = set(valid_ranges)
    #print(valid_tickets)
    return set(valid_ranges), nearby_tickets, your_tickets

def number_one() -> int:
    valid_tickets, tickets, _ = parse_input('input.txt')

    not_valids = [t for t in tickets if t not in valid_tickets]

    return sum(not_valids)

def parse_input2(inputfile: str):
    '''Parse input'''
    with open(inputfile, 'r') as input_file:
        lines = [line.rstrip("\n") for line in input_file.readlines()]
  
    valid_ranges = {}
    for line in lines:
        parts = line.split(': ')
        if len(parts) > 1:# and parts[0].startswith('departure'):
            #print(parts[0])
            ranges = parts[1].split(' or ')
            #print(ranges)
            first_start, first_end = ranges[0].split('-')
            second_start, second_end = ranges[1].split('-')
            current = []
            current.extend([i for i in range(int(first_start), int(first_end)+1)])
            current.extend([i for i in range(int(second_start), int(second_end)+1)])
            valid_ranges[parts[0]]= (set(current))
        if line == 'nearby tickets:':
            nearby = lines[lines.index(line)+1:]

        if line == 'your ticket:':
            your = lines[lines.index(line)+1]

    nearby_tickets = []
    for  i in nearby:
        vals = i.split(',')
        nearby_tickets.append([int(v) for v in vals])
    #nearby_tickets = [i.split(',') for i in nearby]
    #print(nearby_tickets)

    your_t = your.split(',')
    your_tickets = [int(t) for t in your_t]
    #print(your_tickets)

    #print(nearby_tickets)
    #print(valid_tickets)
    return valid_ranges, nearby_tickets, your_tickets

def number_two() -> int:
    valid_tickets, nearby_tickets, your_ticket = parse_input2('testinput2.txt')
    print(valid_tickets)
    print (nearby_tickets)

    order = { i:[] for i in range(len(nearby_tickets[0])) }
    print(order)

    for i in order:
        for n in nearby_tickets:
            order[i].append(n[i] )

    print(order)

    return 0

print('Ans 1: ', number_one())
print('Ans 2: ', number_two())
