# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 10:21:28 2022

@author: HP
"""

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [num for num in numbers if num%2==0]


print(result)