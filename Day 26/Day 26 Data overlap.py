# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 10:50:41 2022

@author: HP
"""

with open("file1.txt") as file1:
    list1 = file1.readlines()
    
with open("file2.txt") as file2:
    list2 = file2.readlines()
    
result = [int(num) for num in list1 if num in list2]


print(result)



