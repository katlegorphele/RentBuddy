#!/usr/bin/env python3

'''
Module meant to help a first time renter 
navigate the rental market in South Africa
Uses beautiful soup to get rent data from property websites
and calculates the approximate total cost of renting a property

It must factor in budget and filter out places that are too expensive
but it must also have a threshold for the max amount over budget
'''

from bs4 import BeautifulSoup
import requests
from buildings import Building
from main import total_cost

# Get a list of all the buildings in the area
def get_buildings():
    # Get the html from the website
    url = 'https://www.privateproperty.co.za/to-rent/gauteng/johannesburg/johannesburg-cbd-and-bruma/marshalltown/1896?pt=2&sorttype=1&quicksearchpropertytype=3'
    response = requests.get(url)
    # Create a beautiful soup object
    soup = BeautifulSoup(response.text, 'lxml')
    # Get the building names
    buildings = soup.find_all('div', class_='infoHolder')
    # Create a list to hold all the building names
    building_list = []
    # Loop through the buildings and add them to the list
    for index, building in enumerate(buildings):
        seller = building.find('div', class_='bankOfficeOrPrivateSeller')
        if seller is not None:
            img_tag = seller.find('img')
            if img_tag is not None:
                seller = img_tag.get('alt')
        title = building.find('div', class_='title').text
        price_description = building.find('div', class_='priceDescription').text
        # price_additional_descriptor = building.find('div', class_='priceAdditionalDescriptor').text
        property_type = building.find('div', class_='propertyType').text
        suburb = building.find('div', class_='suburb').text
        address = building.find('div', class_='address')
        if address == None:
            address = 'No address listed'
        else:
            address = address.text


        building_info = {
            'No': index + 1,
            'Seller': seller,
            'Title': title,
            'Price Description': price_description,
            'Property Type': property_type,
            'Suburb': suburb,
            'Address': address,
        }

        building_list.append(building_info)
    return building_list

#Instantiate a building class for each building
def create_building_objects(building_list):
    buildings = []
    for building in building_list:
        # Assume rent and deposit are always equal
        rent = int(building['Price Description'].replace('R', '').replace(' ', ''))
        admin_fee = 1100
        deposit = rent
        utilities = 611
        new_building = Building(building['Seller'], building['Title'], building['Property Type'], rent, admin_fee, deposit, utilities)
        buildings.append(new_building)
    return buildings
    
my_buildings = create_building_objects(get_buildings())

# for building in my_buildings:
#     print(building)
#     print(total_cost(6, building))
#     print()






