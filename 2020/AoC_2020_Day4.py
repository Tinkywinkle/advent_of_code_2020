# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 17:56:40 2020

@author: hamis
"""

data = []
passport = {}

    

file = open("Passports.txt", "r")

for line in file:
    if line == "\n":
        data.append(passport)
        passport = {}
    else:
        line = line.split()
        for attribute in line:
            key, value = attribute.split(":")
            passport[key] = value
# adds last line as no \n at end            
data.append(passport)
    
def validPassportsA(passportList):
    
    """Takes a passport list and returns the number of valid passports that
    have the keys: "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" """
    
    validPassports = 0
    
    for passport in passportList:
        if passport.keys() >= {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}:
            validPassports += 1
    
    return validPassports

def validPassportsB(passportList):
    
    """Takes a passport list and returns the number of valid passports that
    have the keys: "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" within 
    strict criteria. """
    
    validPassports = 0
    characters = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f")
    eyecolour = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    
    # check each passport for strict criteria
    for passport in passportList:
        if not passport.keys() >= {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}:
            pass
        elif not (1920 <= int(passport['byr']) <= 2002):
            pass
        elif not (2010 <= int(passport["iyr"]) <= 2020):
            pass
        elif not (2020 <= int(passport["eyr"]) <= 2030):
            pass
        elif len(passport["hcl"]) != 7 or passport["hcl"][0] != "#":
            pass
        elif not all (char in characters for char in passport["hcl"][1:]):
            pass 
        elif not (passport["hgt"][-2:] == "cm" and int(passport["hgt"][:-2]) >= 150 and int(passport["hgt"][:-2]) <= 193) and not (passport["hgt"][-2:] == "in" and int(passport["hgt"][:-2]) >= 59 and int(passport["hgt"][:-2]) <= 76):
            pass
        elif not (passport["ecl"] in eyecolour):
            pass
        elif len(passport["pid"]) != 9 or not(int(passport["pid"])):
            pass
        else:
            validPassports += 1

    return validPassports


print('The number of valid passports in question A is:', validPassportsA(data)) 
print('The number of valid passports in question A is:', validPassportsB(data))

