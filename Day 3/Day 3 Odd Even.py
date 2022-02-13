# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 11:05:11 2022

@author: HP
"""

number = int(input("Which number do you want to check? "))


#If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
  print("This is an even number.")
  
#Otherwise (number cannot be divided by 2 with 0 remainder).
else:
  print("This is an odd number.")
