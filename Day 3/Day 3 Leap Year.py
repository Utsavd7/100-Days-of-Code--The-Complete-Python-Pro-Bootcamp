# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 11:10:17 2022

@author: HP
"""

year = int(input("Which year do you want to check? "))


if year % 4 == 0:
    
  if year % 100 == 0:
      
    if year % 400 == 0:
      print("Leap year.")
    
    else:
      print("Not leap year.")
  
  else:
    print("Leap year.")

else:
  print("Not leap year.")