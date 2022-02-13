# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 12:24:12 2022

@author: HP
"""


even_sum = 0
for number in range(2, 101, 2):
  # print(number)
  even_sum += number
print(even_sum)
  

# alternative_sum = 0
# for number in range(1, 101):
#   if number % 2 == 0:
#     # print(number)
#     alternative_sum += number
# print(alternative_sum)