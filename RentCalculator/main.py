#!/usr/bin/env python3
'''
I need a program that will help me figure out how much my budget must be to afford an apartment.
'''


# Calculate the total cost of a specific lease agreement eg 3 months based on the building class 
def total_cost(months, building):
    total = 0
    breakdown = ''

    for i in range(months):
        if i == 0:
            month1_cost = building.admin_fee + building.deposit + building.rent + building.utilities
            breakdown += f'First month: R{month1_cost} ({building.admin_fee} admin fee + {building.deposit} deposit + {building.rent} rent + {building.utilities} utilities)\n'
            total += month1_cost
        else:
            monthly_cost = building.rent + building.utilities
            breakdown += f'Month {i + 1}: R{monthly_cost} ({building.rent} rent + {building.utilities} utilities)\n'
            total += monthly_cost
    return f'Total cost breakdown for {building.name} {building.unit_type} over {months} months:\n{breakdown}Total Cost: R{total}'

def filter_buildings_by_budget(building_list, budget, max_over_budget=500):
    filtered_buildings = []
    for building in building_list:
        rent = int(building['Price Description'].replace('R', '').replace(' ', ''))
        if rent <= budget + max_over_budget:
            filtered_buildings.append(building)
    return filtered_buildings

def display_buildings(buildings):
    print("\nAvailable Buildings:")
    for index, building in enumerate(buildings, start=1):
        print(f"{index}. {building.name} - {building.unit_type} - R{building.rent}")
        print(f"   Seller: {building.prop_group}")
        #print(f"   Suburb: {building.suburb}")
        #print(f"   Address: {building.address}")
        print("------------------------")
    print()
