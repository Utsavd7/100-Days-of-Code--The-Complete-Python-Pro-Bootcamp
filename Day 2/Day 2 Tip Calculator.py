# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 19:11:27 2022

@author: HP
"""

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? Rs "))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
#percentage tip

people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100 
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: Rs {final_amount}")