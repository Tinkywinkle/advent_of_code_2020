# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:27:54 2020

@author: hamis
"""
# creates a list of passwords from file.  Each item in the list contains 3 items:
# a password policy, the key letter, and the password

passwordList = []
file = open("PasswordList.txt", "r")

for line in file:
    temp = line.rstrip("\n")
    passwordList.append(temp.split(" "))
    
  
def numValidLetters(numbers):
    """ takes a string with 2 numbers seperated by a hyphen, and returns both
    numbers as integers."""
    
    stringNumbers = numbers.split("-")
    x = int(stringNumbers[0])
    y = int(stringNumbers[1])
    
    return x, y

    
def isPasswordValidA(passwordList): 
    """ Takes a password list in which each password contains a list with a
    range of needed correct letters, the correct letter needed and the password.
    Returns the number of correct passwords that meet this criteria in the list. """
    
    correctPassword = 0
    
    for item in passwordList:
        count = 0
        
        # get the number of valid letters
        x, y = numValidLetters(item[0])
        
        # check if any character in the password matches the password policy
        # character
        for character in item[2]:
            if character == item[1][0]:
                count += 1
        
        # check if the number of correct policy characters are within the 
        # policy character range.  Add this to this correct password count
        # if true
        if count >= x and count <= y:
            correctPassword += 1
            
    return correctPassword


def isPasswordValidB(passwordList):
    """ Takes a password list in which each password contains a list with the 
    two possible positions of the correct letters, the correct letter needed 
    and the password.
    Returns the number of correct passwords that meet this criteria in the list
    (only one letter must be in the correct position, not both). """
    
    correctPassword = 0
    
    for item in passwordList:
        
        # get the valid letter positions
        x, y = numValidLetters(item[0])
        x -= 1  # corrects letter position in string
        y -= 1  # corrects letter position in string
        
        
        # check to see if one letter is on the correct position, 
        # and the other is not.  Add this to the correct password count if true.
        if item[2][x] == item[1][0] and item[2][y] != item[1][0]:
            correctPassword += 1
        elif item[2][y] == item[1][0] and item[2][x] != item[1][0]:
            correctPassword += 1
        
            
    return correctPassword
        

print("The number of valid passwords for Question 1 is:", 
      isPasswordValidA(passwordList))

print("The number of valid passwords for Question 2 is:", 
      isPasswordValidB(passwordList))