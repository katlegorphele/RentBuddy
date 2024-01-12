#!/usr/bin/env python3

'''
Module meant to help a first time renter 
navigate the rental market in South Africa
Uses beautiful soup to get rent data from property websites
and calculates the approximate total cost of renting a property

It must factor in budget and filter out places that are too expensive
but it must also have a threshold for the max amount over budget
'''

from buildings import Building
from buildingscraper import get_buildings
from main import filter_buildings_by_budget, display_buildings, total_cost


#Instantiate a building class for each building
def create_building_objects(building_list):
    buildings = []
    for building in building_list:
        # Assume rent and deposit are always equal
        rent = int(building['Price Description'].replace('R', '').replace(' ', ''))
        admin_fee = 1100
        deposit = rent
        utilities = 611
        new_building = Building(building['Seller'], building['Title'], building['Property Type'], building['Address'], rent, admin_fee, deposit, utilities)
        buildings.append(new_building)
    return buildings
    
def main():
    # Get user's budget input
    budget = float(input("Enter your budget for rent: R"))

    # Get list of available buildings within budget
    building_list = filter_buildings_by_budget(get_buildings(), budget)

    # Create building objects
    my_buildings = create_building_objects(building_list)

    # Display available buildings
    display_buildings(my_buildings)

    # User selects a building
    selected_building_index = int(input("Enter the number of the building you're interested in: "))
    selected_building = my_buildings[selected_building_index - 1]

    # User specifies the number of months
    months_to_rent = int(input("Enter the number of months you want to rent: "))

    # Calculate and display total cost
    print(total_cost(months_to_rent, selected_building))

if __name__ == "__main__":
    main()






