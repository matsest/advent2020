#!/usr/bin/env python3
"https://adventofcode.com/2020/day/13"

def parse_input(inputfile: str):
    '''Parse input'''
    with open(inputfile, 'r') as input_file:
        lines = [line.rstrip("\n") for line in input_file.readlines()]
    timestamp = int(lines[0])
    services = [int(s) for s in lines[1].split(',') if s != 'x']
    
    return timestamp,services

def number_one() -> int:
    timestamp, services = parse_input('input.txt')
    #print(timestamp)
    #print(services)

    earliest = max(services)

    for s in services:
        times = [r for r in range(0,timestamp+max(services),s) if r >= timestamp]
        waiting_time = times[0] - timestamp
        if waiting_time < earliest:
            earliest = waiting_time
            bus = s

    #print(bus,earliest)
    return bus*earliest

def parse_input2(inputfile: str):
    '''Parse input'''
    with open(inputfile, 'r') as input_file:
        lines = [line.rstrip("\n") for line in input_file.readlines()]
    services = {int(s):i for i,s in enumerate(lines[1].split(',')) if s != 'x'}
    
    return services

def number_two() -> int:
    buses = parse_input2('input.txt')
    #print(buses)

    timestamp, increment = 0, 1

    for bus in buses:
        delay = buses[bus]
        bus_interval = bus

        while (timestamp + delay) % bus_interval != 0:
            timestamp += increment

        increment *= bus_interval
        #print(bus, delay, timestamp+delay)

    return timestamp

print('Ans 1: ', number_one())
print('Ans 2: ', number_two())
