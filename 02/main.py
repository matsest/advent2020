#!/usr/bin/env python3
"https://adventofcode.com/2020/day/2"

from typing import Union

def parse_line(line: str) -> Union[int, int, str, str]:
    '''Parses a line "1-3 a: pasfdsafsd" -> int, int, str, str'''
    parts = line.rsplit(" ")
    letter_min_count, letter_max_count = [int(n) for n in parts[0].rsplit("-")]
    letter = parts[1].strip(":")
    password = parts[2]

    return letter_min_count, letter_max_count, letter, password

def validate_password(letter_min_count: int, letter_max_count: int, letter: str, password: str) -> bool:
    '''Check if a password is valid based on the letter policy'''

    if (password.count(letter) >= letter_min_count) and (password.count(letter) <= letter_max_count):
        return True

    return False

def validate_password2(letter_pos1: int, letter_pos2: int, letter: str, password: str) -> bool:
    '''Check if a password is valid based on the position based letter policy'''

    # Only one of the positions must match, this corresponds to a xor
    if (password[letter_pos1 - 1] == letter) ^ (password[letter_pos2 - 1] == letter):
        return True

    return False

def number_one() -> int:
    '''Find number of valid passwords based on policy'''
    with open("input.txt", 'r') as input_file:
        lines = [line for line in input_file.readlines()]

    valid_count = 0

    for line in lines:
        letter_min_count, letter_max_count, letter, password = parse_line(line)

        if validate_password(letter_min_count, letter_max_count, letter, password):
            valid_count += 1

    return valid_count

def number_two() -> int:
    '''Find number of valid passwords based on new policy'''
    with open("input.txt", 'r') as input_file:
        lines = [line for line in input_file.readlines()]

        valid_count = 0

        for line in lines:
            letter_pos1, letter_pos2, letter, password = parse_line(line)

            if validate_password2(letter_pos1, letter_pos2, letter, password):
                valid_count += 1

    return valid_count

print('Ans 1: ', number_one())
print('Ans 2: ', number_two())

