#!/usr/bin/env python3
'''
I need a program that will help me figure out how much my budget must be to afford an apartment.
'''


# Calculate the total cost of a specific lease agreement eg 3 months based on the building class 
def total_cost(months, building):
    total = 0
    for i in range(months):
        if i == 0:
            total += building.admin_fee + building.deposit + building.rent + building.utilities
        else:
            total += building.rent + building.utilities
    return f'It will cost R{total } to rent {building.name} {building.unit_type} for {months} months'


