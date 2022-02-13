# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 15:07:18 2022

@author: HP
"""

import random

for i in range(4):
    names_string = input("Give me a name ")
names = names_string.split(", ")


num_items = len(names)

random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")
