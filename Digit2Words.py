# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:46:38 2017

@author: gan_wei
version: python 3.5

"""

from collections import defaultdict
KEYBOARD = {2: 'ABC', 3: 'DEF', 4: 'GHI',
            5: 'JKL', 6: 'MNO', 7: 'PQRS',
            8: 'TUV', 9: 'WXYZ'}
DICT = ['FASTCAR','FAST','CAR','OF','VISITED', 'ONEFASTCAR','ONE']
INPUT = '6633278227'


# create a new dict with digit and words:
# {'227': 'CAR',
#  '3278': 'FAST',
#  '3278227': 'FASTCAR',
#  '63': 'OF',
#  '8474833': 'VISITED'}
def mk_dict(zipped):
    return {k:v for k,v in zipped}


# get reverse keyboard(get digit by char)
def get_digit_by_char():
    reverse_keyboard = {}
    for k, v in KEYBOARD.items():
        reverse_keyboard.update({letter: str(k) for letter in v})
    return reverse_keyboard


def is_word(string):
    return True if new_dict.get(string) else False


# split each phase into words if it is a phase, each word is at least 3-char long
def word_in_phase (dial=INPUT):
    pointer = 3
    while len(dial)>= 3 or len(dial)-pointer >= 3:
        if is_word(dial[:pointer]):
            return [new_dict[dial[:pointer]]] + word_in_phase(dial[pointer:])
        else:
            pointer += 1
    return []


# combine words into phases
def word_to_phase(ls):
    combinations = []
    for i in range(0, len(ls)):
        combinations.extend([''.join(ls[i:j]) for j in range(i+1,len(ls)+1)])
    return combinations

# create digit list comprehension corresponding to DICT:
# ['3278227', '3278', '227', '3278227', '63', '8474833', '227', '3278227227']
reverse_keyboard = get_digit_by_char()
digit_list = [''.join(map(reverse_keyboard.get, word)) for word in DICT]

# zip digit list and DICT
zipped = zip(digit_list,DICT)
new_dict = mk_dict(zipped)
# find all phase combinations with words given
phases = word_to_phase(word_in_phase())
output = []
for phase in phases:
    if phase in DICT:
        output.append(phase)



