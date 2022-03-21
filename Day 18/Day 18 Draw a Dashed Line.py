# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 21:44:42 2022

@author: HP
"""

import turtle as t

tim = t.Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()