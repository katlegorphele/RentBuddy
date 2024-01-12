from bs4 import BeautifulSoup
import requests
from buildings import Building
from main import total_cost, filter_buildings_by_budget, display_buildings
from rentbuddy import get_buildings, create_building_objects

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
