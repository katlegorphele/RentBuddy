'''
Module to scrape the property websites
'''
from bs4 import BeautifulSoup
import requests

def get_private_property():
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

def get_buildings():
    buildings_list = []
    buildings_list.extend(get_private_property())
    return buildings_list

