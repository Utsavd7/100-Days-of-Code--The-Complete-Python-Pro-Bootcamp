# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 10:57:46 2022

@author: HP
"""

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}


print(weather_f)