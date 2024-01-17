#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()
more_trips = 'y'

while more_trips == "y":

    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    gas_price = float(input("What is the price of gas:    "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif gas_price <= 0:
        print("Gas price must be greater than 0. Try again")
    else:
        # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        gas = round(gallons_used * gas_price, 1)
        gas_mile =  round(gas/ miles_driven, 1)
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:    ", gas)
        print("Cost Per Mile:    ", gas_mile)
        
    more_trips = input("Do you want to calculate more trips? (y/n)")
    print()
print("Bye!")



