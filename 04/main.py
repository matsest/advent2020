#!/usr/bin/env python3
"https://adventofcode.com/2020/day/4"

from typing import List
import re

def parse_passports(inputfile: str) -> List[dict]:
    '''Parse passports'''
    with open(inputfile, 'r') as input_file:
        lines = [line.rstrip("\n") for line in input_file.readlines()]

    # Transform input to dictionary 
    passports = [{}]
    i = 0
    for line in lines:
        #print(line.split())
        if line != '':
            for k in line.split():
                k,v = k.split(':')
                passports[i][k] = v
        else:
            passports.append({})
            i += 1

    return passports

def validate_key(k:str, v: str) -> bool:
    '''Validate if key is in specific format'''
    validation = False

    if k == 'byr':
        if int(v) <= 2002 and int(v) >= 1920:
            validation = True
    if k == 'iyr':
        if int(v) <= 2020 and int(v) >= 2010:
            validation = True
    if k == 'eyr':
        if int(v) <= 2030 and int(v) >= 2020:
            validation = True
    if k == 'hgt':
        if v.endswith('cm'):
            h = v.split('cm')[0]
            if int(h) <= 193 and int(h) >= 150:
                validation = True
        if v.endswith('in'):
            h = v.split('in')[0]
            if int(h) <= 76 and int(h) >= 59:
                validation = True
    if k == 'hcl':
        if re.search("^#[a-f,0-9]{6}$",v):
            validation = True
    if k == 'ecl':
        valids = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if v in valids:
            validation = True
    if k == 'pid':
        if re.search("^[0-9]{9}$", v):
            validation = True
    if k == 'cid':
        validation = True

    return validation


def number_one() -> int:
    '''Check for passports with mandatory keys'''
    passports = parse_passports('input.txt')
    mandatory_keys = ['ecl','pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    valid_count = 0

    for passport in passports:
        if all (k in passport for k in mandatory_keys):
            valid_count += 1

    return valid_count

def number_two():
    '''Check for passports with mandatory keys and validate all keys'''
    passports = parse_passports('input.txt')
    mandatory_keys = ['ecl','pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    valid_count = 0

    for passport in passports:
        if all (k in passport for k in mandatory_keys):
            if all (validate_key(k, passport[k]) for k in passport):
                valid_count += 1

    return valid_count

print('Ans 1: ', number_one())
print('Ans 2: ', number_two())

