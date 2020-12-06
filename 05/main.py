#!/usr/bin/env python3
"https://adventofcode.com/2020/day/5"

def calc_seat_id(boarding_pass: str) -> int:

    # Find row ranges
    row_low, row_high = 0, 128
    for i in range(7):
        if boarding_pass[i] == 'F':
            row_high = row_high - (row_high-row_low)/2
        if boarding_pass[i] == 'B':
            row_low = row_high - (row_high-row_low)/2
        #print(boarding_pass[i],row_low, row_high)
    # Choose row
    if boarding_pass[i] == 'F':
        row = row_low
    if boarding_pass[i] == 'B':
        row = row_high - 1

    # Find seat
    seat_low, seat_high = 0, 8
    for i in range(7,10):
        if boarding_pass[i] == 'R':
            seat_low = seat_high - (seat_high-seat_low)/2
        if boarding_pass[i] == 'L':
            seat_high = seat_high - (seat_high-seat_low)/2
        #print(boarding_pass[i],seat_low, seat_high)
    # Choose seat
    if boarding_pass[i] == 'R':
        seat = seat_high - 1
    if boarding_pass[i] == 'L':
        seat = seat_low

    #print(boarding_pass, row, seat)

    return row * 8 + seat

def number_one() -> int:
    '''Find highest seat ID on all boarding passes'''
    with open('input.txt', 'r') as input_file:
        boarding_passes = [line.rstrip("\n") for line in input_file.readlines()]

    #boarding_passes = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    highest_id = 0
    for boarding_pass in boarding_passes:
        pass_id = calc_seat_id(boarding_pass)
        if pass_id > highest_id:
            highest_id = pass_id

    return highest_id

def number_two():
    '''Find your seat!'''
    with open('input.txt', 'r') as input_file:
        boarding_passes = [line.rstrip("\n") for line in input_file.readlines()]

    #boarding_passes = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    all_ids = []
    for boarding_pass in boarding_passes:
        pass_id = calc_seat_id(boarding_pass)
        all_ids.append(pass_id)

    sorted_ids = sorted(all_ids)
    for i in range(len(all_ids)):
        if sorted_ids[i+1] == sorted_ids[i] + 2:
            return sorted_ids[i] +1

    return 0

print('Ans 1: ', number_one())
print('Ans 2: ', number_two())

