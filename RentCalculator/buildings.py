'''
Module to hold building rental data
'''

# Advertised_price = 1925
# Admin_fee = 1100
# Deposit = Advertised_price
# Utilities = 611

# create classes that will hold different building rental price data
class Building:
    # Assume rent and deposit are always equal
    def __init__(self, prop_group, name,unit_type,address, rent, admin_fee, deposit, utilities):
        self.prop_group = prop_group
        self.name = name
        self.unit_type = unit_type
        self.rent = rent
        self.admin_fee = admin_fee
        self.deposit = deposit
        self.utilities = utilities
        self.address = address
    
    def __str__(self):
        
        return f"{self.name} costs {self.rent+self.utilities} per month"
    
    def __repr__(self):
        return f"{self.prop_group},{self.name}, {self.rent}, {self.admin_fee}, {self.deposit}, {self.utilities}"
